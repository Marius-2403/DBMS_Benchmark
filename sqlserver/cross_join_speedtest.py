import pyodbc

from datetime import datetime
from random import randrange
import sql_server_connection


def create_cross_join_db(lines):
    """
    If there is no database for the cross_join_speedtest it will create one with to tables
    :param lines: The amount of lines which will be added to both tables of the database
    """
    # Connects to SQL-Server
    connection = pyodbc.connect('Driver={SQL Server};'
                                f'Server={sql_server_connection.server};'
                                f'Database={sql_server_connection.database};'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()

    # Deletes the first Table
    cursor.execute("DROP table IF EXISTS numbers_one")
    connection.commit()

    # Deletes the second Table
    cursor.execute("DROP table IF EXISTS numbers_two")
    connection.commit()

    # Creates the first table
    cursor.execute('''CREATE TABLE numbers_one (
                            Datum text, Zahl int)''')

    # Create the second table
    cursor.execute('''CREATE TABLE numbers_two (
                            Datum text, Zahl int)''')

    # Fill the database
    for i in range(lines):
        cursor.execute(f"INSERT INTO numbers_one (Datum, Zahl) VALUES ('{datetime.now().time()}','{i}')")
        cursor.execute(f"INSERT INTO numbers_two (Datum, Zahl) VALUES ('{datetime.now().time()}','{i}')")

    # Save (commit) the changes
    connection.commit()

    # Closes the connection
    connection.close()


def check_table_exists(connection, name):
    """
    Checks if a table with a given name exists in the given database
    :param connection: The connection to the database
    :param name: The name of the table which will be checked
    :return: Returns True if a table with the given name exists otherwise returns False
    """
    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(name.replace('\'', '\'\'')))
    if cursor.fetchone()[0] == 1:
        cursor.close()
        return True

    cursor.close()
    return False


def cross_join_speedtest(searches):
    """
    Uses a database with two tables and cross joins them. Two random numbers will determine which
    line will be selected.
    :param searches: Determines how many lines will be searched
    :return: The time the function needed to find the lines in the cross joined database
    """
    # Connects to SQL-Server
    connection = pyodbc.connect('Driver={SQL Server};'
                                f'Server={sql_server_connection.server};'
                                f'Database={sql_server_connection.database};'
                                'Trusted_Connection=yes;')
    cursor = connection.cursor()

    if not check_table_exists(connection, "numbers_one"):
        create_cross_join_db(100000)

    # get the amount of rows of the database
    i = 0
    for row in cursor.execute("SELECT * from numbers_one"):
        i += 1

    # Cross joins both tables and searches a random generated date
    start = datetime.now()
    for amount in range(searches):
        x = randrange(i)
        y = randrange(i)
        cursor.execute(f"SELECT * FROM numbers_one CROSS JOIN numbers_two \
                        WHERE numbers_one.Zahl = '{x}' AND \
                        numbers_two.Zahl = '{y}' ")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    return result.total_seconds()
