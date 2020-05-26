# The function converts the number to a single format
import re


def phone_converter(phone):
    phone = re.sub(r"[()-]", "", phone).replace(' ', '')
    return phone
