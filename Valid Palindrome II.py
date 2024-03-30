class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False  # If characters don't match, it's not a palindrome.
            left += 1
            right -= 1
        return True  # If the loop completes, it's a palindrome.
