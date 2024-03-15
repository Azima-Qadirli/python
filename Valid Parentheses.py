class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for i in s:
            if i in "({[":
                check.append(i)
            elif i in ")}]" and not check:
                return False
            elif i == ")" and check[-1] != "(":
                return False
            elif i == "}" and check[-1] != "{":
                return False
            elif i == "]" and check[-1] != "[":
                return False
            else:
                check.pop()
        if not check:
            return True
        return False