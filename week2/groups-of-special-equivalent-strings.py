class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        
        unique = set()
        for a in A:
            odd = ""
            even = ""
            for i in range(len(a)):
                if i % 2 == 0:
                    even += a[i]
                else:
                    odd += a[i]
            odd = ''.join(sorted(odd))
            even = ''.join(sorted(even))
            unique.add((odd , even))
        return(len(unique))
        
                
