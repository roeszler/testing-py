"""
Functions to submit data to the database
"""
import os
from northotics.display import (
    update_status, display_order
    )
from northotics.utilities import (
    update_date_ordered, combine_data_for_export,
    verify_change_feature_of_order
    )
from northotics.inputs import (
    get_order_data, get_user_data, cancel_confirm
    )
from northotics.manipulation import (
    generate_row_no, generate_order_no, update_to_pending_status
    )
from northotics.store import SHEET, export_data, order_data, user_data
from northotics.landing import start, summary_order_data, select_option
from northotics.dates import generate_utc_time


def submit_order():
    """
    User choice to deny or confirm order submission.
    Confirn compiles list from user_data and oder_data then
    exports it to update_sales-worksheet function
    """
    submit = input('\nWould you like to submit this order? y/n: ').lower()
    if submit.startswith('n'):
        save_order()
    else:
        clear_screen()
        generate_order_no()
        update_date_ordered()
        combine_data_for_export()
        generate_row_no()
        update_order_worksheet(export_data)

        recent_order_no = export_data[6]
        order_data[7] = export_data[10]
        submitted_time = export_data[7]

        print('Order Successfully Submitted!!')
        print(f'\nYour order number is: {recent_order_no}')
        print(f'Submitted on: {submitted_time}')
        summary_order_data()
        email_print_update_startover()


def save_order():
    """
    User descision to save order as pending within gsheets or
    clear all local data and return to start screen
    """
    save = input('\nWould you like to save this order? y/n: ').lower()
    if save.startswith('n'):
        order_data.clear()
        export_data.clear()
        clear_screen()
        start()
    else:
        export_data[7] = ''
        update_to_pending_status()
        email_print_update_startover()


def yes_no_user():
    """
    Prompt for user to confirm or input correct user_data
    """
    summary_user_data()
    correct = input('\nIs this information correct? y/n: ').lower()
    if correct.startswith('y'):
        clear_screen()
        f_name = user_data[0]
        print(
            f'Thanks {f_name}. Now lets customise your N3 Othoses order...'
            )
        get_order_data()
        generate_order_no()
        combine_data_for_export()
        summary_order_data()
        submit_order()
    else:
        clear_screen()
        get_user_data()


def update_order_worksheet(data):
    """
    Update sales google worksheet, add new row with the list data provided
    """
    print('Contacting the mothership...')
    order_worksheet = SHEET.worksheet('orders')
    order_worksheet.append_row(data)
    print('Information received...')


def update_to_canceled_status():
    """
    Updates status to pending when user saves order
    """
    row = order_data[7]
    order_worksheet = SHEET.worksheet('orders')
    print(f'Current order status is: {export_data[8]}')
    if export_data[8] == 'PENDING' or export_data[8] == 'NEW ORDER' or \
            export_data[8] == 'UPDATED ORDER' or export_data[8] == 'CREATED' \
            or export_data[8] == 'ACCEPTED' or export_data[8] == 'DESIGNED':
        print('Order is modifiable.\n')
        cancel_confirm()
        iso_format_timezone = generate_utc_time()
        export_data[9] = iso_format_timezone
        export_data[8] = 'CANCELED'
        order_worksheet.update(f'I{row}', f'{export_data[8]}')
        order_worksheet.update(f'J{row}', f'{export_data[9]}')
        print('\nOrder successfully CANCELED.')
        print(
            f"An email with it's credit note details will be sent to"
            f' {export_data[2]}'
            )
        print(
            f'\nPlease carefully record the order no. {export_data[6]}'
            '\nYou will need it to refer to this action into the future.'
            )
        email_print_update_startover()
    else:
        print(
            'Unfortunatley as a custom made product, this order is already at'
            f' the {export_data[8]} stage.'
            )
        print(
            '\nFrom this point manufacturing has already commenced. As it '
            '\nis made to your specifications, the window to alter or cancel '
            '\nthe order has passed.'
            )
        print(
            '\nFor further clarificaiton of made-to-order products purchased'
            ' online,'
            '\nspecifically section 13(1)(c) of the UK Distance Selling'
            ' Regulations, please visit: '
            'https://www.legislation.gov.uk/uksi/2000/2334/contents/made. '
            '\nAlternately, contact info@northotics.com refering order '
            'number :'
            f' {export_data[6]}.'
            '\nYour purchasing rights have not been affected.\n'
            )
        email_print_update_startover()


def submit_row_data():
    """
    Replaces the exsisting row data in the worksheet with updated data and
    records the date of the order update
    """
    row = order_data[7]
    order_worksheet = SHEET.worksheet('orders')
    print(f'Accessing your order on row number : {row}')
    iso_format_timezone = generate_utc_time()
    export_data[9] = iso_format_timezone
    export_data[8] = 'UPDATED ORDER'
    order_worksheet.update(f'A{row}', export_data[0])
    order_worksheet.update(f'B{row}', export_data[1])
    order_worksheet.update(f'C{row}', export_data[2])
    order_worksheet.update(f'D{row}', float(export_data[3]))
    order_worksheet.update(f'E{row}', export_data[4])
    order_worksheet.update(f'F{row}', export_data[5])
    order_worksheet.update(f'G{row}', int(export_data[6]))
    order_worksheet.update(f'H{row}', export_data[7])
    order_worksheet.update(f'I{row}', export_data[8])
    order_worksheet.update(f'J{row}', export_data[9])
    print(f'\nOrder No. {export_data[6]} successfully updated!')
    print('Thanks for using the N(3)Orthotics order submission app.\n')
    update_status()


def clear_screen():
    """
    Checks if Operating System is Mac and Linux or Windows and
    clears the screen
    """
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


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
