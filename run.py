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
    
    f_name = input('Your First Name: ')
    l_name = input('Your Last Name: ')
    user_email = input('Your Email: ')
    
    print(f'\nThanks {f_name}. Your user details are as follows:')
    print('------------')
    print(f'Full Name: {f_name.capitalize()} {l_name.capitalize()}\nEmail: {user_email.lower()}')
    print('------------\n')
    yes_no()
    validate_data(f'{f_name.capitalize()}, {l_name.capitalize()}, {user_email.lower()}')

def validate_data(values):
    """
    Inside the try, converts all get_size_data inputs into floats.
    Converts all email string values into lowercase with .lower()
    Converts all email string values into first letter capital with .capitalize()
    Raises ValueError if strings cannot be converted into float or
    if height == low or mid or high string values or 
    if width == narrow or standard or wide.
    """
    print(f'The data you provided converted into a list of strings is:\n{values}')



def yes_no():
    correct = input('Is this information correct? y/n: ').lower()
    if correct.startswith('y'):
        print(f'Thanks *** , updating worksheet and proceeding to order_data\n')
    else:
        get_user_data() # etc.

def main():
    """
    Run all program functions
    """
    user = get_user_data()
main()

# validate_data(values)