class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        binary = bin(num)[2:]
        
        comp = ""
        for bit in binary:
            comp = comp + str(1-int(bit))
            
        return int(comp,2)
    
