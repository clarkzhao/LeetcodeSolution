class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [0,0]
        left,right = 0,len(numbers)-1
        while (left < right):
            sum = numbers[left] + numbers[right]
            if (sum == target):
                res = [left +1, right +1]
                break
            elif (sum > target):
                right -= 1
            else:
                left += 1
        return res

#Test
numbers = [2,7,11,15]
target = 13
s = Solution()
print s.twoSum(numbers, target)
