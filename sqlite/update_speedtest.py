import os
import sqlite3

from datetime import datetime


def update_speedtest(lines):
    """
    Creates a database with a given amount of lines and updates each line afterwards
    :param lines: Determines how many lines will be updated
    :return: Returns the needed time to update all lines with the UPDATE command
    """
    # Create Database
    connection = sqlite3.connect("sqlite_update.db")
    cursor = connection.cursor()

    # Create table
    cursor.execute('''CREATE TABLE numbers
                       (time text, number text)''')

    # Fill the Database
    for x in range(lines):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{x}')")

    # Updates the lines
    start = datetime.now()
    for i in range(lines):
        cursor.execute(f"UPDATE numbers SET number = '{lines - i}' WHERE number = '{i}'")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    # Deletes the benchmark database
    os.remove("sqlite_update.db")

    return result.total_seconds()
