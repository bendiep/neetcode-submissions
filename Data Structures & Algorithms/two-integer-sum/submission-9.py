class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        temp_dict = {}

        # Store all unique values in dict
        for i in range(len(nums)):
            if nums[i] not in temp_dict:
                temp_dict[nums[i]] = i
        
        # Validate if keys in dict match the difference
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in temp_dict and i != temp_dict[difference]:
                if i < temp_dict[difference]:
                    result = [i,temp_dict[difference]]
                else:
                    result = [temp_dict[difference], i]
                break
                
        return result
        