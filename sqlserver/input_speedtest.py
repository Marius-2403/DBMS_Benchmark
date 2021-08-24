import pyodbc

from datetime import datetime
from random import randrange
import sql_server_connection


def input_speedtest(amount):
    """
    Tests the input speed of the database by adding amount lines to it and
    calculating the time of the process.
    :param amount: The amount of lines wich will be added to the database
    :return: The time the function needed to add the lines to the database
    """
    # Connects to SQL-Server
    connection = pyodbc.connect('Driver={SQL Server};'
                                f'Server={sql_server_connection.server};'
                                f'Database={sql_server_connection.database};'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()

    # Deletes the table if it already exists
    cursor.execute("DROP table IF EXISTS numbers")
    connection.commit()

    # Creates a new table
    cursor.execute('''CREATE TABLE numbers (
                        Datum text, Zahl int)''')

    # Fills the Database
    start = datetime.now()
    for x in range(amount):
        cursor.execute(f"INSERT INTO numbers (Datum, Zahl) VALUES ('{datetime.now().time()}','{randrange(100)}')")
    result = datetime.now() - start

    # Deletes the Table
    cursor.execute("DROP table IF EXISTS numbers")
    connection.commit()

    return result.total_seconds()
