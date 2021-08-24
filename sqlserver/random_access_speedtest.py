import pyodbc

from datetime import datetime
from random import randrange
import sql_server_connection


def random_select_speedtest(accesses):
    """
    Calculates the time the database needs to for x accesses in a table of 100.000 lines
    :param accesses: How often a random access will be executed
    :return: The time the function needed to find the lines in the database
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
    for x in range(100000):
        cursor.execute(f"INSERT INTO numbers (Datum, Zahl) VALUES ('{datetime.now().time()}','{x}')")

    # Makes random accesses
    start = datetime.now()
    for i in range(accesses):
        accesses_number = randrange(100000)
        cursor.execute(f"SELECT * FROM numbers WHERE numbers.Zahl = {accesses_number}")
    result = datetime.now() - start

    # Deletes the Table
    cursor.execute("DROP table IF EXISTS numbers")
    connection.commit()

    return result.total_seconds()

