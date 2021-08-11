from datetime import datetime
from sqlite3.dbapi2 import IntegrityError

from utilities import TodoDatabaseConnector, insert_todo

# Json has four important functions: json.load, json.loads, json.dump,
# json.dumps First of all, you have to store the user's input. Secondly, the
# time in which the input was given. Lastly, an ID. The data should be stored
# something like this:
# [
#     {
#         "ID": 1,
#         "user_input": "Take your dog out for a walk.",
#         "time": "20:29, 31/07/2021"
#     }
# ]
# python main.py create "Take the dog out for a walk." these are command-line
# arguments.


def add_todo(todo_database_connector: TodoDatabaseConnector, user_input: str):
    current_time = datetime.now()
    data_tuple = (user_input, current_time)
    try:
        todo_database_connector.execute_query(insert_todo(), data_tuple)
    except IntegrityError:
        print("This todo already exists")
        return
    print("Your todo was stored successfully")
