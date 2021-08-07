import pprint
import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("data.db")

create_movies_table_sql = """
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT NOT NULL,
    year INTEGER NOT NULL,
    length_minutes INTEGER NOT NULL
);
"""


execute_query(connection, create_movies_table_sql)

insert_movies = """
INSERT INTO movies
    (title, director, year, length_minutes)
VALUES
    ('First Movie', 'John', 1985, 120),
    ('Second Movie', 'John', 1965, 120),
    ('Second Movie 2', 'John', 1965, 20)
;
"""

execute_query(connection, insert_movies)

get_all_movies = """
SELECT * FROM movies;
"""

pprint.pprint(execute_read_query(connection, get_all_movies))
