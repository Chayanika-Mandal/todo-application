# python main.py list_all


from utilities import load_data


def list_all():
    json_data = load_data()
    if json_data == []:
        print("Your todo list is empty")
    else:
        for todo in json_data:
            print(f"ID: {todo['ID']}")
            print(f"TODO: {todo['user_input']}")
            print(f"TIME: {todo['time']}")
            print()
