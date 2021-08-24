import os
import sqlite3

from datetime import datetime


def delete_speedtest(size):
    """
    Creates a database with a given size and deletes the data afterwards
    with the DELETE command
    :param size: Determines the size of the created database in lines
    :return: Returns the time the DBMS needed to delete the data
    """
    # Create Database
    connection = sqlite3.connect("sqlite_delete.db")
    cursor = connection.cursor()

    # Create table
    cursor.execute('''CREATE TABLE numbers
                       (time text, number text)''')

    # Fill the Database
    for x in range(size):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{x}')")

    # Deletes the Data
    start = datetime.now()
    for y in range(size):
        cursor.execute(f"DELETE FROM numbers WHERE numbers.number = '{y}'")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    # Deletes the benchmark database
    os.remove("sqlite_delete.db")

    return result.total_seconds()
