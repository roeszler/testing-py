"""
Functions used to verify data
"""
import re
from northotics.store import SHEET, REGEX, order_data, user_data
from northotics.manipulation import (
    delete_blank_space, flatten_nested_list, change_feature_of_order,
    clear_screen
    )
from northotics.display import email_print_update_startover


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
        f_name = delete_blank_space(input('Your First Name : ').capitalize())
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
        l_name = delete_blank_space(input('Your Last Name : ').capitalize())
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
        user_email = delete_blank_space(input('Your Email: ').lower())
        verify_user_email(user_email)
        user_data[2] = user_email
