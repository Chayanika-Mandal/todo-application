# python main.py remove <ID>


from utilities import dump_data, load_data


def remove_todo(ID):
    json_data = load_data()
    found = False
    for todo in json_data:
        if todo["ID"] == ID:
            json_data.remove(todo)
            found = True
    if found:
        dump_data(json_data)
        print("Your Todo has been successfully removed.")
    else:
        print("The ID provided by the user does not exist.")
