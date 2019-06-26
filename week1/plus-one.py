class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
    
        index = 1
        while index <= len(digits):
            if digits[-1 * index] < 9:
                digits[-1 * index] += 1
                return digits
            else:
                digits[-1 * index] = 0
                index += 1
        digits = [1] + digits
        return digits
