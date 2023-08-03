import smtplib
import datetime as dt
from random import choice

MY_EMAIL = "brunocool719@gmail.com"
MY_PASSWORD = "nbloqgodrucgiuig"

now = dt.datetime.now()
weekday = now.weekday()

# If the week day is equals to monday
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)

    print(quote)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

#     with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#         connection
# my_email = "brunocool719@gmail.com"
# password = "nbloqgodrucgiuig"
# receiver_email = "bruno.santos@elogroup.com.br"
#
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs=receiver_email,
#         msg="Subject: Hello bro\n\n"
#             "This is the body of my email."
#     )
#
#
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)