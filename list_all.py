# python main.py list_all
import utilities


def list_all():
    json_data = utilities.load_data()
    for todo in json_data:
        print(f"ID: {todo['ID']}\nTODO: {todo['user_input']}\nTIME: {todo['time']}\n")


list_all()
