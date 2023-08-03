import smtplib

my_email = "brunocool719@gmail.com"
password = "nbloqgodrucgiuig"
receiver_email = "bruno.santos@elogroup.com.br"

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=receiver_email,
        msg="Subject: Hello bro\n\n"
            "This is the body of my email."
    )

