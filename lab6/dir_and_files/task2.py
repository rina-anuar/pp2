import os

def check_path_access(path):
    print(f"Path: {path}")
    print(f"Existence: {os.path.exists(path)}")
    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")


specified_path = "/Users/rinaanuar/Desktop/pp2/pp2/lab6/dir_and_files/task1.py"
check_path_access(specified_path)