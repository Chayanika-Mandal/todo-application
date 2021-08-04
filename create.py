import json
from datetime import datetime

from utilities import load_data

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


def add_todo(user_input):
    json_data = load_data()
    if json_data == []:
        new_id = 1
    else:
        for todo in json_data:
            if user_input == todo["user_input"]:
                print("This todo already exists.")
                return
            else:
                new_id = json_data[-1]["ID"] + 1
    current_time = datetime.now().strftime(r"%H:%M, %d/%m/%Y")
    new_todo = {
        "ID": new_id,
        "time": current_time,
        "user_input": user_input,
    }
    json_data.append(new_todo)

    with open("data.json", "w") as data:
        json.dump(json_data, data, indent=4)

    print("Your todo was stored successfully")
