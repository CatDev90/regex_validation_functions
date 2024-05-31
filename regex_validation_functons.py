import re

"""
Simple functions for validating phone numbers and email address.
The regular expressions can be changed to suit your reqiurements.
"""

# Validators
def validate_phone_number(phone_number):
    """
    A function for validating uk phone numbers
    """
    reg_pattern = r'07\d{9,13}|447\d{7,12}' #regex for uk mobile numbers
    if re.match(reg_pattern, phone_number): # if the phone number matches the reg_pattern then return value
        return reg_pattern


def validate_email(email):
    """
    A function for validating email addresses
    """  
    reg_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' # regex for valid emails
    if re.match(reg_pattern, email): # if the email matches the reg_pattern then return value
        return email