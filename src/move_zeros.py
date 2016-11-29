#An brute solution
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index_of_zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.insert(index_of_zero, 0)
                del nums[i+1]
                index_of_zero += 1
        nums[::] = nums[index_of_zero:] + nums[:index_of_zero]

#An more elegant solution
class Solution2(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1

nums = [0, 1, 0, 3, 12,0]
s = Solution2()
s.moveZeroes(nums)
print nums
