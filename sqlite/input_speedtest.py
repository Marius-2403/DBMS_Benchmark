import os
import sqlite3

from datetime import datetime
from random import randrange


def input_speedtest(amount):
    """
    Tests the input speed of the database by adding amount lines to it and
    calculating the time of the process.
    :param amount: The amount of lines wich will be added to the database
    :return: The time the function needed to add the lines to the database
    """
    # Create Database
    connection = sqlite3.connect("sqlite_input.db")
    cursor = connection.cursor()

    # Create table
    cursor.execute('''CREATE TABLE numbers
                       (time text, number text)''')

    # Fill the Database
    start = datetime.now()
    for x in range(amount):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{randrange(100)}')")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    # Deletes the benchmark database
    os.remove("sqlite_input.db")

    return result.total_seconds()
