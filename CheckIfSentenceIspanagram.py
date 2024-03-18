class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        sentence = sentence.lower()
        letters =set()
        for char in sentence:
            if char.isalpha():
                letters.add(char)
        return len(letters)==26

    #or
        
        
        #return(len(set(sentence))==26)
