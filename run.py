import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')

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

    f_name = input('Your First Name: ')
    l_name = input('Your Last Name: ')
    user_email = input('Your Email: ')

    print(f'\nThanks {f_name}. Your user details are as follows: \n')
    print(f'Full name: {f_name} {l_name}\nEmail: {user_email}\n')

def main():
    """
    Run all program functions
    """
    user = get_user_data()
main()