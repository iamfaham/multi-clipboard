import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_data(filepath, data):
    with open(filepath,'w') as f:
        json.dump(data,f)

def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}
    
def delete_data(key):
    if key in data:
        data.pop(key)
        return data
    else:
        print("Key not found!")


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)
    
    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data copied to clipboard")
        else:
            print("Key does not exist!")

    elif command == "list":
        print(data)

    elif command == "del":
        key = input("Enter a key: ")
        delete_data(key)
        save_data(SAVED_DATA, data)

    else:
        print('Please pass only one and correct argument!')