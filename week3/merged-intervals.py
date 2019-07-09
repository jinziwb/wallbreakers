class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        merged = []
        if len(intervals) == 0:
            return merged
        
        intervals = sorted(intervals, key=lambda element: (element[0], element[1]))
        
        i = 0
        current = intervals[i]
        while i < len(intervals)-1:
            nextInt = intervals[i+1]
            if current[1] >= nextInt[0]:
                current = [current[0], max(current[1],nextInt[1])]
            else: 
                merged.append(current)
                current = nextInt
            i += 1
        if current not in merged:
            merged.append(current)
        return merged
