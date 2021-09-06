import pyodbc

from datetime import datetime
import sql_server_connection


def delete_speedtest(size):
    """
    Creates a database with a given size and deletes the data afterwards
    with the DELETE command
    :param size: Determines the size of the created database in lines
    :return: Returns the time the DBMS needed to delete the data
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
        cursor.execute(f"INSERT INTO numbers VALUES ('{datetime.now().time()}','{x}')")

    # Deletes the Data
    start = datetime.now()
    for y in range(size):
        cursor.execute(f"DELETE FROM numbers WHERE numbers.Zahl = {y}")
    result = datetime.now() - start

    # Deletes the Table
    cursor.execute("DROP table IF EXISTS numbers")
    connection.commit()

    return result.total_seconds()
