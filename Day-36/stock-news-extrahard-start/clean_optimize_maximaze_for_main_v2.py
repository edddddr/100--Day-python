import os
import datetime
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables
load_dotenv()


# Constants
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_URL = "https://www.alphavantage.co/query"
NEWS_API_URL = "https://newsapi.org/v2/everything"
PRICE_CHANGE_THRESHOLD = 5  # percent

NEWS_API_KEY = os.getenv("NEWS_API-KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
TWILIO_FROM = "+12344152831"
TWILIO_TO = "+251912138331"


def get_previous_date(days_ago: int) -> str:
    date = datetime.datetime.today() - datetime.timedelta(days=days_ago)
    return date.strftime("%Y-%m-%d")

def fetch_news(company: str, api_key: str, limit: int = 3):
    params = {'q': company, 'apikey': api_key}
    response = requests.get(NEWS_API_URL, params=params)
    response.raise_for_status()
    articles = response.json().get('articles', [])[:limit]
    return [{'headline': a['title'], 'brief': a['description']} for a in articles]


def fetch_stock_data(symbol: str, api_key: str):
    params = {
        'function': "TIME_SERIES_DAILY",
        'outputsize': 'compact',
        'symbol': symbol,
        'apikey': api_key
    }
    response = requests.get(STOCK_API_URL, params=params)
    response.raise_for_status()
    return response.json()["Time Series (Daily)"]

def calculate_price_change(data: dict, date1: str, date2: str) -> float:
    price1 = float(data[date1]['4. close'])
    price2 = float(data[date2]['4. close'])
    return round(abs(price1 - price2) / ((price1 + price2) / 2) * 100, 2)

def send_alert(message: str):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    sms = client.messages.create(body=message, from_=TWILIO_FROM, to=TWILIO_TO)
    print(sms.body)



stock_data = fetch_stock_data(STOCK, STOCK_API_URL)
news_data = fetch_news(NEWS_API_URL, NEWS_API_KEY)
price_percentage = calculate_price_change(stock_data, get_previous_date(2), get_previous_date(3))

send_alert(f'TSLA: 🔺{price_percentage} % Headline:{news_data[0]['headline']} Brief:{news_data[0]['brief']}')


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or"""

"""TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""




