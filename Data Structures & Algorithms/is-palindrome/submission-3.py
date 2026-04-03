class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = False
        
        # Clean up the string (Remove spaces, special chars etc)
        clean_chars = []
        for char in s:
            if char.isalnum():
                clean_chars.append(char.lower())
        clean_str = ''.join(clean_chars)
        
        # Create reversed clean str
        reverse_clean_str = clean_str[::-1] # [start : end : step]

        # Compare
        if clean_str == reverse_clean_str:
            result = True
        
        return result
