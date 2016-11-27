class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rst = range(1,len(nums)+1)
        for i in range(len(nums)):
            rst[nums[i]-1] = 0  #Mark the appeared value as 0
        return [i + 1 for i in range(len(rst)) if rst[i] != 0]

nums = [4,3,2,7,8,2,3,1]
s = Solution()
print s.findDisappearedNumbers(nums)
