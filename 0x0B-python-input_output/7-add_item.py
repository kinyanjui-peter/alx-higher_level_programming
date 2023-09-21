#!/usr/bin/python3
import sys
if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__(
        '6-load_from_json_file').load_from_json_file

# Check if "add_item.json" exists and load its content if it exists.
try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []

# Add command-line arguments to the existing data list.
arguments = sys.argv[1:]  # Exclude the script name itself.
existing_data.extend(arguments)

# Save the updated list to "add_item.json".
save_to_json_file(existing_data, "add_item.json")

#Arguments added and saved successfully to add_item.json.

