from os import _exit 
import diff 

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


    def line_comp(self, similar_threshold=0.8):
        file1_lines, file2_lines = self.file_parser()
        hash_map = {}
        used_file2 = set()
        
        for i, line1 in enumerate(file1_lines):
            if line1 == "":
                continue
            for j, line2 in enumerate(file2_lines):
                if j in used_file2:
                    continue
                if line1==line2:
                    hash_map[i+1] = j+1
                    used_file2.add(j)
                    break

        ### For approximate matches
        for i, line1 in enumerate(file1_lines):
            ## alr matched or empty line
            if (i+1) in hash_map or line1== "":
                continue
            
            best_j = None
            best_scor = 0
           
            j = i
            if i > 5:
                j -= 5
            else:
                j-=i
            while True:
                if j > i+5:
                    break

                left_context_file1 = file1_lines[max(0, i-1):i]
                right_context_file1 = file1_lines[i+1:min(len(file1_lines), i+2)]

                score_o = diff.SimilarityScore(
                        line1=line1,
                        line2=line2,
                        left_context_vec=left_context_file1,
                        right_context_vec=right_context_file1
                )
                sim_score = score_o.lhdiff_check()
                if sim_score > best_scor:
                    best_scor = sim_score
                    best_j = j
                j += 1

            if best_j is not None and best_scor >= similar_threshold:
                hash_map[i+1] = best_j+1
                used_file2.add(best_j)
        return hash_map

    
         
    def check(self):
        hash_map = self.line_comp()
        print("Line matches:")
        for key, val in hash_map.items():
            print(f"{key} - {val}")


