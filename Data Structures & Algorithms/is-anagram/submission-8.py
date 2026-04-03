class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        temp_dict_s = {}
        temp_dict_t = {}

        # Store chars in s
        for char in s:
            if char not in temp_dict_s:
                temp_dict_s[char] = 1
            else:
                temp_dict_s[char] += 1

        # Store chars in t + minor validation
        for char in t:
            # Edge: Break early if char not found in temp_dict_s
            if char not in temp_dict_s:
                result = False
                break
            
            if char not in temp_dict_t:
                temp_dict_t[char] = 1
            else:
                temp_dict_t[char] = temp_dict_t[char] + 1
                
        # major validation
        if temp_dict_s != temp_dict_t:
            result = False

        return result