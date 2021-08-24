import os
import tkinter as tk
import pyodbc

import sql_server_connection
from gui.sqlite_frame.sqlite_main_frame import create_sqlite
from gui.sqlserver_frame.sqlserver_main_frame import create_sqlserver
from gui.description_frame.description_main_frame import create_description


def initialize_window():
    """
    Creates a tkinter window as a frontend for the performance tests
    """
    root = tk.Tk()
    root.title("DBMS Benchmark")

    root.configure(background='#004181')

    # Deletes the database so it will be synchronized when the programm is started
    if os.path.isfile("sqlite_cross_join.db"):
        os.remove("sqlite_cross_join.db")

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

    # initializes both frames for the different DBMS systems
    create_sqlite(root)
    create_sqlserver(root)
    create_description(root)

    root.mainloop()
