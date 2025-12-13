from os import _exit 
import diff 
import simhash
import re

class SimilarityChecker:
    file1 = ""
    file2 = ""
    sim_thres = 0.6

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def build_context(self, lines, idx, window=3):
        start = max(0, idx - window)
        end = min(len(lines), idx + window + 1)
        context = [lines[k] for k in range(start, end) if k != idx]
        return context

    def normalize_line(self,line: str) -> str:
        line=line.strip()
        line=re.sub(r"\s+", " ", line)
        line=re.sub(r"\s*([=+\-*/<>!]+)\s*", r"\1 ", line)
        line=re.sub(r"\s+", " ", line)
        return line
    
    def file_parser(self):
        try:
            with open(self.file1, "r", encoding='utf-8', errors='ignore') as f1:
                lines1 = f1.readlines()
            with open(self.file2, "r", encoding='utf-8', errors='ignore') as f2:
                lines2 = f2.readlines()
        except IOError as e:
            print("Error loading file:", str(e))
            _exit(1)
    
        # Normalize but preserve empty lines as placeholders
        normalized1 = []
        normalized2 = []
        
        for line in lines1:
            norm = self.normalize_line(line)
            # Keep empty lines but mark them
            if not norm.strip():
                normalized1.append("")  # Empty placeholder
            else:
                normalized1.append(norm)
        
        for line in lines2:
            norm = self.normalize_line(line)
            if not norm.strip():
                normalized2.append("")
            else:
                normalized2.append(norm)
        
        return normalized1, normalized2

    def compute_hashes(self, lines):
        content_hashes = []
        context_hashes = []
        
        for i, line in enumerate(lines):
            # Content hash
            content_hash = simhash.SimHash(line, "").compute_hash(line)
            content_hashes.append(content_hash)
            
            # Context hash
            context_lines = self.build_context(lines, i)
            context_text = " ".join(context_lines)
            context_hash = simhash.SimHash(context_text, "").compute_hash(context_text)
            context_hashes.append(context_hash)
            
        return content_hashes, context_hashes

    def calculate_adaptive_threshold(self, old_lines, new_lines):
        old_nonblank = sum(1 for line in old_lines if line.strip())
        new_nonblank = sum(1 for line in new_lines if line.strip())
    
        # If one file has way more lines, be more permissive
        ratio = min(old_nonblank, new_nonblank) / max(old_nonblank, new_nonblank)
    
        if ratio < 0.5:  # Files very different in size
            self.sim_thres = 0.5
    
        if old_nonblank < 10 or new_nonblank < 10:
            self.sim_thres = 0.65
    
        self.sim_thres = 0.55
    def line_comp(self):
        file1_lines, file2_lines = self.file_parser()
        self.calculate_adaptive_threshold(file1_lines, file2_lines)
        hash_map = {}
        used_file2 = set()

        # Phase 1: Compute SimHashes for all lines
        f1_content_hashes, f1_context_hashes = self.compute_hashes(file1_lines)
        f2_content_hashes, f2_context_hashes = self.compute_hashes(file2_lines)

        # Phase 2: Exact matches first
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

        # Phase 3: Use SimHash to find candidate matches
        for i, line1 in enumerate(file1_lines):
            if (i+1) in hash_map or not line1.strip():
                continue

            # find top 15
            candidates = []
            for j, line2 in enumerate(file2_lines):
                if j in used_file2:
                    continue
                    
                content_hamming = self.hamming_dist(f1_content_hashes[i], f2_content_hashes[j])
                context_hamming = self.hamming_dist(f1_context_hashes[i], f2_context_hashes[j])
                combined_hamming = 0.6 * content_hamming + 0.4 * context_hamming
                
                candidates.append((j, combined_hamming))
            
            # sort by hamming dist and take top 15 cands 
            candidates.sort(key=lambda x: x[1])
            top_candidates = [j for j, _ in candidates[:15]]
            
            # Phase 4: Detailed comparison on top candidates
            best_score = -1.0
            best_loc = None
            is_split = False
            split_lines = []
            
            for j in top_candidates:
                if j in used_file2:
                    continue
                
                # Check single line match
                left_vec = self.build_context(file1_lines, i)
                right_vec = self.build_context(file2_lines, j)
                score_obj = diff.SimilarityScore(line1, file2_lines[j], left_vec, right_vec)
                sim_score = score_obj.lhdiff_check()
                
                if sim_score > best_score:
                    best_score = sim_score
                    best_loc = j
                    is_split = False
                
                # Check line splitting (1-4 lines)
                for k in range(1, 4):
                    if j + k >= len(file2_lines):
                        break
                    
                    merged_line = " ".join(file2_lines[j:j+k+1])
                    split_score_obj = diff.SimilarityScore(line1, merged_line, left_vec, right_vec)
                    split_score = split_score_obj.lhdiff_check()
                    
                    if split_score > best_score:
                        best_score = split_score
                        best_loc = j
                        is_split = True
                        split_lines = list(range(j, j+k+1))
                

            if best_loc is not None and best_score >= self.sim_thres:
                if is_split and split_lines:
                    # Map to first line of split
                    hash_map[i+1] = split_lines[0] + 1
                    # Mark all split lines as used
                    for line_num in split_lines:
                        used_file2.add(line_num)
                else:
                    hash_map[i+1] = best_loc + 1
                    used_file2.add(best_loc)

        return hash_map
    
    def hamming_dist(self, hash1, hash2):
        """Calculate Hamming distance between two integers"""
        xor = hash1 ^ hash2
        total = 0
        while xor:
            total += 1
            xor &= xor - 1
        return total
     
    def check(self):
        hash_map = self.line_comp()
        print("Line matches:")
        for key, val in hash_map.items():
            print(f"{key} - {val}")
