"""
Module with code related to updating dates and times
"""
import datetime
from datetime import timezone
from northotics.store import order_data


def update_date_ordered():
    """
    Updates the order_date filed within order_data list
    """
    time_zone = generate_utc_time()
    order_data[4] = time_zone
    order_data[5] = 'NEW ORDER'


def generate_utc_time():
    """
    Creates Univesal Coordinated time (UTC) version of date and time
    in iso format
    """
    iso_utc_now = datetime.datetime.now(timezone.utc).isoformat()
    return iso_utc_now
