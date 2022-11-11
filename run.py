import sys
import subprocess

def run(argv):
    if len(argv) > 0:
        if argv[0] == "gui":
            subprocess.run("python -m gui",shell=True)
        elif argv[0] == "api":
            subprocess.run("uvicorn api.main:app --reload",shell=True)
        else:
            print("Invalid Argument: gui | api")
            return -1
    else:
        print("Invalid number of Arguments")

if __name__ == "__main__":
    run(sys.argv[1:])