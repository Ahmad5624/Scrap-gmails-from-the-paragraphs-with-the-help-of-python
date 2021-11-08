import phonenumbers
import re
try:
    for match in phonenumbers.PhoneNumberMatcher(description, ("US" or "IN" or "PAK" or "CA" or "CN")):     #enter the region
        number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        try:
            number = number.replace("+1 ", "")
        except Exception:
            pass
        print(number)
except Exception:
    pass

try:
    emails = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", description) #description is the value where you want to scrap mails from
    for mail in emails:
        print("Email:", mail)
except Exception:
    pass