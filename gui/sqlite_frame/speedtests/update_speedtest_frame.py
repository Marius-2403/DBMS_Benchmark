import tkinter as tk

import sqlite.update_speedtest


def create_sqlite_update_speedtest(frame):
    """
    Creates the buttons for the update speedtest and connects them with the function to execute them
    :param frame:
    """
    test_name_lable = tk.Label(frame, text="Update Speedtest: ", background='#ccd9ff')
    test_name_lable.config(font=("Arial", 10))
    test_name_lable.grid(row=11, column=0)

    test_1k_button = tk.Button(frame, text="1.000",
                               command=lambda: get_update_speedtest_result(1000, lapsed_time_label),
                               borderwidth=1)
    test_1k_button.grid(row=11, column=1, padx=5, pady=5)
    test_1k_button['relief'] = 'solid'

    test_10k_button = tk.Button(frame, text="10.000",
                                command=lambda: get_update_speedtest_result(10000, lapsed_time_label),
                                borderwidth=1)
    test_10k_button.grid(row=11, column=2, padx=5, pady=5)
    test_10k_button['relief'] = 'solid'

    test_20k_button = tk.Button(frame, text="20.000",
                                command=lambda: get_update_speedtest_result(20000, lapsed_time_label),
                                borderwidth=1)
    test_20k_button.grid(row=11, column=3, padx=5, pady=5)
    test_20k_button['relief'] = 'solid'

    result_label = tk.Label(frame, text="Ergebnis: ", background='#ccd9ff')
    result_label.grid(row=12, column=0)

    lapsed_time_label = tk.Label(frame, text="---", background='#ccd9ff')
    lapsed_time_label.grid(row=12, column=1)

    seconds_label = tk.Label(frame, text="Sekunden", background='#ccd9ff')
    seconds_label.grid(row=12, column=2)


def get_update_speedtest_result(lines, label):
    """
    Refreshes the label to showcase the result of the test
    :param lines: Defines the amount of rows which will be added to the database
    :param label: Changes the text of the given label
    """
    result = sqlite.update_speedtest.update_speedtest(lines)
    label.config(text=result)
