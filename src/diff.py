### algorithm
class SimilarityScore:
    line1 = ""
    line2 = ""

    def __init__(self,line1, line2):
        self.line1 = line1
        self.line2 = line2
    
    ## returns a float between 0.0 - 1.0 --> Similarity Score
    def lhdiff_check(self):
        ## Formula
        ## comb_sim = 0.6 * levenshtein_distance(left, right) + 0.4 * cosine_similarity(left_vec, right_vec)

    def levenshtein_distance(left, right):
        None

    def cosine_similarity(left_context_vec, right_context_vec):
        None
