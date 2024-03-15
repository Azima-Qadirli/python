class Solution:
    def mostCommonWord(self, paragraph: str, banned:str) -> str:
        import re
        from collections import Counter
        
        # Replace punctuations with spaces and convert to lowercase
        words = re.findall(r'\w+', paragraph.lower())
        
        # Count word frequencies excluding banned words
        word_count = Counter(word for word in words if word not in banned)
        
        # Find the most common word
        return max(word_count, key=word_count.get)
