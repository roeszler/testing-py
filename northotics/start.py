"""
Conatins start screen function
"""
from northotics.system import clear_screen
from northotics.display import (
    display_order, summary_order_data, instruct_user_data, yes_no_user
    )
from northotics.manipulation import combine_data_for_export
from northotics.inputs import get_user_data


def start():
    """
    Start screen prompting user to Create or Retrieve an exsisting order
    using an order number
    """
    print('Welcome to N(3)ORTHOTICS order portal.\n')
    print('Use this app to directly access made-to-order N3D Printed Insoles')
    print('Please visit northotics.com/home for more information\n')
    print('Select 1. : Place a new N3D insole order')
    print('Select 2. : Retrieve an exsisting N3D order')
    print('Select 3. : Exit Program\n')


def select_option():
    """
    Initial user choice to place a new or retieve an exsisting N3D order
    """
    correct = input('Your Selection: ')
    for i in correct:
        if i == '1':
            return True
        elif i == '2':
            clear_screen()
            print('Retieve an esxisting N3D insole order : \n')
            display_order()
        elif i == '3':
            clear_screen()
            quit()
        else:
            print(
                f'The number you have provided "{correct}" is not available.')
            print('Please select again\n')
            select_option()


instruct_user_data()
get_user_data()
clear_screen()
yes_no_user()
summary_order_data()
combine_data_for_export()


# def main():
#     """
#     Run all primary program functions
#     """
#     clear_screen()
#     start()
#     select_option()
#     instruct_user_data()
#     get_user_data()
#     clear_screen()
#     yes_no_user()
#     summary_order_data()
#     combine_data_for_export()
