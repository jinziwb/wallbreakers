class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set()
        for num in nums1:
            set1.add(num)
        
        intersection = set()
        for num in nums2:
            if num in set1:
                intersection.add(num)
                
        return list(intersection)
                
