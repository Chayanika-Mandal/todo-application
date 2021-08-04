import sys

from create import add_todo
from list_all import list_all
from remove import remove_todo

action = sys.argv[1]

if action == "remove":
    remove_todo(int(sys.argv[2]))
elif action == "list_all":
    list_all()
elif action == "create":
    add_todo(sys.argv[2])
