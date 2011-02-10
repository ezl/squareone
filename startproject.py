import fileinput
import sys

def replace_in_file(filename, search_exp, replace_exp):
    """http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python"""
    for line in fileinput.input(filename, inplace=1):
        if search_exp in line:
                line = line.replace(search_exp,replace_exp)
        sys.stdout.write(line)

replace_in_file("test.py", "squareone", "FOOOOOOOOOOOOOOOOO")

