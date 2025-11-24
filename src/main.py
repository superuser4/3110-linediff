
from os import _exit 
import sys

class SimilarityChecker:
    file1 = ""
    file2 = ""

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def file_parser(self):
        try:
            lin1 = open(self.file1).readlines()
            lin2 = open(self.file2).readlines()
        except IOError as e:
            print("Error: " + str(e))
            _exit(1)
        return lin1, lin2


    def basic_line_comp(self):
        file1_lines, file2_lines = self.file_parser()
        hash_map = {}
        for i in range(len(file1_lines)):
            try:
                if file1_lines[i] == file2_lines[i]:
                    hash_map[i] = i
            except IndexError:
                # one file is shorter in length than another
                break
        return hash_map
    def parse(self):
        hash_map = self.basic_line_comp()
        print("Line matches:")
        for key, val in hash_map.items():
            print(f"{key} - {val}")


def main():
    if len(sys.argv) < 2:
        print("Error you must pass 2 files to compare e.g. (./main.py file1 file2)")
        _exit(1)
    
    checker = SimilarityChecker(sys.argv[1], sys.argv[2])
    checker.parse()
    
if __name__ == "__main__":
    main()
