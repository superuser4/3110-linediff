class SimHash():
    line1 = ""
    line2 = ""
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
    
    def str_to_hash(self, string):
    def bit_simhash(self, string):
    def xor_hamming_dist(self):
        hash1 = self.bit_simhash(self.line1)
        hash2 = self.bit_simhash(self.line2)
        
        xor = hash1 ^ hash2
        
        total = 0
        while xor:
            total += 1
            x &= x -1
        return total


    def hamming_distance(self) -> int:
        #Takes two strings, counts the difference and returns the answers as an Int
        #Strings do not have to be the same length, if one string is longer than blanks will count as differences
        #Example 1: a = 1111 , b = 1100, answer = 2
        #Example 2: a = 11111, b = 1100, answer = 3
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
