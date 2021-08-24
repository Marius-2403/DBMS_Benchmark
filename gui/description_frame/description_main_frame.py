import tkinter.messagebox
import tkinter as tk
from tkinter import ttk


def create_description(root):
    frame = tk.Frame(root, background='#ccd9ff')
    frame["borderwidth"] = 3
    frame['relief'] = 'solid'
    frame.grid(row=0, column=1, padx=5, pady=5)

    # Title label
    w = tk.Label(frame, text="Beschreibung", background='#ccd9ff')
    w.config(font=("Arial", 15))
    w.grid(row=0, column=0)

    # Separators between the different sections
    ttk.Separator(frame).place(x=0, y=26, relwidth=1)
    ttk.Separator(frame).place(x=0, y=84, relwidth=1)
    ttk.Separator(frame).place(x=0, y=139, relwidth=1)
    ttk.Separator(frame).place(x=0, y=249, relwidth=1)
    ttk.Separator(frame).place(x=0, y=304, relwidth=1)
    ttk.Separator(frame).place(x=0, y=360, relwidth=1)

    input_messagebox_content = "Beim Input Speedtest wird getestet, wie schnell man die Datenbank mit Daten befüllen " \
                               "kann. Dabei wird eine Datenbank erzeugt, die mit Daten gefüllt wird und danach " \
                               "wieder gelöscht wird. Die Zeit, die die Datenbank zum befüllen braucht wird " \
                               "gemessen. Die Zahlen auf den Knöpfen repräsentieren dabei die Anzahl an Datensätzen, " \
                               "die in die Datenbank geschrieben werden. Bei den Datensätzen handelt es sich um die " \
                               "aktuelle Zeit und eine zufällig Zahl zwischen 0 und 100. \n" \
                               "\n" \
                               "Durchschnittliche Ergebnisse auf meinem Computer: \n" \
                               "\n" \
                               "SQLite:\n" \
                               "10.000: 0,0713232 Sekunden\n" \
                               "100.000: 0,644997 Sekunden\n" \
                               "1.000.000: 7,0075072 Sekunden\n" \
                               "\n" \
                               "SQL-Server:\n" \
                               "10.000: 1,238135 Sekunden\n" \
                               "100.000: 12,0284056 Sekunden\n" \
                               "1.000.000: 126,8435617 Sekunden"

    random_access_messagebox_content = "Beim Random Access Speedtest, wird die Zeit berechnet, die das DBMS braucht, " \
                                       "um zufällige Zugriffe auf einer Datenbank zu machen. Dabei wird eine " \
                                       "Datenbank, mit 100.000 Datensätzen erzeugt. Die Datensätze bestehen dabei " \
                                       "aus der aktuellen Zeit und einer einzigartigen Zahl zwischen 0 und 100.000. " \
                                       "Die Knöpfe erzeugen dann 100, 1.000 oder 10.000 zufällige Abfragen, indem " \
                                       "sie nach einer zufälligen Zahl zwischen 0 und 100.000 suchen. \n" \
                                       "\n" \
                                       "Durchschnittliche Ergebnisse auf meinem Computer: \n" \
                                       "\n" \
                                       "SQLite:\n" \
                                       "100: 0,3235008 Sekunden\n" \
                                       "1.000: 3,1440724 Sekunden\n" \
                                       "10.000: 32,828491 Sekunden\n" \
                                       "\n" \
                                       "SQL-Server:\n" \
                                       "100: 0,591903 Sekunden\n" \
                                       "1.000: 5,480200333 Sekunden\n" \
                                       "10.000: 57,61030333 Sekunden"

    cross_join_messagebox_content = "Beim Cross Join Speedtest, wird die Zeit berechnet, die das DBMS braucht, " \
                                    "um ein Datensatz mit dem Cross Join Befehl zu finden. Die Datenbank, besteht " \
                                    "dabei aus zwei gleich großen Tabellen, die mit dem Cross Join verbunden werden. " \
                                    "Beide Tabellen werden mit der aktuellen Zeit und einer einzigartigen Zahl " \
                                    "befüllt. Bei der Suche, wird dann nach einem Datensatz, mit zwei bestimmten " \
                                    "Zahlen gesucht. Mit den 1, 5, 10 Knöpfen kann man Einstellen, wie oft gesucht " \
                                    "werden soll. Mit den anderen Knöpfen kann man die Anzahl der Datensätze in den " \
                                    "Datenbanken bestimmen, die dann mit dem Cross Join verbunden werden. \n" \
                                    "\n" \
                                    "Durchschnittliche Ergebnisse auf meinem Computer: \n" \
                                    "\n" \
                                    "SQLite:\n" \
                                    "10.000 Datensätze: \n" \
                                    "1: 0,0138058 Sekunden \n" \
                                    "5: 0,025918 Sekunden \n" \
                                    "10: 0,0659638 Sekunden\n" \
                                    "\n" \
                                    "100.000 Datensätze: \n" \
                                    "1: 0,0765206 Sekunden \n" \
                                    "5: 0,4008912 Sekunden \n" \
                                    "10: 0,8142406 Sekunden\n" \
                                    "\n" \
                                    "1.000.000 Datensätze: \n" \
                                    "1: 0,9606832 Sekunden \n" \
                                    "5: 5,2917846 Sekunden \n" \
                                    "10: 11,2540785 Sekunden\n" \
                                    "\n" \
                                    "\n" \
                                    "SQL-Server:\n" \
                                    "10.000 Datensätze: \n" \
                                    "1: 0.0093918 Sekunden \n" \
                                    "5: 0.0358396 Sekunden \n" \
                                    "10: 0.0706842 Sekunden\n" \
                                    "\n" \
                                    "100.000 Datensätze: \n" \
                                    "1: 0.0503926 Sekunden \n" \
                                    "5: 0.1190708 Sekunden \n" \
                                    "10: 0.1464676 Sekunden\n" \
                                    "\n" \
                                    "1.000.000 Datensätze: \n" \
                                    "1: --- Sekunden \n" \
                                    "5: --- Sekunden \n" \
                                    "10: --- Sekunden\n" \
                                    "\n"

    order_by_messagebox_content = "Beim Order By Speedtest, wird die Zeit berechnet, die das DBMS braucht, um eine " \
                                  "Datenbank mit dem ORDER BY Befehl zu sortieren. Dafür wird eine Datenbank mit " \
                                  "100.000, 1.000.000. oder 10.000.000 Datensätzen erzeugt. Die Datensätze bestehen " \
                                  "aus der aktuellen Zeit und einer zufälligen Zahl zwischen 0 und 1000. Es werden " \
                                  "dann alle Datensätze abgefragt und Aufsteigend nach der Zahl sortiert. \n" \
                                  "\n" \
                                  "Durchschnittliche Ergebnisse auf meinem Computer: \n" \
                                  "\n" \
                                  "SQLite:\n" \
                                  "100.000:  0.0360561 Sekunden\n" \
                                  "1.000.000: 0.4313642 Sekunden\n" \
                                  "10.000.000:  4.3556848 Sekunden\n" \
                                  "\n" \
                                  "SQL-Server:\n" \
                                  "100.000: 0.020337 Sekunden\n" \
                                  "1.000.000: 0.2848357 Sekunden\n" \
                                  "10.000.000: --- Sekunden"

    update_messagebox_content = "Beim Update Speedtest, wird die Zeit berechnet, die das DBMS braucht, um alle " \
                                "Datensätze einer Tabelle upzudaten. Mit den Knöpfen kann man die größe der " \
                                "Datenbank bestimmen, die geupdatet werden soll. Für den Test wird eine Datenbank " \
                                "mit der ausgewählten Anzahl an Datensätzen erstellt und danach wieder gelöscht. " \
                                "Die Datensätze bestehen aus dem aktuellen Datum und einer Einzigartigen Zahl. " \
                                "Bei dem Updateprozess werden alle Zahlen, die vorher generiert wurden, mit neuen " \
                                "ersetzt. \n" \
                                "\n" \
                                "Durchschnittliche Ergebnisse auf meinem Computer: \n" \
                                "\n" \
                                "SQLite:\n" \
                                "1.000: 0.054958 Sekunden\n" \
                                "10.000: 5.2413187 Sekunden\n" \
                                "20.000: 22.1327254 Sekunden\n" \
                                "\n" \
                                "SQL-Server:\n" \
                                "1.000: 0.1845992 Sekunden\n" \
                                "10.000: 9.2330576 Sekunden\n" \
                                "20.000: 34.7693896 Sekunden"

    delete_messagebox_content = "Beim Delete Speedtest, wird die Zeit berechnet, die das DBMS braucht, um alle " \
                                "Datensätze einer Tabelle zu löschen. Mit den Knöpfen kann man die Anzahl der " \
                                "Datensätze bestimmen, die gelöscht werden sollen. \n" \
                                "\n" \
                                "Durchschnittliche Ergebnisse auf meinem Computer: \n" \
                                "\n" \
                                "SQLite:\n" \
                                "1.000: 0.0311184 Sekunden\n" \
                                "10.000: 2.5914934 Sekunden\n" \
                                "20.000: 11.1709674 Sekunden\n" \
                                "\n" \
                                "SQL-Server:\n" \
                                "1.000: 7.778904 Sekunden\n" \
                                "10.000: 74.934125 Sekunden\n" \
                                "20.000: 140.8468497 Sekunden"

    generate_description_button(frame, "Input Speedtest Beschreibung",
                                lambda: generate_description_window(root, "Input Speedtest Beschreibung",
                                                                    input_messagebox_content), 1)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=2, column=0)

    generate_description_button(frame, "Random Access Speedtest Beschreibung",
                                lambda: generate_description_window(root, "Random Access Speedtest Beschreibung",
                                                                    random_access_messagebox_content), 3)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=4, column=0)

    generate_description_button(frame, "Cross Join Speedtest Beschreibung",
                                lambda: generate_description_window(root, "Cross Join Speedtest Beschreibung",
                                                                    cross_join_messagebox_content), 5)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=6, column=0, padx=5, pady=1)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=7, column=0, padx=5, pady=5)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=6, column=0, padx=5, pady=12)

    generate_description_button(frame, "Order By Speedtest Beschreibung",
                                lambda: generate_description_window(root, "Order By Speedtest Beschreibung",
                                                                    order_by_messagebox_content), 9)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=10, column=0)

    generate_description_button(frame, "Update Speedtest Beschreibung",
                                lambda: generate_description_window(root, "Update Speedtest Beschreibung",
                                                                    update_messagebox_content), 11)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=12, column=0)

    generate_description_button(frame, "Delete Speedtest Beschreibung",
                                lambda: generate_description_window(root, "Delete Speedtest Beschreibung",
                                                                    delete_messagebox_content), 13)

    placeholder = tk.Label(frame, text=" ", background='#ccd9ff')
    placeholder.grid(row=14, column=0)


def generate_description_button(frame, text, command, row):
    description_button = tk.Button(frame, text=text, command=command, borderwidth=1)
    description_button.grid(row=row, column=0, padx=5, pady=5)
    description_button['relief'] = 'solid'


def generate_description_window(root, title, payload):
    tkinter.messagebox.showinfo(master=root, title=title, message=payload)
