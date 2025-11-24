
from os import _exit 
import sys

def file_opener(file1, file2):
    try:
        fd1 = open(file1)
        fd2 = open(file2)
    except IOError as e:
        print("Error: " + str(e))
        _exit(1)
    return fd1, fd2


def basic_line_comp(file1, file2):
    fd1, fd2 = file_opener(file1, file2)

    try:
        file1_lines = fd1.readlines()
        file2_lines = fd2.readlines()
    except IOError as e:
        print("Error: " + str(e))
        _exit(1)

    hash_map = {}
    for i in range(len(file1_lines)):
        try:
            if file1_lines[i] == file2_lines[i]:
                hash_map[i] = i
        except IndexError:
            # one file is shorter in length than another
            break
    return hash_map

def main():
    if len(sys.argv) < 2:
        print("Error you must pass 2 files to compare e.g. (./main.py file1 file2)")
        _exit(1)
    hash_map = basic_line_comp(sys.argv[1], sys.argv[2])
    print("Line matches:")
    for key, val in hash_map.items():
        print(f"{key} - {val}")


if __name__ == "__main__":
    main()
