import tkinter as tk

import sqlite.delete_speedtest


def create_sqlite_delete_speedtest(frame):
    """
    Creates the buttons for the delete speedtest and connects them with the function to execute them
    :param frame: The items of this function will be placed in the given frame
    """
    test_name_lable = tk.Label(frame, text="Delete Speedtest: ", background='#ccd9ff')
    test_name_lable.config(font=("Arial", 10))
    test_name_lable.grid(row=13, column=0)

    test_1k_button = tk.Button(frame, text="1.000",
                               command=lambda: get_delete_speedtest_result(1000, lapsed_time_label),
                               borderwidth=1)
    test_1k_button.grid(row=13, column=1, padx=5, pady=5)
    test_1k_button['relief'] = 'solid'

    test_10k_button = tk.Button(frame, text="10.000",
                                command=lambda: get_delete_speedtest_result(10000, lapsed_time_label),
                                borderwidth=1)
    test_10k_button.grid(row=13, column=2, padx=5, pady=5)
    test_10k_button['relief'] = 'solid'

    test_20k_button = tk.Button(frame, text="20.000",
                                command=lambda: get_delete_speedtest_result(20000, lapsed_time_label),
                                borderwidth=1)
    test_20k_button.grid(row=13, column=3, padx=5, pady=5)
    test_20k_button['relief'] = 'solid'

    result_label = tk.Label(frame, text="Ergebnis: ", background='#ccd9ff')
    result_label.grid(row=14, column=0)

    lapsed_time_label = tk.Label(frame, text="---", background='#ccd9ff')
    lapsed_time_label.grid(row=14, column=1)

    seconds_label = tk.Label(frame, text="Sekunden", background='#ccd9ff')
    seconds_label.grid(row=14, column=2)


def get_delete_speedtest_result(size, label):
    """
    Refreshes the label to showcase the result of the test
    :param size: The amount of lines the database will have
    :param label: Changes the text of the given label
    """
    result = sqlite.delete_speedtest.delete_speedtest(size)
    label.config(text=result)
