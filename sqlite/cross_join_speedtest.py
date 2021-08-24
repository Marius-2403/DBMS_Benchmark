import os
import sqlite3

from datetime import datetime
from random import randrange


def create_cross_join_db(lines):
    """
    If there is no database for the cross_join_speedtest it will create one with to tables
    :param lines: The amount of lines which will be added to both tables of the database
    """
    # Deletes a database if its already there
    if os.path.isfile("sqlite_cross_join.db"):
        os.remove("sqlite_cross_join.db")

    # Create Database
    connection = sqlite3.connect("sqlite_cross_join.db")
    cursor = connection.cursor()

    # Create the first table
    cursor.execute('''CREATE TABLE numbers_one
                               (time text, number text)''')
    # Create the second table
    cursor.execute('''CREATE TABLE numbers_two
                                   (time text, number text)''')

    # Fill the database
    for i in range(lines):
        cursor.execute(f"INSERT INTO numbers_one VALUES ('{datetime.now().time()}','{i}')")
        cursor.execute(f"INSERT INTO numbers_two VALUES ('{datetime.now().time()}','{i}')")

    # Save (commit) the changes
    connection.commit()

    # Closes the connection
    connection.close()


def cross_join_speedtest(searches):
    """
    Uses a database with two tables and cross joins them. Two random numbers will determine which
    line will be selected.
    :param searches: Determines how many lines will be searched
    :return: The time the function needed to find the lines in the cross joined database
    """
    # Creates the Database with the default amount of lines
    if not os.path.isfile("sqlite_cross_join.db"):
        create_cross_join_db(100000)

    # Connects to the db
    connection = sqlite3.connect("sqlite_cross_join.db")
    cursor = connection.cursor()

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
                        WHERE numbers_one.number = '{x}' AND \
                        numbers_two.number = '{y}' ")
    result = datetime.now() - start

    # Closes the connection
    connection.close()

    return result.total_seconds()
