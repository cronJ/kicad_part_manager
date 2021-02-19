import pytest
import os
import sys
import inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 

import parts

class TestClass:
    def test_part_number(self):
        yaml_directory = os.path.join(os.getcwd(), "part_data")
        yaml_files = parts.list_all_yaml_files(yaml_directory)
        part_numbers = parts.list_all_part_numbers(yaml_directory, yaml_files)

        part_number = parts.create_part_number(part_numbers)

        assert "PN-0000000000004" in part_number