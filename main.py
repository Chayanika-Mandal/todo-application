import json
from datetime import datetime
# Json has four important functions: json.load, json.loads, json.dump, json.dumps
user_input = "Take your dog out for a walk."
# First of all, you have to store the user's input. Secondly, the time in which the input was given. Lastly, an ID.
# The data should be stored something like this:
# [
#     {
#         "ID": 1,
#         "user_input": "Take your dog out for a walk.",
#         "time": "20:29, 31/07/2021"
#     }
# ]
with open("data.json", "r") as data:
    json_data = json.load(data)
    new_id = json_data[-1]["ID"] + 1
    current_time = datetime.now().strftime(r"%H:%M, %d/%m/%Y")
    new_todo = {"ID": new_id, "time": current_time, "user_input": user_input}
    json_data.append(new_todo)


with open("data.json", "w") as data:
    json.dump(json_data, data, indent=4)
