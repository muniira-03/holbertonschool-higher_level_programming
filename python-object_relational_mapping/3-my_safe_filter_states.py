#!/usr/bin/python3
"""write one that is safe from MySQL injections!"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    # Selects the text preceding the semicolon (if any)
    # in argv[4] to prevent SQL injections.
    argv_4 = argv[4].split(';')[0]

    curs = connexion.cursor()
    curs.execute("""SELECT * FROM states
                 WHERE BINARY name LIKE '{}%'
                 ORDER BY id;""".format(argv_4))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    connexion.close()
