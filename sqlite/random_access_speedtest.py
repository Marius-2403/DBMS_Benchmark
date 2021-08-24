import os
import sqlite3

from datetime import datetime
from random import randrange


def random_select_speedtest(accesses):
    """
    Calculates the time the database needs to for x accesses in a table of 100.000 lines
    :param accesses: How often a random access will be executed
    :return: The time the function needed to find the lines in the database
    """
    # Create Database
    connection = sqlite3.connect("sqlite_random.db")
    cursor = connection.cursor()

    # Create table
    cursor.execute('''CREATE TABLE numbers
                       (time text, number text)''')

    # Fill the Database
    for x in range(100000):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{x}')")

    # Makes random accesses
    start = datetime.now()
    for i in range(accesses):
        access_number = randrange(100000)
        cursor.execute(f"SELECT * FROM numbers WHERE numbers.number = {access_number}")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    # Deletes the benchmark database
    os.remove("sqlite_random.db")

    return result.total_seconds()
