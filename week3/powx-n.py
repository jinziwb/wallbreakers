class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n >= 0:
            return rec(x,n)
        else:
            return 1/rec(x,abs(n))
    
def rec(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x
    elif n % 2 == 0:
        print(n)
        return rec(x*x,n/2)
    else:
        return x*rec(x*x,(n-1)/2)
