from os import _exit 
import diff 
import simhash

class SimilarityChecker:
    file1 = ""
    file2 = ""

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def build_context(self, lines, idx, window=2):
        start = max(0, idx - window)
        end = min(len(lines), idx + window + 1)
        context = [lines[k] for k in range(start, end) if k != idx]
        return context

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

        #1️⃣ Exact matches
        for i, line1 in enumerate(file1_lines):
            if not line1.strip():
                continue
            for j, line2 in enumerate(file2_lines):
                if j in used_file2:
                    continue
                if line1 == line2:
                    hash_map[i+1] = j+1
                    used_file2.add(j)
                    break

        # Approx matches using SimHash + similarity
        for i, line1 in enumerate(file1_lines):
            if (i+1) in hash_map or not line1.strip():
                continue
            # SimHash Hamming distances
            hamminged_map = {}
            for j, line2 in enumerate(file2_lines):
                if j in used_file2:
                    continue
                simhasher = simhash.SimHash(line1, line2)
                hamminged_map[j] = simhasher.hamming_distance()

            # Top 15 candidates
            candidates = sorted(hamminged_map.items(), key=lambda x: x[1])[:15]

            best_score = -1.0
            best_loc = None
            for (j, _) in candidates:
                left_vec  = self.build_context(file1_lines, i)
                right_vec = self.build_context(file2_lines, j)
                line2 = file2_lines[j]
                score_obj = diff.SimilarityScore(line1, line2, left_vec, right_vec)
                sim_score = score_obj.lhdiff_check()

                if sim_score > best_score:
                    best_score = sim_score
                    best_loc = j

            if best_loc is not None and best_score >= similar_threshold:
                hash_map[i+1] = best_loc + 1
                used_file2.add(best_loc)

        return hash_map
     
    def check(self):
        hash_map = self.line_comp()
        print("Line matches:")
        for key, val in hash_map.items():
            print(f"{key} - {val}")


