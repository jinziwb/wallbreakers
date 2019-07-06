class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        numsCount = collections.Counter(nums)
        
        dup = numsCount.most_common(1)[0]
        
        n = [i+1 for i in range(len(nums))]
        
        for num in n:
            if num not in numsCount:
                return [dup[0], num]
        
    
