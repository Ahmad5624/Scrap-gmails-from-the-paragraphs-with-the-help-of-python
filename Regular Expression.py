import re

try:
    emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", description) #description is the value where you want to scrap mails from
    for mail in emails:
        print("Email:", mail)
except Exception:
    pass
