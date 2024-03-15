class Solution:
    def countConsistentStrings(self, allowed: str, words:str) -> int:
        count= len(words)
        for i in words:
            for j in i:
                if j not in allowed:
                    count -=1
        return count 