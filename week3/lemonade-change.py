class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        collected = []
        
        for bill in bills:
            if bill == 5:
                collected.append(5)
            elif bill == 10:
                if 5 in collected:
                    collected.remove(5)
                    collected.append(10)
                else:
                    return False
            elif bill == 20:
                if 10 in collected:
                    if 5 in collected:
                        collected.remove(10)
                        collected.remove(5)
                    else:
                        return False
                else:
                    if 5 in collected:
                        collected.remove(5)
                        if 5 in collected:
                            collected.remove(5)
                            if 5 in collected:
                                collected.remove(5)
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
        return True
