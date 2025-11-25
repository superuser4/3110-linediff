### algorithm
class SimilarityScore:
    line1 = ""
    line2 = ""
    context_vec = []

    def __init__(self,line1, line2):
        self.line1 = line1
        self.line2 = line2
    
    ## returns a float between 0.0 - 1.0 --> Similarity Score
    def lhdiff_check(self):
        None
    ## Context gather 4 lines around the line
