"""
Module to collect all user input functions
"""
# from northotics.blanks import delete_blank_space
from northotics.store import user_data
from northotics.utilities import (
    get_size_data, get_height_data, get_width_data,
    verify_user_f_name, verify_user_l_name,
    verify_user_email
    )
from northotics.landing import start


def get_user_data():
    """
    User input of first name, last name and email to from a string
    with fist letter capitalized for names and all lowercase email
    """
    f_name = input('Your First Name: ').capitalize().replace(' ', '')
    verify_user_f_name(f'{f_name}')
    f_name = user_data[0]

    l_name = input('Your Last Name: ').capitalize().replace(' ', '')
    verify_user_l_name(f'{l_name}')
    l_name = user_data[1]

    user_email = input('Your Email: ').lower().replace(' ', '')
    verify_user_email(f'{user_email}')
    user_email = user_data[2]


# def get_size_data():
#     """
#     Converts to a float() between EU shoe size between EU19 and EU50 only.
#     Inside the try, converts all string values into floating points and
#     raises ValueError if not a number.
#     """
#     while True:
#         try:
#             size_eu = float(input(
#                 '\nWhat EU Shoe Size would you like to fit into?'
#                 '\n(sized in 0.5 increments between 19 and 50): '
#                 ).replace(' ', ''))
#             size_divisble = size_eu % 0.5
#             if size_eu >= 19 and size_eu <= 50:
#                 if size_divisble != 0:
#                     print(
#                         '\nIncorrect information provided for european'
#                         f'shoe sizing: {size_eu}'
#                         )
#                     # get_size_data()
#                     continue
#                 else:
#                     order_data[0] = size_eu
#                     return size_eu
#             else:
#                 print(
#                     f'\nUnfortunatley {size_eu} is not within the european'
#                     'shoe size range we do.'
#                     )
#                 get_size_data()
#         except ValueError as error:
#             print(f'Invalid data : {error}, please try again.\n')
#             continue


# def get_height_data():
#     """
#     Height user input converted into ['Low', 'Med', 'High'] for order_data
#     Only strings starting with l, m or h accepted. Not case sensitive.
#     """
#     height = input(
#         '\nWhat level of support under the inside arch would you like?'
#         '\n(L: Low Support / M: Medium Support / H: High Support): '
#         ).lower().replace(' ', '')
#     if height.startswith('l'):
#         order_data[1] = 'Low'
#     elif height.startswith('m'):
#         order_data[1] = 'Medium'
#     elif height.startswith('h'):
#         order_data[1] = 'High'
#     else:
#         print(f'\nIncorrect information provided for arch height: {height}')
#         get_height_data()


# def get_width_data():
#     """
#     Width user input converted into ['Narrow', 'Standard', 'Wide'] for
#     order_data
#     """
#     width = input(
#         '\nWidth of insole to fit the foot &/or shoe'
#         '\n(N: Narrow / S: Standard / W: Wide): '
#         ).lower().replace(' ', '')
#     if width.startswith('n'):
#         order_data[2] = 'Narrow'
#     elif width.startswith('s'):
#         order_data[2] = 'Standard'
#     elif width.startswith('w'):
#         order_data[2] = 'Wide'
#     else:
#         print(f'\nIncorrect information provided for insole width: {width}')
#         get_width_data()


def get_order_data():
    """
    Collection of User input used to order N3D Orthosis.
    """
    get_size_data()
    get_height_data()
    get_width_data()


def input_order_no():
    """
    Checks the user input order number is only numerical and correct length
    """
    print('Please enter your order number below.')
    print(
        'This information should be in a valid syntax, with no spaces.'
        'For example:\n'
        )
    print('Example order_no format: 2205190001\n')
    while True:
        try:
            order_no = int(input('You Order Number: ').replace(' ', ''))
            order_no_string = str(order_no)
            if len(order_no_string) != 10:
                raise ValueError(
                    'Our order numbers require 10 digits.'
                    f'\nUnfortunatley {order_no} has {len(order_no_string)}'
                    ' digits.'
                )
        except ValueError as error:
            print(
                f'Invalid data : {error}'
                '\nPlease check your records and try again below;\n')
            continue
        return order_no


def cancel_confirm():
    """
    Confirms the user input to cancel order and returns to start screen
    """
    confirm = input('Are you sure you wish to cancel this order? y/n : ')
    if confirm.startswith('y'):
        return True
    elif confirm.startswith('n'):
        start()
