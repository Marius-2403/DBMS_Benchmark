import pyodbc

from datetime import datetime
import sql_server_connection


def update_speedtest(lines):
    """
    Creates a database with a given amount of lines and updates each line afterwards
    :param lines: Determines how many lines will be updated
    :return: Returns the needed time to update all lines with the UPDATE command
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
    for x in range(lines):
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{x}')")

    # Updates the lines
    start = datetime.now()
    for i in range(lines):
        cursor.execute(f"UPDATE numbers SET Zahl = '{lines - i}' WHERE Zahl = '{i}'")
    result = datetime.now() - start

    # Deletes the Table
    cursor.execute("DROP table IF EXISTS numbers")
    connection.commit()

    return result.total_seconds()
