import json
from json.decoder import JSONDecodeError


def load_data():
    """This function is supposed to return the data from the data.json file as
    a python object."""
    with open("data.json", "r") as data:
        try:
            json_data = json.load(data)
        except JSONDecodeError:
            json_data = []
    return json_data


def dump_data(json_data):
    """This function is supposed to write data to the json file."""
    with open("data.json", "w") as data:
        json.dump(json_data, data, indent=4)
