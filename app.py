import json
import os
import sys

products = {}


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def save_db(data, filename="data.json"):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_db(filename="data.json"):
    # If file does not exist, create it with empty dict
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

    # If file exists but is empty or invalid JSON, reset it
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        with open(filename, "w") as f:
            json.dump({}, f)
        return {}

products = load_db()



while True:
    clear_console()
    print("=== Inventory Management System ===")
    input()