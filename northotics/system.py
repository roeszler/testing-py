"""
Imports modules used to interact with various operating systems
"""
import os


def clear_screen():
    """
    Checks if Operating System is Mac and Linux or Windows and
    clears the screen
    """
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
