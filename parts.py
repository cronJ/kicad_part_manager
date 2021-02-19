import os
import yaml
import random

import part_class

def create_part_number(part_number_list):
    highest_number = 0

    for number in part_number_list:
        n = int(number[3:])
        if n > highest_number:
            highest_number = n

    return "PN-{}".format(str(highest_number + 1).zfill(13))

def list_all_part_numbers(part_folder, file_list):
    part_number_list = []

    for _, _, filenames in os.walk(part_folder):
        for filename in filenames:
            if filename in file_list:
                with open(os.path.join(part_folder, filename), 'r') as stream:
                    try:
                        parts = yaml.safe_load(stream)
                    except yaml.YAMLError as exc:
                        print(exc)
                
                for part in parts:
                    part_number_list.append(part)

    return part_number_list

def list_all_yaml_files(part_folder):
    file_list = []

    # Walk through the directory and check every file
    for _, _, filenames in os.walk(part_folder):
        for filename in filenames:
            # Check only for *.yaml files
            _, ext = os.path.splitext(filename)
            if ext == ".yaml":
                file_list.append(filename)

    return file_list

if __name__ == '__main__':

    # Get the current directory and attach the part_data folder
    yaml_directory = os.path.join(os.getcwd(), "part_data")

    yaml_files = list_all_yaml_files(yaml_directory)
    part_numbers = list_all_part_numbers(yaml_directory, yaml_files)

    part_number = create_part_number(part_numbers)

    print(part_number)