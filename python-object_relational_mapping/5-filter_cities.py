#!/usr/bin/python3
"""script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connexion = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    argv_4 = argv[4].split(';')[0]

    curs = connexion.cursor()
    curs.execute("""
                SELECT cities.name
                FROM cities
                INNER JOIN states ON cities.state_id = states.id
                WHERE states.name = '{}'
                ORDER BY cities.id ASC;
                """.format(argv_4))

    rows = curs.fetchall()
    liste_cities = ()

    if len(rows) > 0:
        print(rows[0][0], end="")
    for row in rows[1:]:
        print(", " + row[0], end="")

    print()
    curs.close()
    connexion.close()
