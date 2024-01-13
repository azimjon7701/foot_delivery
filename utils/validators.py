import re
from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

@deconstructible
class PhoneNumberValidator(validators.RegexValidator):
    regex = r"^\+?1?\d{9,15}$"
    message = _(
        "Enter a valid phone number. The number may start with an optional '+' sign, followed by 9 to 15 digits."
    )
    flags = re.ASCII
