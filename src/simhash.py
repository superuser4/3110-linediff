import re
import hashlib

class SimHash():
    line1 = ""
    line2 = ""
    
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
    
    def tokenize(self, text: str) -> list[str]:
        """Simpler, more robust tokenizer"""
        if not text:
            return []
    
        # Simple: split by whitespace and keep punctuation as separate tokens
        tokens = re.findall(r'\b\w+\b|\S', text)  # \w+ for words, \S for punctuation
        return tokens
    
    def compute_hash(self, text: str) -> int:
        """Compute and return the SimHash value (64-bit integer), NOT the distance"""
        tokens = self.tokenize(text)
        if not tokens:
            return 0
        
        v = [0] * 64
        
        for token in tokens:
            h = int(hashlib.md5(token.encode()).hexdigest()[:16], 16)
            for i in range(64):
                if h & (1 << i):
                    v[i] += 1
                else:
                    v[i] -= 1
        
        # Convert to binary fingerprint
        fp = 0
        for i in range(64):
            if v[i] > 0:
                fp |= (1 << i)
        return fp
    
    def xor_hamming_dist(self):
        """Calculate Hamming distance between two SimHash values"""
        # First compute the SimHash for each line
        hash1 = self.compute_hash(self.line1)
        hash2 = self.compute_hash(self.line2)
        
        # Then calculate Hamming distance
        xor = hash1 ^ hash2
        total = 0
        while xor:
            total += 1
            xor &= xor - 1
        return total
    
    def hamming_distance(self) -> int:
        answer = 0
        if len(self.line1) != len(self.line2):
            if(len(self.line1) > len(self.line2)):
                tempB = self.line2
                temp = len(self.line2)
                while temp != len(self.line1):
                    tempB += "2"
                    temp +=1
                self.line2 = tempB
            else:
                tempA = self.line1
                temp = len(self.line1)
                while temp != len(self.line2):
                    tempA += "2"
                    temp +=1
                self.line1 = tempA
        
        index = 0
        for char in self.line1:
            if char != self.line2[index]:
                answer += 1
            index +=1
        return answer
