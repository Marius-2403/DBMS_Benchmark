import tkinter as tk

import sqlite.order_by_speedtest


def create_sqlite_order_by_speedtest(frame):
    """
    Creates the buttons for the ORDER BY speedtest and connects them with the function to execute them
    :param frame: The items of this function will be placed in the given frame
    """
    test_name_lable = tk.Label(frame, text="Order By Speedtest: ", background='#ccd9ff')
    test_name_lable.config(font=("Arial", 10))
    test_name_lable.grid(row=9, column=0)

    test_100k_button = tk.Button(frame, text="100.000",
                                 command=lambda: get_order_by_speedtest_result(100000, lapsed_time_label),
                                 borderwidth=1)
    test_100k_button.grid(row=9, column=1, padx=5, pady=5)
    test_100k_button['relief'] = 'solid'

    test_1mil_button = tk.Button(frame, text="1.000.000",
                                 command=lambda: get_order_by_speedtest_result(1000000, lapsed_time_label),
                                 borderwidth=1)
    test_1mil_button.grid(row=9, column=2, padx=5, pady=5)
    test_1mil_button['relief'] = 'solid'

    test_10mil_button = tk.Button(frame, text="10.000.000",
                                  command=lambda: get_order_by_speedtest_result(10000000, lapsed_time_label),
                                  borderwidth=1)
    test_10mil_button.grid(row=9, column=3, padx=5, pady=5)
    test_10mil_button['relief'] = 'solid'

    result_label = tk.Label(frame, text="Ergebnis: ", background='#ccd9ff')
    result_label.grid(row=10, column=0)

    lapsed_time_label = tk.Label(frame, text="---", background='#ccd9ff')
    lapsed_time_label.grid(row=10, column=1)

    seconds_label = tk.Label(frame, text="Sekunden", background='#ccd9ff')
    seconds_label.grid(row=10, column=2)


def get_order_by_speedtest_result(size, label):
    """
    Refreshes the label to showcase the result of the test
    :param size: The amount of lines the database will have
    :param label: Changes the text of the given label
    """
    result = sqlite.order_by_speedtest.order_by_speedtest(size)
    label.config(text=result)
