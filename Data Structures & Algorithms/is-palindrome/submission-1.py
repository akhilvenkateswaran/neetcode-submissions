class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1

        while start < end:
            while start < end and not(self.isAlphaNum(s[start])):
                start += 1
            while end > start and not(self.isAlphaNum(s[end])):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start +=1
            end -= 1
        return True
    
    def isAlphaNum(self, i:str) -> bool:
        return ((ord(i) >= 48 and ord(i) <= 57) or
                (ord(i) >= 65 and ord(i) <= 90) or
                (ord(i) >= 97 and ord(i) <= 122))
            
            