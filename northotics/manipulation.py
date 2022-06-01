"""
Functions that manipulate data
"""
import datetime
from datetime import timezone
from northotics.system import clear_screen
from northotics.store import SHEET, order_data, export_data, user_data
from northotics.validation import (
    verify_user_f_name, verify_change_feature_of_order,
    verify_user_l_name, verify_user_email
    )
from northotics.inputs import get_size_data, get_height_data, get_width_data
from northotics.submit import submit_row_data
from northotics.__init__ import start


def flatten_nested_list(input_list):
    """
    Flattens a nested list into a list
    """
    flattened_list = []
    for value in input_list:
        if isinstance(value, list):
            flattened_list.extend(flatten_nested_list(value))
        else:
            flattened_list.append(value)
    return flattened_list


def combine_data_for_export():
    """
    Loops through user_data then order_data to create single export_data
    list in preparation to update_order_worksheet
    """
    clear_screen()
    export_data.clear()
    for value in user_data:
        export_data.append(value)
    for value in order_data:
        export_data.append(value)
    export_data.pop()
    return export_data


def generate_utc_time():
    """
    Creates Univesal Coordinated time (UTC) version of date and time
    in iso format
    """
    iso_utc_now = datetime.datetime.now(timezone.utc).isoformat()
    return iso_utc_now


def slice_last_order_no():
    """
    Steps order number back by one value to account for the heading information
    within gsheets document.
    """
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = last_entry[0]
    slice_last_digit = slice(6)
    reset_no = int(last_entry_int[slice_last_digit])
    reset_no_to_ten_thousand = reset_no * 10000
    return reset_no_to_ten_thousand


def generate_order_no():
    """
    Generates an order number with todays date + increment from previoius
    order entry in worksheet
    """
    order_no = SHEET.worksheet('orders').get_values('G:G')
    last_index = len(order_no) - 1
    last_entry = order_no[last_index]
    last_entry_int = int(last_entry[0])
    now = datetime.datetime.now(timezone.utc)
    order_date = now.strftime('%y%m%d')
    new_order_no = (
        int(order_date)*10000) + (last_entry_int - slice_last_order_no() + 1)
    order_data[3] = new_order_no
    return new_order_no


def update_date_ordered():
    """
    Updates the order_date filed within order_data list
    """
    time_zone = generate_utc_time()
    order_data[4] = time_zone
    order_data[5] = 'NEW ORDER'


def generate_row_no():
    """
    Retrieves current row data length and extends it by 1 value
    """
    row_data = SHEET.worksheet('orders').get_values('K:K')
    new_row_no = len(row_data) + 1
    export_data.append(new_row_no)


def delete_blank_space(string):
    """
    deletes all spaces in string inputs
    """
    return string.replace(' ', '')


def change_feature_of_order():
    """
    Generates a list to choose which feature of an exsisting order to change
    """
    feature_selection = input('Your Selection : ')
    if feature_selection == '1':
        clear_screen()
        f_name = input('New First Name details: ')
        clear_screen()
        verify_user_f_name(f_name)
        f_name = user_data[0]
        verify_change_feature_of_order()
    elif feature_selection == '2':
        clear_screen()
        l_name = input('New Last Name details: ')
        clear_screen()
        verify_user_l_name(l_name)
        l_name = user_data[1]
        verify_change_feature_of_order()
    elif feature_selection == '3':
        clear_screen()
        user_email = input('New Email details: ')
        verify_user_email(user_email)
        user_email = user_data[2]
        verify_change_feature_of_order()
    elif feature_selection == '4':
        clear_screen()
        get_size_data()
        clear_screen()
        verify_change_feature_of_order()
    elif feature_selection == '5':
        clear_screen()
        get_height_data()
        clear_screen()
        verify_change_feature_of_order()
    elif feature_selection == '6':
        clear_screen()
        get_width_data()
        clear_screen()
        verify_change_feature_of_order()
    elif feature_selection == '7':
        update_date_ordered()
        combine_data_for_export()
        submit_row_data()
    elif feature_selection == '8':
        combine_data_for_export()
        start()
    else:
        print(
            f'The number you have provided "{feature_selection}" is not part'
            'of this selection.'
            )
        print('Please select again\n')
        verify_change_feature_of_order()


def update_to_pending_status():
    """
    Updates status to pending when user saves order
    """
    time_zone = generate_utc_time()
    export_data[9] = time_zone
    export_data[8] = 'PENDING'
    export_data[7] = ''
    new_order_no = generate_order_no()
    export_data[6] = new_order_no
    generate_row_no()
    order_worksheet = SHEET.worksheet('orders')
    order_worksheet.append_row(export_data)
    clear_screen()
    print('Data successfully saved as PENDING.')
    print(
        f'\nPlease carefully record order no : {export_data[6]}'
        '\nYou will need it to recall this item into the future.'
        )
