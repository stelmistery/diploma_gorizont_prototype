import re

def phone_converter(phone):
    phone = re.sub(r"[()-]", "", phone).replace(' ', '')
    return phone

# def check_user_exist(phone, email):
#     if CustomerUser.objects.get(email=email).