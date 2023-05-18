#import smtplib


#my_email = "irina_po1@yahoo.com"
#password = "xafzikebmhhjnkcc"


#my_email = irina.po1122@gmail.com
#password = "230520emma"

#with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email,
#                        to_addrs="irina.po1122@gmail.com",
#                        msg="Subject:Hello\n\n This is my email.")

#import datetime as dt
#now = dt.datetime.now()
#year = now.year
#month = now.month
#day_of_week = now.weekday()
#print(year)

#date_of_birth = dt.datetime(year=1995, month=12, day=15)
#print(date_of_birth)
import random
import smtplib
import datetime as dt

my_email = "irina_po1@yahoo.com"
password = "rouqtonypetuuwgt"

with open("quotes.txt") as text:
    quotes_list = text.read().splitlines()


now = dt.datetime.now()

if now.weekday() == 5:
    random_quote = random.choice(quotes_list)
    print(random_quote)
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="irina.po1122@gmail.com",
                            msg=f"Subject:Quote of the day\n\n {random_quote}")

#with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email,
#                        to_addrs="irina.po1122@gmail.com",
#                        msg="Subject:Hello\n\n This is my email.")
