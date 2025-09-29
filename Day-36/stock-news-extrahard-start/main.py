import os
import datetime
from dotenv import load_dotenv
from twilio.rest import Client

import requests

load_dotenv()

# variable declaration
STOCK = "TSLA"
news = []
COMPANY_NAME = "Tesla Inc"
stock_api_end_point ='https://www.alphavantage.co/query'
news_api_end_point = 'https://newsapi.org/v2/everything'
ava_api_key = os.getenv("AVA_API_KEY")
news_api_key = os.getenv("NEWS_API-KEY")
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

# parameters
url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2025-09-26&'
       'sortBy=popularity&')

parameter_for_stock = {
    'function' : "TIME_SERIES_DAILY",
    'outputsize':'compact',
    'symbol' : STOCK,
    'apikey' : ava_api_key
}

parameter_for_news = {
    'q': 'tesla',
    'apikey' : news_api_key
}


def get_response(api_end_point, parameter):
    """" Get response data in a given endpoint"""
    response = requests.get(api_end_point, params=parameter)
    response.raise_for_status()
    return response.json()

def date_converter(num) -> str:
    """" It giv a day, which is the
         day before and the day before
          yesterday """
    split_current_day = str(datetime.datetime.today().date()).split('-')
    date = int(split_current_day[2])
    split_current_day[2] = str(date - num)
    return  "-".join(split_current_day)


time_series_data = get_response(stock_api_end_point, parameter_for_stock)["Time Series (Daily)"]
news_data = get_response(news_api_end_point, parameter_for_news)

news_slice = news_data['articles'][:3]
for article in news_slice:
    headline = article['title']
    brief = article['description']

    news.append({'headline': headline, 'brief': brief})


yesterday = date_converter(1)
the_day_yesterday = date_converter(2)

yesterday_close_price = float(time_series_data[yesterday]['4. close'])
the_day_yesterday_close_price = float(time_series_data[the_day_yesterday]['4. close'])

percentage_of_current_stock_price = round(((abs(yesterday_close_price - the_day_yesterday_close_price) /
            ((yesterday_close_price + the_day_yesterday_close_price) / 2)) * 100), 2)


print(percentage_of_current_stock_price)

if percentage_of_current_stock_price + 5:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"TSLA: {round(percentage_of_current_stock_price,2)}% Headline: {news[0]['headline']} Brief: {news[0]['brief']}",
        from_="+12344152831",
        to="+251912138331",
    )
    print(message.body)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

