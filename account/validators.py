from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    if re.match(r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,12}$', value):
        return value
    else:
        raise ValidationError("A valid phone number must be entered in")

