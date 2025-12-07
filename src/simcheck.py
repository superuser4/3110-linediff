from os import _exit 

class SimilarityChecker:
    file1 = ""
    file2 = ""

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def file_parser(self):
        try:
            lin1 = open(self.file1).readlines()
            lin1 = [s.strip() for s in lin1]

            lin2 = open(self.file2).readlines()
            lin2 = [s.strip() for s in lin2]
        except IOError as e:
            print("Error: " + str(e))
            _exit(1)
        return lin1, lin2


    def line_comp(self):
        file1_lines, file2_lines = self.file_parser()
        hash_map = {}
        used_file2 = set()
        
        for i in range(len(file1_lines)):
            left_context_vec = []
            right_context_vec = []

            for j in range(len(file2_lines)):
                if j in used_file2:
                    break
                if file1_lines[i] == file2_lines[j]:
                    if file1_lines[i] == "":
                        continue
                    
                    hash_map[i+1] = j+1
                    break
        

        return hash_map
    def check(self):
        hash_map = self.line_comp()
        print("Line matches:")
        for key, val in hash_map.items():
            print(f"{key} - {val}")


