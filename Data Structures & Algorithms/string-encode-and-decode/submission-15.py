class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res += str(len(i)) + "#" + i
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Find the position of '#'
            j = i
            while j < len(s) and s[j] != '#':
                j += 1
            
            # If we reached the end without finding '#', break
            if j >= len(s):
                break
                
            # Extract the length
            word_length = int(s[i:j])
            
            # Extract the word
            word = s[j+1 : j+1+word_length]
            result.append(word)
            
            # Move to the next encoded string
            i = j + 1 + word_length
        
        return result