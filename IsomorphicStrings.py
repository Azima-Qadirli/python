class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]].append(i) 
            else:
                dict1[s[i]] = [i]  
            
            if t[i] in dict2:
                dict2[t[i]].append(i) 
            else:
                dict2[t[i]] = [i]  
        
        for i in range(len(s)):
            if dict1[s[i]] != dict2[t[i]]:
                return False
        
        return True

        
        return True

    # We may write it as below

    #return len(set(zip(s, t))) == len(set(s)) == len(set(t))
        