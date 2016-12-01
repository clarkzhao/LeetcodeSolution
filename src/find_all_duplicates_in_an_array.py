class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)
        for i in range(len(nums)):
            result[nums[i]-1] += nums[i]
        return [result[i]/2 for i in range(len(result)) if 2*(i +1) == result[i] ]

class Solution2(object):
    def findDuplicates(self,nums):
        result = []
        for value in nums:
            if nums[abs(value)-1] <0:
                result.append(abs(value))
            nums[abs(value) -1] *= -1
        return result

nums = [4,3,2,7,8,2,3,1]
s = Solution2()
print s.findDuplicates(nums)
