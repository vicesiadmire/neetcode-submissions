class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(''.join(sorted(s)))
        
        #can just compare the two sorted strings
        return sorted(s) == sorted(t)
        
        #OG solution
        #return True if ''.join(sorted(s)) == ''.join(sorted(t)) else False
        
        
        #I misunderstood the ask - this works to flip
        ## the string to compare whether a string is a
        ### palindromes True if s[::-1] == s else False
        