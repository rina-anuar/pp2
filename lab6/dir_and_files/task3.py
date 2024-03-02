import os

def test_exists(path):
    if os.path.exists(path):
        print("Path exists.")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("Path does not exist.")

specified_path = "/Users/rinaanuar/Desktop/pp2/pp2/lab6/task2.py"
test_exists(specified_path)