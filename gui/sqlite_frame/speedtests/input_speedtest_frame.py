import tkinter as tk

import sqlite.input_speedtest


def create_sqlite_input_speedtest(frame):
    """
    Creates the buttons for the input speedtest and connects them with the function to execute them
    :param frame: The items of this function will be placed in the given frame
    """
    test_name_lable = tk.Label(frame, text="Input Speedtest: ", background='#ccd9ff')
    test_name_lable.config(font=("Arial", 10))
    test_name_lable.grid(row=1, column=0)

    test_10k_button = tk.Button(frame, text="10.000",
                                command=lambda: get_input_speedtest_result(10000, lapsed_time_label),
                                borderwidth=1)
    test_10k_button.grid(row=1, column=1, padx=5, pady=5)
    test_10k_button['relief'] = 'solid'

    test_100k_button = tk.Button(frame, text="100.000",
                                 command=lambda: get_input_speedtest_result(100000, lapsed_time_label),
                                 borderwidth=1)
    test_100k_button.grid(row=1, column=2, padx=5, pady=5)
    test_100k_button['relief'] = 'solid'

    test_1mil_button = tk.Button(frame, text="1.000.000",
                                 command=lambda: get_input_speedtest_result(1000000, lapsed_time_label),
                                 borderwidth=1)
    test_1mil_button.grid(row=1, column=3, padx=5, pady=5)
    test_1mil_button['relief'] = 'solid'

    result_label = tk.Label(frame, text="Ergebnis: ", background='#ccd9ff')
    result_label.grid(row=2, column=0)

    lapsed_time_label = tk.Label(frame, text="---", background='#ccd9ff')
    lapsed_time_label.grid(row=2, column=1)

    seconds_label = tk.Label(frame, text="Sekunden", background='#ccd9ff')
    seconds_label.grid(row=2, column=2)


def get_input_speedtest_result(amount, label):
    """
    Refreshes the label to showcase the result of the test
    :param amount: Defines the amount of rows which will be added to the database
    :param label: Changes the text of the given label
    """
    result = sqlite.input_speedtest.input_speedtest(amount)
    label.config(text=result)
