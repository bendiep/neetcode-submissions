class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        temp_dict = {}

        for i in range(len(nums)):
            if nums[i] not in temp_dict:
                temp_dict[nums[i]] = i
        
        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in temp_dict and i != temp_dict[difference]:
                if i < temp_dict[difference]:
                    return [i, temp_dict[difference]]
                return [temp_dict[difference], i]
                    
        return result