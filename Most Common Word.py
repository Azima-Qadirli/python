class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        check={}
        for i in  "!?',;.":
            paragraph = paragraph.replace(i," ")
        paragraph = paragraph.lower().split()
        for i in paragraph:
            if i not in banned:
                if i in check:
                    check[i] += 1
                else:
                    check[i] = 1
        ans= " "
        count = 0
        for i in check:
            if count < check[i]:
               count = check[i]
               ans=i
        return ans


  
