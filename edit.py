# python main.py edit <ID>

from utilities import TodoDatabaseConnector, edit_todo_by_id, get_one_todo


def edit_todo(todo_database_connector: TodoDatabaseConnector, ID):
    original_todo = todo_database_connector.execute_read_query(get_one_todo(), (ID,))
    try:
        edited_input = input(
            f"The todo at id = {ID} is '{original_todo[0][0]}' Enter new todo:\n"
        )
    except IndexError:
        print("The Todo ID provided by the user does not exist.")
        return
    todo_database_connector.execute_query(edit_todo_by_id(), (edited_input, ID))
    print("Todo edited successfully")
