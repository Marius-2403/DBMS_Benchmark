# DBMS Benchmark

## Vorstellungsvideo
- https://www.youtube.com/watch?v=yo6EIFjqBzk

## Installation
### 1. Projekt Klonen 
- Neuen Ordner an einer beliebigen Stelle erstellen.
- Repository in den neuen Ordner mit PyCharm Klonen.
- Wenn gefragt wird, ob eine virtuelle Umgebung erzeugt werden soll, zustimmen. 

### 2. SQL-Server Connection einstellen
- Zuerst sollte in Microsoft SQL Server Management Studio auf einem lokalen Server eine neue Datenbank erstellt werden.
- Der Name des Servers und der Name der Datenbank muss dann in der Datei sql_server_connection.py eingetragen werden.

### 3. main.py
- Nach dem Ausführen der vorherigen Schritte sollte man die main.py starten können.
- Sollte beim Ausführen nach einen Interpreter gefragt werden, einfach einen aktuellen auswählen.
- Sollte keine Installation des pyodbc requirements vorhanden sein, 
  - kann dies in der Python Konsole mit "pip install pyodbc" installiert werden oder
  - oder, wenn das nicht funktioniert, in der gui/window.py auf das pyodbc import Statement gehen und
  "install package" in den "Quick-Fixes" auswählen.
- Zum Schreiben des Programmes wurde Python 3.8 genutzt.
