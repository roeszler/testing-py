# Modules
import gspread
from google.oauth2.service_account import Credentials
import re # regular extensions import for checking syntax of email
import os
import datetime
from datetime import timezone
import pytz # regional date time for order_no and order_date

import smtplib, ssl
import getpass


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
UTC = pytz.timezone('Etc/GMT+0')


user_data = ['f_name', 'l_name', 'user_email']
order_data = ['size_eu', 'height', 'width', 'order_no', '', 'order_status', '']
update_order = ['order_status', 'order_update']
export_data = []
search_res_row = 0



# Testing email details SSL
def test_email():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "testingn3d@gmail.com"  # Enter your address
    receiver_email = user_data[2] # retrieves the receiver address
    print(receiver_email)
    password = input("Type your password and press enter: ")
    message = """\
    Subject: Hi there

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# # Testing email details TLS
# def test_email():
#     port = 587  # For starttls
#     smtp_server = "smtp.gmail.com"
#     sender_email = "testingn3d@gmail.com"
#     receiver_email = user_data[2] # retrieves the receiver address
#     password = input("Type the testing password provided by developer and press enter: ")
#     message = """\
#     Subject: Hi there

#     This message is sent from Python."""

#     context = ssl.create_default_context()
#     with smtplib.SMTP(smtp_server, port) as server:
#         # server.ehlo()  # Can be omitted
#         server.starttls(context=context)
#         # server.ehlo()  # Can be omitted
#         server.login(sender_email, password)
#         server.sendmail(sender_email, receiver_email, message)

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
    print('Select 2. : Retrieve an exsisting N3D order')
    print('Select 3. : Exit Program\n')
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
            display_order()
            # get_user_data()
            # instruct_user_data()
            # get_user_data()
        elif i == '3':
            quit()
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
    Inside the try, checks all user input syntax.
    Raises ValueError if strings cannot be converted
    and prompts to replace data in index [0] of the 
    user_data list = f_name
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
    Inside the try, checks all user input syntax.
    Raises ValueError if strings cannot be converted
    and prompts to replace data in index [1] of the 
    user_data list = l_name
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
    Inside the try, checks all user email input syntax.
    Raises ValueError if strings cannot be converted
    and prompts to replace data in index [2] of the 
    user_data list = user_email
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
    Converts to a float() between EU shoe size between EU19 and EU50 only.
    Inside the try, converts all string values into floating points and
    raises ValueError if not a number.
    """
    while True:
        try:
            size_eu = float(remove(input('\nWhat EU Shoe Size would you like to match with?\n(sized in 0.5 increments between 19 and 50): ')))
            size_divisble = size_eu % 0.5

            if size_eu >= 19 and size_eu <= 50:
                if size_divisble != 0:
                    print(f'\nIncorrect information provided for european shoe sizing: {size_eu}\n')
                    get_size_data()
                else:          
                    order_data[0] = size_eu
                    return size_eu
            else:
                print(f'\nUnfortunatley {size_eu} is not within the european shoe size range we do.')
                get_size_data()

        except ValueError as e:
            print(f'Invalid data : {e}, please try again.\n')
            # return False
            continue
        return True

def get_height_data():
    """
    Height user input converted into ['Low', 'Med', 'High'] for order_data
    Only strings starting with l, m or h accepted. Not case sensitive.
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
    """
    Loops through user_data then export_data to create single export_data
    list in preparation to update_order_worksheet
    """
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
    Generates an order number with todays date + increment from previoius 
    oder entry in worksheet
    """
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = int(last_entry[0])
    now = datetime.datetime.now(timezone.utc)
    order_date = now.strftime('%y%m%d')
    new_order_no = (int(order_date)*10000) + (last_entry_int - slice_last_order_no() + 1)
    order_data[3] = new_order_no
    print(new_order_no)
    return new_order_no


# def generate_date_time():
#     """
#     Creates UTC (Coordinated Universal Time) version of date and time
#     """
#     now = datetime.datetime.now()
#     order_date = now.strftime('%c')
#     n = order_date.title()
#     print(f'{n}')

def generate_UTC_time():
    """
    Creates Central European Standard Time (CEST) version of date and time
    in iso 
    """
    utc_now = datetime.datetime.now(timezone.utc)
    # CEST = pytz.timezone('Europe/Stockholm')
    # UTC = pytz.timezone('Etc/GMT+0')
    # print('{} CEST'.format(utc_now.astimezone(CEST).isoformat()))
    # print('{} UTC'.format(utc_now.astimezone().isoformat()))
    # print('the supported timezones by the pytz module:', pytz.all_timezones, '\n')
    # n = '{}'.format(utc_now.astimezone(CEST).isoformat())
    n = '{}'.format(utc_now.astimezone(UTC).isoformat())
    # print(export_data)
    return n

def update_date_ordered():
    """
    Updates the order_date filed within order_data list
    """
    n = generate_UTC_time()
    order_data[4] = n
    order_data[5] = 'NEW ORDER'
    print(order_data)


def update_to_pending_status():
    """
    Updates status to pending when user saves order
    """
    n = generate_UTC_time()
    export_data[9] = n
    export_data[8] = 'PENDING'
    order_worksheet = SHEET.worksheet('orders') # accessing our sales_worksheet from our google sheet
    order_worksheet.append_row(export_data) # adds a new row in the google worksheet selected
    # print(export_data)
    clear_screen()
    print(f'Data successfully saved as PENDING.')
    print(f"An email with it's details to {export_data[2]}")
    print(f'\nPlease carefully record order no.{export_data[6]}\nYou will need it to recall thi5s item into the future.')

def input_order_no():
    """
    Checks the user input order number is only numerical and correct length
    """
    print('Please enter your order number below.')
    print('This information should be in a valid syntax, with no spaces. For example:\n')
    print('Example order_no format: 2205190001\n')
    while True:
        try:
            order_no = int(remove(input('You Order Number: ')))
            order_no_string = str(order_no)
            if len(order_no_string) != 10:
                raise ValueError(
                f'`Our order numbers require 10 digits.\nUnfortunatley {order_no} has {len(order_no_string)} digits.'
                )
        except ValueError as e:
            print(f'Invalid data : {e}\nPlease check your records and try again below;\n')
            # return False
            continue
        # print(len(order_no_string))
        # print(order_no)
        # return True
        return order_no

# Sourced from https://www.pythonpool.com/flatten-list-python/
def flatten_nested_list(input_list):
    """
    Flattens a nested list into a list 
    """
    flattened_list = []
    for i in input_list:
        if type(i) == list:
            flattened_list.extend(flatten_nested_list(i))
        else:
            flattened_list.append(i)
    return flattened_list


def retrieve_order():
    """
    Searches worksheet coloum order_no for a match to user input and
    returns row information to local user_data, oder_data and export_data lists
    """
    search_input = str(input_order_no())
    order_nos_import = SHEET.worksheet('orders').get_values('G:G')
    order_nos = flatten_nested_list(order_nos_import)
   
    res = [i for i in range(len(order_nos)) if order_nos[i] == search_input]
    if res == []:
        print(f'Order number {search_input} not found?!\n')
        retrieve_order()
    else:
        for i in range(len(order_nos)):
            if search_input == order_nos[i]:
                search_res_row = i+1
                print(f'\nOrder found in database row no.{search_res_row} :')
                return search_res_row


def display_order():
    """
    
    """
    row = int(retrieve_order())
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:L{row}')
    flat_order = flatten_nested_list(order_row)
    user_data[0:3] = flat_order[0:3]
    order_data[0:6] = flat_order[3:9]

    # f_name = user_data[0]
    # l_name = user_data[1]
    # user_email = user_data[2]
    
    print('\nYour order details are as follows:\n')
    print(f'Full Name : {user_data[0]} {flat_order[1]}\nEmail : {flat_order[2]}')
    print(f'Shoe Size : EU {flat_order[3]}\nArch Height : {flat_order[4]}\nInsole Width : {flat_order[5]}')
    print(f'Order No. : {flat_order[6]}\nDate Ordered : {flat_order[7]}\nCurrent Status : {flat_order[8]}\n')

    # print('What would you like to do with this order :')
    update_status()


    # print(user_data)
    # print(order_data)

def update_status():
    """
    
    """
    order_no = order_data[3]
    f_name = user_data[0]

    print(f'Hi {f_name}. What would you like to do with order no.{order_no} ?')
    print('\nSelect 1. : Re-Print this order again (no changes)')
    print('Select 2. : Change the features')
    print('Select 3. : Start a new order')
    print('Select 4. : Cancel order')
    print('Select 5. : Search different order')
    print('Select 6. : Take me home\n')

    startover = input('Your Selection: ')
    for i in startover:
        if i == '1':
            clear_screen()
            print(f'Re-printing order number : {order_no}...\n')
            submit_order()
            # test_email()
            # email_print_update_startover()
        elif i == '2':
            clear_screen()
            print(f'Change features of order : {order_no}...\n')
            # email_print_update_startover()
        elif i == '3':
            clear_screen()
            print('Starting a new N3D insole order...')
            yes_no_user()
            # get_order_data()
        elif i == '4':
            clear_screen()
            print(f'Cancelling order {order_no}...\n')
        elif i == '5':
            clear_screen()
            display_order()
            # order_no = input(f'Your order no. : {order_no}')
        elif i == '6':
            clear_screen()
            main()
        else:
            print(f'The number you have provided "{startover}" is not available.\nPlease select again\n')
            email_print_update_startover()


    n = generate_UTC_time()
    update_order[1] = n
    print(update_order)
    print(export_data)


def submit_order():
    """
    User choice to deny or confirm order submission. 
    Confirn compiles list from user_data and oder_data then 
    exports it to update_sales-worksheet function
    """
    submit = input('Would you like to submit this order? y/n: ').lower()
    if submit.startswith('n'):
        save_order()
    else:
        clear_screen()
        generate_order_no()
        update_date_ordered()
        combine_data_for_export()
        update_order_worksheet(export_data)

        user_email = export_data[2]
        recent_order_no = export_data[6]
        submitted_time = export_data[7]

        print(f'\nOrder Successfully Submitted!!\nYou will shortly receive an email instructions to:\n{user_email} with the details to arrange secure payment.')
        print(f'\nYour order number is: {recent_order_no}')
        print(f'Submitted on: {submitted_time}')
        summary_order_data()
        email_print_update_startover()



def update_order_worksheet(data):
    """
    Update sales google worksheet, add new row with the list data provided
    """
    print('Contacting the mothership...')
    order_worksheet = SHEET.worksheet('orders') # accessing our sales_worksheet from our google sheet
    order_worksheet.append_row(data) # adds a new row in the google worksheet selected
    print('Information received...')



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
        # update_date_ordered()
        update_to_pending_status()
        # combine_data_for_export()
        # print(export_data)
        # summary_order_data()
        # display_order()
        email_print_update_startover()


# def export_to_printer():
#     os.startfile("TestFile.txt", "print")
#     import platform
#     print(platform.platform())







def email_print_update_startover():
    print('\nWhat would you like to do next?')
    print('\nSelect 1. : Email this order')
    print('Select 2. : Print this order')
    print('Select 3. : Start a new N3D insole order')
    print('Select 4. : Retrieve an exsisting N3D order')
    print('Select 5. : Take Me Home')
    print('Select 6. : Exit the Program\n')

    startover = input('Your Selection: ')
    order_no = order_data[3]
    user_email = user_data[2]
    for i in startover:
        if i == '1':
            clear_screen()
            print(f'Emailing order number : {order_no} to {user_email}...\n')
            test_email()
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
            display_order()
        elif i == '5':
            print('Exiting this n3orthotics session...\n')
            clear_screen()
            start()
            select_option()
        elif i == '6':
            exit()
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
# generate_UTC_time()
# update_date_ordered()
# instruct_user_data()
# email_print_update_startover()
# slice_last_order_no()
# test_email()
# export_to_printer()
# update_status()
# retrieve_order() 
# display_order()
# input_order_no()
# update_to_pending_status()