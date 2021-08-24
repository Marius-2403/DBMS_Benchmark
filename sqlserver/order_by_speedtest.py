import pyodbc

from random import randrange
from datetime import datetime
import sql_server_connection


def order_by_speedtest(size):
    """
    Creates a database with a given size and orders it with the ORDER BY SQL command
    :param size: Determines the size of the created database in lines
    :return: Returns the time the DBMS needed to order the data
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

    # Fill the Database
    for x in range(size):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{randrange(1000)}')")

    # Orders the data
    start = datetime.now()
    cursor.execute("SELECT * FROM numbers ORDER BY numbers.Zahl ASC")
    result = datetime.now() - start

    # Deletes the Table
    cursor.execute("DROP table IF EXISTS numbers")
    connection.commit()

    return result.total_seconds()
