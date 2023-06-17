#!/usr/bin/python3
"""Module of script that adds all arguments to a Python list,
and then save them to a file."""
from sys import argv


load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

try:
    json_data = load_file('add_item.json')
except (ValueError, FileNotFoundError):
    json_data = []

for items in argv[1:]:
    json_data.append(items)

save_file(json_data, 'add_item.json')
