class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            findNum = target - nums[i]
            if findNum in nums[i+1:]:
                index = nums[i+1:].index(findNum) + i + 1
                return [i,index]
