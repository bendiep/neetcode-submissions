class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_dict = {}
        result = False

        for num in nums:
            if num not in temp_dict:
                temp_dict[num] = None
            else:
                result = True
                break
        
        return result
