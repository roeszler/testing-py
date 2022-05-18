import gspread
from google.oauth2.service_account import Credentials
import re # regular extensions import for checking syntax of email
import os

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')

# REGEX_NAME = r'^[a-zA-Z]$'
REGEX_EMAIL = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

user_data = ['f_name', 'l_name', 'user_email']
order_data = ['size_eu', 'height', 'width']

# orders = SHEET.worksheet('orders')
# data = orders.get_all_values()
# print(data)

# def start_select_option():
#     """
#     Start screen prompting user to:
#     1. Create a new order, or
#     2. Retrieve an exsisting order with order number
#     """


def instruct_user_data():
    """
    Insruct User on format of first name, last name and email.
    """
    print('Where prompted below, please enter your name and email.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')
    
    print('First Name: Bobby\nLast Name: Hunden')
    print('Email: bobby123@yourdomain.com\n')
    get_user_data()


def get_user_data():
    """
    User input of first name, last name and email to from a string
    with fist letter capitalized for names and all lowercase email 
    """
    f_name = remove(input('Your First Name: ').capitalize())
    user_data[0] = f_name
    print(user_data)

    l_name = remove(input('Your Last Name: ').capitalize())
    user_data[1] = l_name
    print(user_data)

    user_email = remove(input('Your Email: ').lower())
    user_data[2] = user_email
    print(user_data)
    
    print(f'\nThanks {f_name}. Your user details are as follows:')
    print('------------')
    print(f'Full Name: {f_name} {l_name}\nEmail: {user_email}')
    print('------------\n')
    validate_user_names(f'{f_name}')
    validate_user_names(f'{l_name}')
    validate_user_email(f'{user_email}')



def validate_user_names(values):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    # values_string = f'{values.split(",")}'
    # print(f'The user_data you provided converted into a list of strings is:\n{values_string}\n')

    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            print('Name is valid...')
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Please check the entry and try again.\n')
        get_user_data()








def validate_user_email(values):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    values_string = f'{values.split(",")}'
    # print(f'The user_data you provided converted into a list of strings is:\n{values_string}\n')

    try:
        if (re.fullmatch(REGEX_EMAIL, values)):
            print('Email is valid...')
            yes_no_user()
        else:
            raise ValueError(
                f'The email you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Please check the entry and try again.\n')
        user_email = remove(input('Your Email: ').lower())
        user_data[2] = user_email
        print(user_data)
        validate_user_email(user_email)


def remove(string):
    """
    Removes all spaces in string inputs
    """
    return string.replace(' ', '')


def get_latest_row_entry():
    """
    
    """
    orders = SHEET.worksheet('orders').get_values('A:F')
    email = orders[-1]
    print(email)


def yes_no_user():
    """
    """
    correct = input('\nIs this information correct? y/n: ').lower()
    if correct.startswith('y'):
        print('Updating worksheet and proceeding to order_data...\n')
        return True
    else:
        main()

def main():
    """
    Run all program functions
    """
    # instruct_user_data()
    user = get_user_data()
main()

# get_latest_row_entry()
# validate_user_email(values='stuart@roeszler.com')
# validate_user_names(values='stuart Roes3ler')