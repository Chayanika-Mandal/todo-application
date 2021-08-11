import sys
from edit import edit_todo
from create import add_todo
from list_all import list_all
from remove import remove_todo
from utilities import TodoDatabaseConnector

action = sys.argv[1]

todo_database_connector = TodoDatabaseConnector("todo.db")


# we need to always create the table incase it does not exists
create_todo_schema = """
CREATE TABLE IF NOT EXISTS 'todos' (
    todo_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_input TEXT NOT NULL,
    time TIMESTAMP NOT NULL
);
"""
todo_database_connector.execute_query(create_todo_schema)


if action == "remove":
    remove_todo(todo_database_connector, int(sys.argv[2]))
if action == "list_all":
    list_all(todo_database_connector)
elif action == "create":
    add_todo(todo_database_connector, sys.argv[2])
if action == "edit":
    edit_todo(todo_database_connector, int(sys.argv[2]))
