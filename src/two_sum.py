class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i in range(len(nums)):
            residual = target - nums[i]
            if hash_map.has_key(residual):
                return [hash_map[residual], i]
            hash_map[nums[i]] = i
            
Class Test(object):
