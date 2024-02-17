##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import datetime as dt
import random
import smtplib

PLACEHOLDER = "[NAME]"
DOCUMENTS = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
document = random.choice(DOCUMENTS)

my_email = "danilotanuso@gmail.com"
password = "cwyu adfk iabm wrlh"

data = pandas.read_csv("birthdays.csv")
name = data["name"].to_list()

now = dt.datetime.now()
current_day = now.day
current_month = now.month
for n in name:
    name_row = data[data.name == n]
    b_day = name_row.day                     #The specific day of each name
    b_month = name_row.month                 # The specific month of each name
    if int(b_day.iloc[0]) == current_day and int(b_month.iloc[0]) == current_month:
        b_name = (data[data.day == b_day.iloc[0]]).name
        b_email = (data[data.day == b_day.iloc[0]]).email
        with open(document) as file:
            content = file.read()
            happy_name = b_name.values[0].strip()
            new_letter = content.replace(PLACEHOLDER, happy_name)
            with open(f"./letter_templates/letter_for_{happy_name}.txt", mode="w") as completed:
                completed.write(new_letter)
            with open(f"./letter_templates/letter_for_{happy_name}.txt", mode="r") as copy:
                to_send = copy.readlines()
                email_body = "".join(to_send)

        happy_email = b_email.values[0]
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=happy_email,
                                msg=f"Subject:Happy Birthday!!!\n\n{email_body}"
                                )









