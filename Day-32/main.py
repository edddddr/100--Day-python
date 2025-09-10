import smtplib
import random
import datetime as dt

import pandas

MY_EMAIL = "endt6342@gmail.com"
MY_PASSWORD = "cnbqubgpmobilcjt"


today = dt.datetime.now()
today_tuple = (today.month, today.day)
data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents.replace("[Name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="ermaisthomas97",
            msg=f"Subject: Happy Birthday\n\n{contents}"
        )