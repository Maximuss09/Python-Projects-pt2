import smtplib
import datetime as dt
import random


my_email = "themexicaniamafia@gmail.com"
my_password = "euqs scie ylvq qlfr" 
test_account = "testeraccount690@yahoo.com"


now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("Day32_SendEmail/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= test_account,
            msg=f"Subject: Monday Motivational Lettet \n\n{quote}"
        )



# my_email = "themexicaniamafia@gmail.com"
# password = "euqs scie ylvq qlfr"

# with smtplib.SMTP("smtp.gmail.com") as connection
#     connection.starttls()
#     connection.login(user=my_email ,password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="testeraccount690@yahoo.com", 
#         msg="Subject: Hello MF\n\nThis is the body of my email"
#         )

# import datetime as dt

# now = dt.datetime.now()
# print(now)


