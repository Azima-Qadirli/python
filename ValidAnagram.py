class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if  len(s) != len(t):
            return False

        dict = {}

        for char in s:
            dict[char] = dict.get(char,0) + 1

        for char in t:
            if char not in dict or dict[char] == 0:
                return False
            dict[char] -= 1


        return True 