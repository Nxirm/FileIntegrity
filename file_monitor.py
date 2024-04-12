import hashlib
import os
import json
import time
from datetime import datetime
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logo =f"""{colors.HEADER}
-----------------------------------------------------------------------------------------------
 ________ .-./`) ,---.    ,---. 
|        |\ .-.')|    \  /    | 
|   .----'/ `-' \|  ,  \/  ,  | 
|  _|____  `-'`"`|  |\_   /|  | 
|_( )_   | .---. |  _( )_/ |  | 
(_ o._)__| |   | | (_ o _) |  | 
|(_,_)     |   | |  (_,_)  |  | 
|   |      |   | |  |      |  | 
'---'      '---' '--'      '--' 
{colors.ENDC}"""
def get_directories_to_monitor():
    directories = []
    while True:
        directory_path = input(f"{colors.OKBLUE}Enter a directory path to monitor (leave blank to finish): {colors.ENDC}").strip()
        if directory_path:
            directories.append(directory_path)
        else:
            break
    return directories

def generate_hashes(directory):
    file_info = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                file_hash = hashlib.sha256(f.read()).hexdigest()
                last_modified_time = os.path.getmtime(file_path)
                file_info[file_path] = {
                    "hash": file_hash,
                    "last_modified": datetime.fromtimestamp(last_modified_time).isoformat()
                }
    return file_info
def monitor_changes(directories):
    file_info = {}
    for directory in directories:
        file_info.update(generate_hashes(directory))

    while True:
        updated_file_info = {}
        for directory in directories:
            for root, dirs, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        current_hash = hashlib.sha256(f.read()).hexdigest()
                        last_modified_time = os.path.getmtime(file_path)
                        current_modified_time = datetime.fromtimestamp(last_modified_time).isoformat()

                        if file_path in file_info:
                            if current_hash != file_info[file_path]["hash"]:
                                print(f"File '{file_path}' has been modified since {file_info[file_path]['last_modified']}!")
                        else:
                            print(f"New file detected: '{file_path}'")
                        updated_file_info[file_path] = {
                            "hash": current_hash,
                            "last_modified": current_modified_time
                        }
        file_info = updated_file_info

        # Sleep for a specified interval (e.g., 60 seconds)
        time.sleep(60)
if __name__ == "__main__": 
    print(logo)
    print(f"{colors.HEADER}File Integrity Monitor{colors.ENDC}")
    print(f"{colors.HEADER}~NupurBhosle{colors.ENDC}")
    print(f"{colors.HEADER}----------------------------------------------------------------------------------------------{colors.ENDC}")
    print(f"{colors.OKBLUE}Enter directory paths to monitor (press Enter with no input to finish){colors.ENDC}")
    directories_to_monitor = get_directories_to_monitor()

    try:
        monitor_changes(directories_to_monitor)

    except KeyboardInterrupt:
        print(f"{colors.FAIL}\nFile Integrity Monitoring script terminated.{colors.ENDC}")
