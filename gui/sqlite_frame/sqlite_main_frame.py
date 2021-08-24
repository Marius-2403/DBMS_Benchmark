import tkinter as tk
from tkinter import ttk

from gui.sqlite_frame.speedtests.cross_join_speedtest_frame import create_sqlite_cross_join_speedtest
from gui.sqlite_frame.speedtests.input_speedtest_frame import create_sqlite_input_speedtest
from gui.sqlite_frame.speedtests.random_access_speedtest_frame import create_sqlite_random_access_speedtest
from gui.sqlite_frame.speedtests.order_by_speedtest_frame import create_sqlite_order_by_speedtest
from gui.sqlite_frame.speedtests.delete_speedtest_frame import create_sqlite_delete_speedtest
from gui.sqlite_frame.speedtests.update_speedtest_frame import create_sqlite_update_speedtest


def create_sqlite(root):
    """
    Creates the left frame of the interface with different tests.
    :param root: The items of this function will be placed in the root
    """
    frame = tk.Frame(root, background='#ccd9ff')
    frame["borderwidth"] = 3
    frame['relief'] = 'solid'
    frame.grid(row=0, column=0, padx=5, pady=5)

    # Title label
    w = tk.Label(frame, text="SQLite", background='#ccd9ff')
    w.config(font=("Arial", 15))
    w.grid(row=0, column=0)

    # Separators between the different sections
    ttk.Separator(frame).place(x=0, y=26, relwidth=1)
    ttk.Separator(frame).place(x=0, y=84, relwidth=1)
    ttk.Separator(frame).place(x=0, y=139, relwidth=1)
    ttk.Separator(frame).place(x=0, y=249, relwidth=1)
    ttk.Separator(frame).place(x=0, y=304, relwidth=1)
    ttk.Separator(frame).place(x=0, y=360, relwidth=1)

    # Create sections for the tests
    create_sqlite_input_speedtest(frame)
    create_sqlite_cross_join_speedtest(frame)
    create_sqlite_random_access_speedtest(frame)
    create_sqlite_order_by_speedtest(frame)
    create_sqlite_delete_speedtest(frame)
    create_sqlite_update_speedtest(frame)
