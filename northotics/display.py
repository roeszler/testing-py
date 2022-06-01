"""
Imports modules used to interact with various operating systems
"""
from northotics.store import SHEET, user_data, order_data, update_order
from northotics.retrieve import retrieve_order
from northotics.manipulation import (
    flatten_nested_list, combine_data_for_export, generate_utc_time
    )
from northotics.system import clear_screen
from northotics.submit import (
    submit_order, yes_no_user, update_to_canceled_status
    )
from northotics.validation import verify_change_feature_of_order
from northotics.__init__ import start, select_option


def display_order():
    """
    Gets orders by row from worksheet
    Converts specific string values back into integers and
    Displays entire order as a list
    """
    row = int(retrieve_order())
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')
    flat_order = flatten_nested_list(order_row)
    size_eu = flat_order[3]
    flat_order[3] = float(size_eu)
    order_no = flat_order[6]
    flat_order[6] = int(order_no)
    user_data[0:3] = flat_order[0:3]
    order_data[0:6] = flat_order[3:9]
    order_data[7] = int(row)
    combine_data_for_export()
    print('Your order details are as follows:\n')
    print(
        f'Full Name : {user_data[0]} {flat_order[1]}\nEmail : {flat_order[2]}'
        )
    print(
        f'Shoe Size : EU {flat_order[3]}'
        f'\nArch Height : {flat_order[4]}'
        f'\nInsole Width : {flat_order[5]}'
        )
    print(
        f'Order No. : {flat_order[6]}'
        f'\nDate Ordered : {flat_order[7]}'
        f'\nCurrent Status : {flat_order[8]}')
    print(f'Row : {flat_order[10]}\n')
    update_status()


def update_status():
    """
    Generates a list of user options to append details of an exsisting order ot
    create new order details and/or navigate through the system
    """
    order_no = order_data[3]
    print(f'What would you like to do with order no. {order_no} ?')
    print('\nSelect 1. : Re-Print this order again (no changes)')
    print('Select 2. : Change the features')
    print('Select 3. : Place a new N3D insole order')
    print('Select 4. : Cancel order')
    print('Select 5. : Search different order')
    print('Select 6. : Take me home\n')

    startover = input('Your Selection: ')
    for i in startover:
        if i == '1':
            clear_screen()
            print(f'Re-printing order number : {order_no}...\n')
            submit_order()
        elif i == '2':
            clear_screen()
            print(f'Order No. {order_no}\n')
            verify_change_feature_of_order()
        elif i == '3':
            clear_screen()
            print('Starting a new N3D insole order...')
            yes_no_user()
        elif i == '4':
            clear_screen()
            print(f'Checking the current status of order no. {order_no} ...')
            update_to_canceled_status()
        elif i == '5':
            clear_screen()
            display_order()
        elif i == '6':
            clear_screen()
            start()
        else:
            print(
                f'The number you have provided "{startover}" is not available.'
            )
            print('Please select again\n')
            email_print_update_startover()

    iso_format_timezone = generate_utc_time()
    update_order[1] = iso_format_timezone


def email_print_update_startover():
    """
    User descision tree to navigate following a successful submission,
    fetaure change, save or change of status
    """
    print('\nWhat would you like to do next?')
    print('Select 1. : Change the features of this Order')
    print('Select 2. : Place a new N3D insole order')
    print('Select 3. : Retrieve an exsisting N(3) order')
    print('Select 4. : Take Me Home')
    print('Select 5. : Exit the N(3)Orthotics order portal\n')
    startover = input('Your Selection: ')
    order_no = order_data[3]
    for i in startover:
        if i == '1':
            clear_screen()
            print(f'Order No. {order_no}\n')
            verify_change_feature_of_order()
        elif i == '2':
            clear_screen()
            print('Starting a new N3D insole order...')
            yes_no_user()
        elif i == '3':
            clear_screen()
            print('Retrieve an Exsisting Order...\n')
            display_order()
        elif i == '4':
            print('Taking you to home page...\n')
            clear_screen()
            start()
            select_option()
        elif i == '5':
            print('Exiting this n3orthotics session...\n')
            clear_screen()
            exit()
        else:
            print(
                f'The number you have provided "{startover}" is not available.'
                '\nPlease select again\n'
                )
            email_print_update_startover()


def summary_user_data():
    """
    Produces a readable summary of the current user_data list
    """
    print(f'Full Name : {user_data[0]} {user_data[1]}\nEmail : {user_data[2]}')


def summary_order_data():
    """
    Produces a summary of the current order data stored locally
    """
    size_eu = order_data[0]
    height = order_data[1]
    width = order_data[2]

    print('\nYour order details are as follows:')
    summary_user_data()
    print(f'Shoe Size : EU {size_eu}')
    print(f'Arch Height : {height}')
    print(f'Insole Width : {width}')


def instruct_user_data():
    """
    Insruct User on format of first name, last name and email.
    """
    clear_screen()
    print('Place a N(3)ORTHOTICS.com N3D printed insole order:\n')
    print('Where prompted below, please enter your name and email.')
    print('This information should be in a valid syntax, with no spaces.')
    print('For example:\n')
    print('First Name: Rob\nLast Name: Bertoe')
    print('Email: rubbertoes@yourdomain.com\n')
