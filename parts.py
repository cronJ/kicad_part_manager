import os

import yaml

yaml_directory = os.path.join(os.getcwd(), "part_data")

for _, _, filenames in os.walk(yaml_directory):
    for filename in filenames:
        yaml_data = yaml.load(filename)