import os
import sqlite3

from datetime import datetime
from random import randrange


def order_by_speedtest(size):
    """
    Creates a database with a given size and orders it with the ORDER BY SQL command
    :param size: Determines the size of the created database in lines
    :return: Returns the time the DBMS needed to order the data
    """
    # Create Database
    connection = sqlite3.connect("sqlite_order_by.db")
    cursor = connection.cursor()

    # Create table
    cursor.execute('''CREATE TABLE numbers
                       (time text, number text)''')

    # Fill the Database
    for x in range(size):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{randrange(1000)}')")

    # Orders the data
    start = datetime.now()
    cursor.execute("SELECT * FROM numbers ORDER BY numbers.number ASC")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    # Deletes the benchmark database
    os.remove("sqlite_order_by.db")

    return result.total_seconds()
