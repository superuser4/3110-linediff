import math
### algorithm
class SimilarityScore:
    line1 = ""
    line2 = ""
    left_context_vec = []
    right_context_vec = []

    def __init__(self,line1, line2, left_context_vec, right_context_vec):
        self.line1 = line1
        self.line2 = line2
        self.left_context_vec = left_context_vec
        self.right_context_vec= right_context_vec
    
    ## returns a float between 0.0 - 1.0 --> Similarity Score
    def lhdiff_check(self):
        dist = self.levenshtein_distance()
        max_len = max(len(self.line1), len(self.line2))
        lev_sim = 1- (dist / max_len) if max_len >0 else 1.0
        comb_sim = 0.6 * lev_sim+ 0.4 * self.cosine_similarity()
        return comb_sim

    def levenshtein_distance(self):
        m, n = len(self.line1), len(self.line2)
        D = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m+1):
            D[i][0] = i
        for j in range(n+1):
            D[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if self.line1[i-1] == self.line2[j-1]:
                    cost = 0
                else:
                    cost = 1
                D[i][j] = min(
                        D[i-1][j] +1,
                        D[i][j-1] + 1,
                        D[i-1][j-1] + cost,
                )
        return D[m][n]
    
    # 3 lines for both vec
    def cosine_similarity(self):
       comb_vocab = []
       old_chunk = ""
       new_chunk = ""

       for line1, line2 in zip(self.left_context_vec, self.right_context_vec):
           local_vocab = line1.split()
           old_chunk += " ".join(local_vocab) + " "
           comb_vocab += local_vocab

           local_vocab2 = line2.split()
           new_chunk += " ".join(local_vocab2) + " "
           comb_vocab += local_vocab2

       comb_vocab = list(set(comb_vocab))

       old_chunk_vec = [0] * len(comb_vocab)
       for vocab_idx in range(len(comb_vocab)):
           for word in old_chunk.split():
               if comb_vocab[vocab_idx] == word: 
                   old_chunk_vec[vocab_idx] += 1
       new_chunk_vec = [0] * len(comb_vocab)
       for vocab_idx in range(len(comb_vocab)):
           for word in new_chunk.split():
               if comb_vocab[vocab_idx] == word:
                   new_chunk_vec[vocab_idx] += 1
       
       ### Computing dot product of two vectors
       dot = 0
       for i,j in zip(old_chunk_vec, new_chunk_vec):
           dot += i * j
       
       ### Compute the magnitude of each vec
       old_magn = 0
       for i in old_chunk_vec:
           old_magn += i * i
       old_magn = math.sqrt(old_magn) 

       new_magn = 0
       for i in new_chunk_vec:
           new_magn += i * i
       new_magn = math.sqrt(new_magn)

       ### Divide dot product by product of magnitudes
       if old_magn == 0 or new_magn == 0:
           sim = 0.0
       else:
          sim = dot / (abs(old_magn) * abs(new_magn))
       return sim
    
    
    def hamming_distance(a: str, b: str) -> int:
    #Takes two strings, counts the difference and returns the answers as an Int
    #Strings do not have to be the same length, if one string is longer than blanks will count as differences
    #Example 1: a = 1111 , b = 1100, answer = 2
    #Example 2: a = 11111, b = 1100, answer = 3
        answer = 0

        if len(a) != len(b):
            
            if(len(a) > len(b)):
                    tempB = b
                    temp = len(b)

                    while temp != len(a):
                            tempB += "2"
                            temp +=1
                    b = tempB
            else:
                    tempA = a
                    temp = len(a)

                    while temp != len(b):
                            tempA += "2"
                            temp +=1
                    a = tempA
        
        index = 0

        for char in a:
                if char != b[index]:
                    answer += 1
                index +=1

        return answer
