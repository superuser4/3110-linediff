from os import _exit
import sys
import simcheck

def main():
    if len(sys.argv) < 2:
        print("Error you must pass 2 files to compare e.g. (./main.py file1 file2)")
        _exit(1)
    
    checker = simcheck.SimilarityChecker(sys.argv[1], sys.argv[2])
    checker.check()
    
if __name__ == "__main__":
    main()
