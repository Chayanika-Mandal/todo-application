# python main.py list_all
import utilities


def list_all():
    json_data = utilities.load_data()
    for todo in json_data:
        print(todo)


list_all()
