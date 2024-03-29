import sqlite3
from sqlite3 import Error
from sqlite3.dbapi2 import PARSE_DECLTYPES


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path, detect_types=PARSE_DECLTYPES)
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


class TodoDatabaseConnector:
    """This class is responsible for connecting to the todo database."""

    def __init__(self, path):
        self.connection = create_connection(path)

    def execute_query(self, query, data_tuple=tuple()):
        cursor = self.connection.cursor()
        cursor.execute(query, data_tuple)
        self.connection.commit()
        return cursor

    def execute_read_query(self, query, data_tuple=tuple()):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query, data_tuple)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")


def get_last_todo_id():
    query = """
    SELECT todo_id from 'todos' ORDER BY todo_id DESC LIMIT 1;
    """
    return query


def insert_todo():
    query = """
    INSERT INTO 'todos'
        (user_input, time)
    VALUES
        (?, ?)
    ;
    """
    return query


def get_all_todos():
    query = """
    SELECT * from 'todos';
    """
    return query


def delete_todo_by_id():
    query = """
    DELETE FROM 'todos' WHERE todo_id = ?;
    """
    return query


def edit_todo_by_id():
    query = """
    UPDATE 'todos' SET user_input = ? WHERE todo_id = ?;
    """
    return query


def get_one_todo():
    query = """
    SELECT user_input FROM 'todos' WHERE todo_id = ?;
    """
    return query
