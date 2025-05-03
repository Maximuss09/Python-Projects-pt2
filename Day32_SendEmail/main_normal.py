from datetime import datetime
import pandas
import random
import smtplib

my_email = "themexicaniamafia@gmail.com"
my_password = "euqs scie ylvq qlfr" 

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("Day32_SendEmail/birthdays.csv")
birthday_dictionary = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# new_dict = {new_key:new_value for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dictionary:
    birthday_person = birthday_dictionary[today_tuple]
    file_path = f"Day32_SendEmail/letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr= my_email,
            to_addrs= birthday_person["email"],
            msg= f"Subject: HAPPY BIRTHDAY!!!\n\n{contents}"

        )




