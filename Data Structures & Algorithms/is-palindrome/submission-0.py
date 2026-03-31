class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""

        for ch in s:
            if ch.isalnum():
                cleanStr += ch.lower()

        left = 0
        right = len(cleanStr) - 1

        while left < right:
            if cleanStr[left] != cleanStr[right]:
                return False
            else:
                left +=1
                right -=1
        return True
                
            