#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
Results sorted by states.id ascending
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server on localhost, port 3306
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=password, db=db_name, charset="utf8")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
