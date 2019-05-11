import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("movies.json").read_text())
print(movies)

if False:
    with sqlite3.connect("db.sqlite3") as connection:
        command = "INSERT INTO Movies VALUES(?, ?, ?)"
        for movie in movies:
            connection.execute(command, tuple(movie.values()))
        connection.commit()

with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies2 = cursor.fetchall()
    print(movies2)