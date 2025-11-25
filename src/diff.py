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
    #def lhdiff_check(self):
        ## Formula
        ## comb_sim = 0.6 * levenshtein_distance() + 0.4 * cosine_similarity()

    #def levenshtein_distance(self):
    
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
       sim = dot / (abs(old_magn) * abs(new_magn))
       return sim

