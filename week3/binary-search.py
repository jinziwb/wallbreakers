class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = binarySearch(nums, target, 0, len(nums)-1)
        return answer

def binarySearch(nums, target, l, r): 
    while l <= r:   
        mid = l + (r - l) / 2; 

        if nums[mid] == target: 
            return mid 
  
        elif nums[mid] < target: 
            l = mid + 1 
        else: 
            r = mid - 1
    return -1
