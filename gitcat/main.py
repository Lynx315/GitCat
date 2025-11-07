import sys
from gitcat import operations

COMMAND_LIST = operations.COMMAND_LIST

UserInput = input("Enter command: ")

def dispatcher():
    command = sys.argv[1] 
    arguments = sys.argv[2:]

    if command in COMMAND_LIST:
        COMMAND_LIST[command](*arguments)
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    dispatcher()


