class SimHash():
    line1 = ""
    line2 = ""
    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
    def hamming_distance(self) -> int:
    #Takes two strings, counts the difference and returns the answers as an Int
    #Strings do not have to be the same length, if one string is longer than blanks will count as differences
    #Example 1: a = 1111 , b = 1100, answer = 2
    #Example 2: a = 11111, b = 1100, answer = 3
        answer = 0

        if len(self.line1) != len(self.line2):
            
            if(len(self.line1) > len(self.line2)):
                    tempB = self.line2
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
