import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weeday = now.weekday()

my_email = "appbreweryinfo@gmail.com"
password = "Vejoaewrfu9*0E"
if weeday == 1:
    with open("quotes.tx") as quotes_files:
        all_quotes = quotes_files.readlines()
        quote_of_the_day  = random.choice(all_quotes)
    with smtplib("smtp.gmailcom") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(form_addr=my_email, 
                            to_addrs="appbrewerytesting@yahoo.com", 
                            msg=f"Subject:Unknown{quote_of_the_day}"
                            ) 
