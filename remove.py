# python main.py remove <ID>
import utilities


def remove_todo(ID):
    json_data = utilities.load_data()
    found = False
    for todo in json_data:
        if todo["ID"] == ID:
            json_data.remove(todo)
            found = True
    if found:
        utilities.dump_data(json_data)
        print("Your Todo has been successfully removed.")
    else:
        print("The ID provided by the user does not exist.")
