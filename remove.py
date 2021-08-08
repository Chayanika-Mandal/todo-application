# python main.py remove <ID>


from utilities import TodoDatabaseConnector, delete_todo_by_id


def remove_todo(todo_database_connector: TodoDatabaseConnector, ID):
    cursor = todo_database_connector.execute_query(delete_todo_by_id(), (ID,))
    if cursor.rowcount == 1:
        print("Your todo has been successfully removed.")
    else:
        print("The ID provided by the user does not exist.")
