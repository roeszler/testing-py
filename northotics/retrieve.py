"""
Functions related to retrieving data
"""
from northotics.inputs import input_order_no
from northotics.manipulation import flatten_nested_list
from northotics.store import SHEET


def retrieve_order():
    """
    Searches worksheet coloum 'order_no' for a match to user input and
    returns row information to local user_data, oder_data and export_data lists
    """
    search_input = str(input_order_no())
    order_nos_import = SHEET.worksheet('orders').get_values('G:G')
    order_nos = flatten_nested_list(order_nos_import)
    order_match = [
        i for i in range(len(order_nos)) if order_nos[i] == search_input
        ]
    if order_match == []:
        print(f'Order number {search_input} not found?!\n')
        retrieve_order()
    else:
        for i in range(len(order_nos)):
            if search_input == order_nos[i]:
                search_match_row = i+1
                print(f'\nOrder found in database row no. {search_match_row}')
                return search_match_row
