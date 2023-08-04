from datetime import datetime
import pandas as pd
from random import randint
from smtplib import SMTP

MY_EMAIL = "brunocool719@gmail.com"
MY_PASSWORD = "nbloqgodrucgiuig"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday {birthday_person['name']}!\n\n{contents}"
        )
