import collections

class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
      
        dict = collections.defaultdict(list)
        for i,s in enumerate(S):
            dict[s].append(i)
        # print(dict)
        values = sorted(dict.values())
        # print(values)
        compiledList = []
        currentFirst = 0
        currentLast = 0
        for lst in values:
            # print(currentFirst, currentLast, lst[0],lst[-1])
            if lst[0]> currentLast:
                # if currentFirst == 0 and currentLast == 0:
                #     if lst[0] == 1:
                #     pass
                # else:
                    # compiledList.append(currentLast - currentFirst + 1)
                compiledList.append(currentLast - currentFirst + 1)
                currentFirst = lst[0]
                currentLast = lst[-1]
            elif lst[0] < currentFirst:
                currentFirst = lst[0]
            elif lst[-1] > currentLast:
                currentLast = lst[-1]
        compiledList.append(currentLast - currentFirst + 1)
        
        return compiledList
                
