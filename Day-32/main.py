import smtplib

my_email = "appbreweryinfo@gmail.com"
password = "Vejoaewrfu9*0E"

with smtplib.SMTP("smtp.gmailcom") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(form_addr=my_email, 
                        to_addrs="appbrewerytesting@yahoo.com", 
                        msg="Subject:Hello\n\nThis is the body of my email."
                        )