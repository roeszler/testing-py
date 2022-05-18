import gspread
from google.oauth2.service_account import Credentials
import re # regular extensions import for checking syntax of email

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')

REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# F_NAME = 

# sales = SHEET.worksheet('orders')
# data = sales.get_all_values()
# print(data)

# def start_select_option():
#     """
#     Start screen prompting user to:
#     1. Create a new order, or
#     2. Retrieve an exsisting order with order number
#     """


def get_user_data():
    """
    Get User first name, last name and email from user as a string
    """
    print('Where prompted below, please enter your name and email.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')
    
    print('First Name: Bobby\nLast Name: Hunden')
    print('Email: bobby123@yourdomain.com\n')
    
    f_name = remove(input('Your First Name: ').capitalize())
    l_name = remove(input('Your Last Name: ').capitalize())
    user_email = remove(input('Your Email: ').lower())
    
    print(f'\nThanks {f_name}. Your user details are as follows:')
    print('------------')
    print(f'Full Name: {f_name} {l_name}\nEmail: {user_email}')
    print('------------\n')
    yes_no_user()
    
    validate_user_data(f'{f_name},{l_name},{user_email}')
    # user_data = [f_name, l_name, user_email]
    # print(user_data)

def remove(string):
    return string.replace(' ', '')


def validate_user_data(values):
    """
    Inside the try, converts all user_email inputs into floats.
    Raises ValueError if strings cannot be converted into float or
    if height == low or mid or high string values or 
    if width == narrow or standard or wide.
    """
    print(f'The user_data you provided converted into a list of strings is:\n{values.split(",")}\n')



def yes_no_user():
    correct = input('Is this information correct? y/n: ').lower()
    if correct.startswith('y'):
        # print(f'Thanks *** , updating worksheet and proceeding to order_data\n')
        return True
    else:
        main()

def main():
    """
    Run all program functions
    """
    user = get_user_data()
main()