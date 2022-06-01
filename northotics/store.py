"""
Conatins moduels to import and export live data and
set global fixed and modifiable variables
"""
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('n3orthotics')
REGEX = r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$'

user_data = ['f_name', 'l_name', 'user_email']
order_data = [
    'size_eu', 'height', 'width', 'order_no', '', 'order_status', '', 'row_no'
    ]
update_order = ['order_status', 'order_update']
export_data = []
