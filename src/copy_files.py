import os
import shutil
from pathlib import Path

def copy_files(base_file_path):
    log = []

    # find working directories
    target_file_path = os.path.join(base_file_path, "public")
    host_file_path = os.path.join(base_file_path, "static")

    # check if public directory exists and delete
    if test_file_path_exists(target_file_path) == True:
        shutil.rmtree(target_file_path)
        if test_file_path_exists(target_file_path) == False:
            log.append(f"public directory deleted {target_file_path}")

    # create public directory
    os.mkdir(target_file_path)
    if test_file_path_exists(target_file_path):
        log.append(f"public directory created {target_file_path}")

    # test host directory
    if test_file_path_exists(host_file_path):
        copy_assist(host_file_path, target_file_path, log)

    # print log to terminal for debugging
    #for input in log:
    #    print (input)

def test_file_path_exists(file_path):
    return os.path.exists(file_path)

def copy_assist(file_path, target, log):
    contents = os.listdir(file_path)
    for content in contents:
        path = os.path.join(file_path, content)
        if os.path.isfile(path) == True:
            shutil.copy(path, target)
            log.append(f"copied file {content} to directory {target}")
        elif os.path.isdir(path) == True:
            new_target = os.path.join(target, content)
            os.mkdir(new_target)
            if test_file_path_exists(new_target) == True:
                log.append(f"directory created {new_target}")
                copy_assist(path, new_target, log)
        else:
            log.append(f"Error: content neither file or directory {path}")

if __name__ == "__main__":
    copy_files()