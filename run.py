import gspread
from google.oauth2.service_account import Credentials
import re # regular extensions import for checking syntax of email
import os
import datetime

SCOPE = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')

REGEX_EMAIL = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

user_data = ['f_name', 'l_name', 'user_email']
order_data = ['size_eu', 'height', 'width', 'order_no']
export_data = []
# order_date = ''

# orders = SHEET.worksheet('orders')
# data = orders.get_all_values()
# print(data)

def start():
    """
    Start screen prompting user to:
    1. Create a new order, or
    2. Retrieve an exsisting order with order number
    """
    print('Welcome to N(3)ORTHOTICS.\n')
    print('Use this app to directly access made-to-order N3D Printed Insoles')
    print('Please visit northotics.com/home for more information\n')
    
    print('Select 1. : Place a new N3D insole order')
    print('Select 2. : Retrieve an exsisting N3D order\n')
    # select_option()



def select_option():
    """
    Initial user choice to place a new or retieve an exsisting N3D order
    """
    correct = input('Your Selection: ')
    for i in correct:
        if i == '1':
            # print('Updating worksheet and proceeding to order_data...\n')
            # order_data.clear()
            # export_data.clear()
            return True
            # main()
        elif i == '2':
            print('Taking you to retrieve_order function...\n')
            # get_user_data()
            # instruct_user_data()
            # get_user_data()
        else:
            print(f'The number you have provided "{correct}" is not available.\nPlease select again\n')
            select_option()

def instruct_user_data():
    """
    Insruct User on format of first name, last name and email.
    """
    clear_screen()
    print('\nPlace a NORTHOTICS.com N3D Printed Insole order:\n')
    print('Where prompted below, please enter your name and email.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')
    print('First Name: Bob\nLast Name: Hunden')
    print('Email: bobby123@yourdomain.com\n')



def get_user_data():
    """
    User input of first name, last name and email to from a string
    with fist letter capitalized for names and all lowercase email 
    """
    f_name = remove(input('Your First Name: ').capitalize())
    user_data[0] = f_name
    # print(user_data)

    l_name = remove(input('Your Last Name: ').capitalize())
    user_data[1] = l_name
    # print(user_data)

    user_email = remove(input('Your Email: ').lower())
    user_data[2] = user_email
    # print(user_data)

    validate_user_f_name(f'{f_name}')
    validate_user_l_name(f'{l_name}')
    validate_user_email(f'{user_email}')



def summary_user_data():
    """
    Produces a readable summary of the current user_data list
    """
    f_name = user_data[0]
    l_name = user_data[1]
    user_email = user_data[2]

    # print(f'\nThanks {f_name}. Your user details are as follows:')
    # print('------------')
    print(f'\nFull Name : {f_name} {l_name}\nEmail : {user_email}')
    # print('------------')


def summary_order_data():
    f_name = user_data[0]
    size_eu = order_data[0]
    height = order_data[1]
    width = order_data[2]

    print('\nYour order details are as follows:')
    # print('------------')
    summary_user_data()
    print(f'Shoe Size : EU {size_eu}\nArch Height : {height}\nInsole Width : {width}\n')
    # print('------------')



def validate_user_f_name(values):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            # print('Name is valid...')
            return True
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}. Please check the entry and try again.\n')
        f_name = remove(input('Your First Name: ').capitalize())
        user_data[0] = f_name
        validate_user_f_name(f_name)
        # print(user_data)


def validate_user_l_name(values):
    """
    Inside the try, checks all user_email input syntax.
    Raises ValueError if strings cannot be converted
    """
    try:
        # if (re.fullmatch(REGEX_NAME, values)):
        if values.isalpha():
            print('Name is valid...')
            return True
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem\nto be in a regular format'
            )
    except ValueError as e:
        print(f'\nInvalid data: {e}. Please check the entry and try again.\n')
        l_name = remove(input('Your Last Name: ').capitalize())
        user_data[1] = l_name
        validate_user_l_name(l_name)
        # print(user_data)



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
    except ValueError as error:
        print(f'\nInvalid data: {error}. Please check the entry and try again.\n')
        user_email = remove(input('Your Email: ').lower())
        user_data[2] = user_email
        validate_user_email(user_email)
        # print(user_data)



def remove(string):
    """
    Removes all spaces in string inputs
    """
    return string.replace(' ', '')


def get_latest_row_entry():
    """
    Prints a list to the termainal of the row last updated
    between colums A to F in the worksheet
    """
    orders = SHEET.worksheet('orders').get_values('A:G')
    latest = orders[-1]
    print(latest)



def yes_no_user():
    """
    Prompt for user to confirm or input correct user_data
    """
    summary_user_data()
    correct = input('\nIs this information correct? y/n: ').lower()
    if correct.startswith('y'):
        clear_screen()
        f_name = user_data[0]
        print(f'\nThanks {f_name}. Now lets customise your N3 Othoses order...')
        get_order_data()
        generate_order_no()
        combine_data_for_export()
        summary_order_data()
        submit_order()
        # return True
    else:
        clear_screen()
        get_user_data()


def get_order_data():
    """
    Collection of User input used to order N3D Orthosis.
    """
    get_size_data()
    get_height_data()
    get_width_data()


def get_size_data():
    """
    EU shoe size between EU19 and EU50 converted to a float() for order_data
    """
    size_eu = float(remove(input('\nWhat EU Shoe Size would you like to match with?\n(sized in 0.5 increments between 19 and 50): ')))
    size_divisble = size_eu % 0.5
    if size_eu >= 19 and size_eu <= 50:
        if size_divisble != 0:
            print(f'\nIncorrect information provided for european shoe sizing: {size_eu}\n')
            get_size_data()
        else:
            # print(size_eu) 
            # print(type(size_eu))          
            order_data[0] = size_eu
            return size_eu
            # print(order_data)
            # generate_order_no()
            # submit_order()
            # get_height_data()
    else:
        print(f'\nUnfortunatley {size_eu} is not within the european shoe size range we do.\n')
        get_size_data()


def get_height_data():
    """
    Height user input converted into ['Low', 'Med', 'High'] for order_data
    """
    height = remove(input('\nWhat level of support under the inside arch would you like?\n(L: Low Support / M: Medium Support / H: High Support): ').lower())
    if height.startswith('l'):
        order_data[1] = 'Low'
    elif height.startswith('m'):
        order_data[1] = 'Medium'
    elif height.startswith('h'):
        order_data[1] = 'High'
    else:
        print(f'\nIncorrect information provided for arch height: {height}\n')
        get_height_data()
    # print(order_data)



def get_width_data():
    """
    Width user input converted into ['Narrow', 'Standard', 'Wide'] for order_data
    """
    width = remove(input('\nWidth of insole to fit the foot &/or shoe\n(N: Narrow / S: Standard / W: Wide): ').lower())
    if width.startswith('n'):
        order_data[2] = 'Narrow'
        # generate_order_no()
        # submit_order()
    elif width.startswith('s'):
        order_data[2] = 'Standard'
        # generate_order_no()
        # submit_order()
    elif width.startswith('w'):
        order_data[2] = 'Wide'
        # generate_order_no()
        # submit_order()
    else:
        print(f'\nIncorrect information provided for insole width: {width}\n')
        get_width_data()
    # print(order_data)


def combine_data_for_export():
    clear_screen()
    export_data.clear()
    for i in user_data:
        export_data.append(i)
    for i in order_data:
        export_data.append(i)
    # print(export_data)
    return export_data



def clear_screen():
    """
    Checks if Operating System is Mac and Linux or Windows and 
    clears the screen
    """
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def slice_last_order_no():
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = last_entry[0]
    x = slice(6)
    reset_no = int(last_entry_int[x])
    reset_no_10K = reset_no * 10000
    # print(type(reset_no))
    return reset_no_10K

def generate_order_no():
    """
    
    """
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = int(last_entry[0])
    now = datetime.datetime.now()
    order_date = now.strftime('%y%m%d')
    new_order_no = (int(order_date)*10000) + (last_entry_int - slice_last_order_no() + 1)
    
    order_data[3] = new_order_no
    # print(type(new_order_no))
    # print(new_order_no)
    # print(type(order_data[3]))
    # print(order_data[3])
    return new_order_no




# def generate_date_time():
#     now = datetime.datetime.now()
#     order_date = now.strftime('%y%m%d')
#     n = int(order_date)
#     # order_date[0] = order_date
#     print(f"Order Prefix: {n}")
#     print(type(n))
#     print(n)
#     order_date = n

    

def submit_order():
    """
    
    """
    submit = input('Would you like to submit this order? y/n: ').lower()
    if submit.startswith('n'):
        save_order()
    else:
        clear_screen()
        generate_order_no()
        combine_data_for_export()

        update_sales_worksheet(export_data)

        user_email = export_data[2]
        recent_order_no = export_data[6]
        print(f'\nOrder Successfully Submitted!!\nYou will shortly receive an email instructions to:\n {user_email} with the details to arrange secure payment')
        print(f'\nYour order number is: {recent_order_no}')
        summary_order_data()
        email_print_update_startover()



def update_sales_worksheet(data):
    """
    Update sales google worksheet, add new row with the list data provided
    """
    print('Contacting the mothership...')
    order_worksheet = SHEET.worksheet('orders') # accessing our sales_worksheet from our google sheet
    order_worksheet.append_row(data) # adds a new row in the google worksheet selected
    print('Success!! The Northo-bots have made contact!')



def save_order():
    """
    
    """
    save = input('\nWould you like to save this order? y/n: ').lower()
    if save.startswith('n'):
        # user_data.clear()
        order_data.clear()
        export_data.clear()
        clear_screen()
        main()
    else:
        combine_data_for_export()
        summary_order_data()
        email_print_update_startover()



def email_print_update_startover():
    print('\nWhat would you like to do next?')
    print('\nSelect 1. : Email this order')
    print('Select 2. : Print this order')
    print('Select 3. : Start a new N3D insole order')
    print('Select 4. : Retrieve an exsisting N3D order')
    print('Select 5. : Exit this n3orthotics session\n')

    startover = input('Your Selection: ')
    order_no = order_data[3]
    user_email = user_data[2]
    for i in startover:
        if i == '1':
            clear_screen()
            print(f'Emailing order number : {order_no} to {user_email}...\n')
            email_print_update_startover()
            # main()
        elif i == '2':
            clear_screen()
            print(f'Printing order number : {order_no}...\n')
            email_print_update_startover()
            # get_user_data()
            # instruct_user_data()
            # get_user_data()
        elif i == '3':
            clear_screen()
            print('Starting a new N3D insole order...')
            yes_no_user()
            # get_order_data()
        elif i == '4':
            clear_screen()
            print('Taking you to retrieve_order function...\n')
        elif i == '5':
            print('Exiting this n3orthotics session...\n')
            clear_screen()
            start()
            select_option()
        else:
            print(f'The number you have provided "{startover}" is not available.\nPlease select again\n')
            email_print_update_startover()

def main():
    """
    Run all program functions
    """
    clear_screen()
    start()
    select_option()
    instruct_user_data()
    get_user_data()
    summary_order_data()
    # generate_order_no()
    combine_data_for_export()
    submit_order()

main()

# get_latest_row_entry()
# validate_user_email(values='stuart@roeszler.com')
# validate_user_names(values='stuart Roes3ler')
# yes_no_user()
# start()
# select_option()
# summary_user_data()
# yes_no_user()
# get_order_data()
# get_size_data()
# summary_order_data()
# submit_order()
# save_order()
# combine_data_for_export()
# clear_screen()
# generate_order_no()
# generate_date_time()
# instruct_user_data()
# email_print_update_startover()
# slice_last_order_no()