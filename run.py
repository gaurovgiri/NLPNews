import sys
import subprocess

def run(argv):
    """
    Run different parts of your application based on the command line argument.

    Args:
        argv (list): A list of command-line arguments.

    Returns:
        int: 0 if successful, -1 if there's an error.

    Usage:
    - If you run the script with the argument "gui", it will start the GUI part of your application.
    - If you run the script with the argument "api", it will start the API part of your application.
    - If you provide an invalid argument, it will print an error message and return -1.
    - If you don't provide any arguments, it will print an error message.

    Examples:
    1. To start the GUI: python script.py gui
    2. To start the API: python script.py api
    3. Invalid argument: python script.py something_else
    4. Missing argument: python script.py
    """
    if len(argv) > 0:
        if argv[0] == "gui":
            subprocess.run("python -m gui", shell=True)
        elif argv[0] == "api":
            subprocess.run("uvicorn api.main:app --reload", shell=True)
        else:
            print("Invalid Argument: gui | api")
            return -1
    else:
        print("Invalid number of Arguments")
        return -1

if __name__ == "__main__":
    run(sys.argv[1:])
