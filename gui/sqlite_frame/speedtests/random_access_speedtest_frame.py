import tkinter as tk

import sqlite.random_access_speedtest


def create_sqlite_random_access_speedtest(frame):
    """
    Creates the buttons for the random access speedtest and connects them with the function to execute them
    :param frame: The items of this function will be placed in the given frame
    """
    test_name_lable = tk.Label(frame, text="Random access Speedtest: ", background='#ccd9ff')
    test_name_lable.config(font=("Arial", 10))
    test_name_lable.grid(row=3, column=0)

    test_1k_button = tk.Button(frame, text="100",
                               command=lambda: get_random_access_speedtest_result(100, lapsed_time_label),
                               borderwidth=1)
    test_1k_button.grid(row=3, column=1, padx=5, pady=5)
    test_1k_button['relief'] = 'solid'

    test_10k_button = tk.Button(frame, text="1.000",
                                command=lambda: get_random_access_speedtest_result(1000, lapsed_time_label),
                                borderwidth=1)
    test_10k_button.grid(row=3, column=2, padx=5, pady=5)
    test_10k_button['relief'] = 'solid'

    test_100k_button = tk.Button(frame, text="10.000",
                                 command=lambda: get_random_access_speedtest_result(10000, lapsed_time_label),
                                 borderwidth=1)
    test_100k_button.grid(row=3, column=3, padx=5, pady=5)
    test_100k_button['relief'] = 'solid'

    result_label = tk.Label(frame, text="Ergebnis: ", background='#ccd9ff')
    result_label.grid(row=4, column=0)

    lapsed_time_label = tk.Label(frame, text="---", background='#ccd9ff')
    lapsed_time_label.grid(row=4, column=1)

    seconds_label = tk.Label(frame, text="Sekunden", background='#ccd9ff')
    seconds_label.grid(row=4, column=2)


def get_random_access_speedtest_result(accesses, label):
    """
    Refreshes the label to showcase the result of the test
    :param accesses: The amount of random accesses which will be executed in the test
    :param label: Changes the text of the given label
    """
    result = sqlite.random_access_speedtest.random_select_speedtest(accesses)
    label.config(text=result)
