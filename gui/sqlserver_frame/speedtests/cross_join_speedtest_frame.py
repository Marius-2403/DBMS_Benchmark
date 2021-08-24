import tkinter as tk

import sqlserver.cross_join_speedtest


def create_sqlserver_cross_join_speedtest(frame):
    """
    Creates the buttons for the cross join speedtest and connects them with the function to execute them.
    Also gives the opportunity to change the linkes of the database
    :param frame: The items of this function will be placed in the given frame
    """
    test_name_lable = tk.Label(frame, text="Cross Join Speedtest: ", background='#ccd9ff')
    test_name_lable.config(font=("Arial", 10))
    test_name_lable.grid(row=5, column=0)

    test_1_button = tk.Button(frame, text="1",
                              command=lambda: get_cross_join_speedtest_result(1, lapsed_time_label),
                              borderwidth=1)
    test_1_button.grid(row=5, column=1, padx=5, pady=5)
    test_1_button['relief'] = 'solid'

    test_5_button = tk.Button(frame, text="5",
                              command=lambda: get_cross_join_speedtest_result(5, lapsed_time_label),
                              borderwidth=1)
    test_5_button.grid(row=5, column=2, padx=5, pady=5)
    test_5_button['relief'] = 'solid'

    test_10_button = tk.Button(frame, text="10",
                               command=lambda: get_cross_join_speedtest_result(10, lapsed_time_label),
                               borderwidth=1)
    test_10_button.grid(row=5, column=3, padx=5, pady=5)
    test_10_button['relief'] = 'solid'

    result_label = tk.Label(frame, text="Ergebnis: ", background='#ccd9ff')
    result_label.grid(row=6, column=0)

    lapsed_time_label = tk.Label(frame, text="---", background='#ccd9ff')
    lapsed_time_label.grid(row=6, column=1)

    seconds_label = tk.Label(frame, text="Sekunden", background='#ccd9ff')
    seconds_label.grid(row=6, column=2)

    configure_db_label = tk.Label(frame, text="DB Größe ändern: ", background='#ccd9ff')
    configure_db_label.grid(row=7, column=0)

    db_10k_button = tk.Button(frame, text="10.000",
                              command=lambda: modify_cross_join_db(10000, display_lines_label, "10.000"),
                              borderwidth=1)
    db_10k_button.grid(row=7, column=1, padx=5, pady=5)
    db_10k_button['relief'] = 'solid'

    db_100k_button = tk.Button(frame, text="100.000",
                               command=lambda: modify_cross_join_db(100000, display_lines_label, "100.000"),
                               borderwidth=1)
    db_100k_button.grid(row=7, column=2, padx=5, pady=5)
    db_100k_button['relief'] = 'solid'

    db_1mil_button = tk.Button(frame, text="1.000.000",
                               command=lambda: modify_cross_join_db(1000000, display_lines_label, "1.000.000"),
                               borderwidth=1)
    db_1mil_button.grid(row=7, column=3, padx=5, pady=5)
    db_1mil_button['relief'] = 'solid'

    lines_now_label = tk.Label(frame, text="Aktuelle Größe: ", background='#ccd9ff')
    lines_now_label.grid(row=8, column=0)

    display_lines_label = tk.Label(frame, text="100.000", background='#ccd9ff')
    display_lines_label.grid(row=8, column=1)


def get_cross_join_speedtest_result(searches, label):
    """
    Refreshes the label to showcase the result of the test
    :param searches: The amount of cross join selects the test does
    :param label: Changes the text of the given label
    """
    result = sqlserver.cross_join_speedtest.cross_join_speedtest(searches)
    label.config(text=result)


def modify_cross_join_db(lines, label, lines_string):
    """
    Generates a database for the cross join tests and updates the amount of lines to be synchronized with the database
    :param lines: amount of lines for the database
    :param label: Changes the text of the given label
    :param lines_string: Gives a string which will be displayed in the label
    """
    sqlserver.cross_join_speedtest.create_cross_join_db(lines)
    label.config(text=lines_string)
