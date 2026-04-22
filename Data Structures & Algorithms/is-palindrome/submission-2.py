class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=''
        for ch in s:
            if ch.isalnum():
                temp += ch
        i,j = 0, len(temp) - 1
        print(temp)
        temp = temp.lower()

        while i < j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        return True