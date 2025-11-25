### algorithm
class SimilarityScore:
    line1 = ""
    line2 = ""

    def __init__(self,line1, line2):
        self.line1 = line1
        self.line2 = line2
    
    ## returns a float between 0.0 - 1.0 --> Similarity Score
    #def lhdiff_check(self, left, right):
        ## Formula
        ## comb_sim = 0.6 * levenshtein_distance(left, right) + 0.4 * cosine_similarity(left_vec, right_vec)

    #def levenshtein_distance(self,left, right):
    
    # 3 lines for both vec
    def cosine_similarity(self, left_context_vec, right_context_vec):
       comb_vocab = []
       old_chunk = ""
       new_chunk = ""

       for line1, line2 in zip(left_context_vec, right_context_vec):
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

       ### Divide dot product by product of magnitudes


