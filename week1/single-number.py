class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0
        for i in range(len(nums)):
            current = current ^ nums[i]
            
        return(current)
