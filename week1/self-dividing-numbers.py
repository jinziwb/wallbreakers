class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        nums = []
        for i in range(left, right+1):
            if isSelfDividing(i):
                nums.append(i)
        return nums
            
def isSelfDividing(num):
    copyNum = num
    while copyNum > 0:
        digit = copyNum % 10
        if digit == 0 or  num % digit != 0:
            return False
        copyNum = copyNum / 10
    return True
