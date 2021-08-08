# python main.py list_all


from utilities import TodoDatabaseConnector, get_all_todos


def list_all(todo_database_connector: TodoDatabaseConnector):
    result = todo_database_connector.execute_read_query(get_all_todos())
    if result == []:
        print("Your todo list is empty")
    else:
        for todo in result:
            print(f"ID: {todo[0]}")
            print(f"TODO: {todo[1]}")
            print(f"TIME: {todo[2]}")
            print()
