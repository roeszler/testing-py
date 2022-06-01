"""
Collection of utility functions to manipulate data
"""
import re
import os
from northotics.store import SHEET, REGEX
# from northotics.system import clear_screen
from northotics.store import user_data, export_data, order_data
# from northotics.inputs import get_width_data
from northotics.dates import update_date_ordered
from northotics.submit import submit_row_data
from northotics.display import email_print_update_startover


# def delete_blank_space(string):
#     """
#     deletes all spaces in string inputs
#     """
#     return string.replace(' ', '')


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
        # start()
    else:
        print(
            f'The number you have provided "{feature_selection}" is not part'
            'of this selection.'
            )
        print('Please select again\n')
        verify_change_feature_of_order()


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


def verify_user_f_name(values):
    """
    Inside the try, checks all user input syntax.
    Raises ValueError if strings cannot be converted and prompts to
    replace data in index [0] of the user_data list = f_name
    """
    try:
        if values.isalpha():
            user_data[0] = values.capitalize()
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem'
                f'\nto be in a regular format'
            )
    except ValueError as error:
        print(
            f'\nInvalid data: {error}. Please check the entry and try again.\n'
            )
        f_name = input('Your First Name : ').capitalize().replace(' ', '')
        verify_user_f_name(f_name)
        user_data[0] = f_name


def verify_user_l_name(values):
    """
    Inside the try, checks all user input syntax.
    Raises ValueError if strings cannot be converted and prompts to
    replace data in index [1] of the user_data list = l_name
    """
    try:
        if values.isalpha():
            user_data[1] = values.capitalize()
        else:
            raise ValueError(
                f'The name you have provided "{values}" does not seem'
                f'to be in a regular format'
            )
    except ValueError as error:
        print(
            f'\nInvalid data: {error}. Please check the entry and try again.\n'
            )
        l_name = input('Your Last Name : ').capitalize().replace(' ', '')
        verify_user_l_name(l_name)
        user_data[1] = l_name


def verify_user_email(values):
    """
    Inside the try, checks all user email input syntax.
    Raises ValueError if strings cannot be converted and prompts to
    replace data in index [2] of the user_data list = user_email
    """
    try:
        if re.fullmatch(REGEX, values):
            print('Email is valid...')
            user_data[2] = values.lower()
            clear_screen()
        else:
            raise ValueError(
                f'The email you have provided "{values}" does not seem'
                'to be in a regular format'
            )
    except ValueError as error:
        print(
            f'\nInvalid data: {error}. Please check the entry and try again.\n'
            )
        user_email = input('Your Email: ').lower().replace(' ', '')
        verify_user_email(user_email)
        user_data[2] = user_email


def verify_change_feature_of_order():
    """
    Valudates order is prior to 'SUBMITTED TO PRINT' stage for
    change_feature_of_order function
    """
    row = order_data[7]
    order_row = SHEET.worksheet('orders').get_values(f'A{row}:K{row}')
    flat_order = flatten_nested_list(order_row)
    print(f'Current order status is: {flat_order[8]}')
    if flat_order[8] == 'PENDING' or flat_order[8] == 'NEW ORDER' or \
            flat_order[8] == 'UPDATED ORDER' or flat_order[8] == 'CREATED' or \
            flat_order[8] == 'ACCEPTED' or flat_order[8] == 'DESIGNED':
        print('Order is modifiable.')
        print('\nYour order details are as follows:\n')
        print(
            f'Order No. : {flat_order[6]}'
            f'\nDate Ordered : {flat_order[7]}'
            f'\nDatabase Row entry : {flat_order[10]}'
            f'\nCurrent Status : {flat_order[8]}'
            )
        print('\nDetails you can edit:\n')
        print(
            f'1. First Name : {user_data[0]}'
            f'\n2. Surname : {user_data[1]}'
            f'\n3. Email : {user_data[2]}'
            )
        print(
            f'4. Shoe Size : EU {order_data[0]}'
            f'\n5. Arch Height : {order_data[1]}'
            f'\n6. Insole Width : {order_data[2]}\n'
            )
        print(
            '7. Submit the above details'
            '\n8. Take me Home\n'
            )
        change_feature_of_order()
    else:
        print(
            f'\nAt the {flat_order[8]} stage, this order is beyond the point'
            'in production\nwhere modifications can occur.'
            )
        email_print_update_startover()


def get_size_data():
    """
    Converts to a float() between EU shoe size between EU19 and EU50 only.
    Inside the try, converts all string values into floating points and
    raises ValueError if not a number.
    """
    while True:
        try:
            size_eu = float(input(
                '\nWhat EU Shoe Size would you like to fit into?'
                '\n(sized in 0.5 increments between 19 and 50): '
                ).replace(' ', ''))
            size_divisble = size_eu % 0.5
            if size_eu >= 19 and size_eu <= 50:
                if size_divisble != 0:
                    print(
                        '\nIncorrect information provided for european'
                        f'shoe sizing: {size_eu}'
                        )
                    # get_size_data()
                    continue
                else:
                    order_data[0] = size_eu
                    return size_eu
            else:
                print(
                    f'\nUnfortunatley {size_eu} is not within the european'
                    'shoe size range we do.'
                    )
                get_size_data()
        except ValueError as error:
            print(f'Invalid data : {error}, please try again.\n')
            continue


def get_height_data():
    """
    Height user input converted into ['Low', 'Med', 'High'] for order_data
    Only strings starting with l, m or h accepted. Not case sensitive.
    """
    height = input(
        '\nWhat level of support under the inside arch would you like?'
        '\n(L: Low Support / M: Medium Support / H: High Support): '
        ).lower().replace(' ', '')
    if height.startswith('l'):
        order_data[1] = 'Low'
    elif height.startswith('m'):
        order_data[1] = 'Medium'
    elif height.startswith('h'):
        order_data[1] = 'High'
    else:
        print(f'\nIncorrect information provided for arch height: {height}')
        get_height_data()


def get_width_data():
    """
    Width user input converted into ['Narrow', 'Standard', 'Wide'] for
    order_data
    """
    width = input(
        '\nWidth of insole to fit the foot &/or shoe'
        '\n(N: Narrow / S: Standard / W: Wide): '
        ).lower().replace(' ', '')
    if width.startswith('n'):
        order_data[2] = 'Narrow'
    elif width.startswith('s'):
        order_data[2] = 'Standard'
    elif width.startswith('w'):
        order_data[2] = 'Wide'
    else:
        print(f'\nIncorrect information provided for insole width: {width}')
        get_width_data()


def clear_screen():
    """
    Checks if Operating System is Mac and Linux or Windows and
    clears the screen
    """
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
