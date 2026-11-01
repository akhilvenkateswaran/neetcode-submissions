class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []

        for i in range(len(intervals)):

            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                print('1',res)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
                print('2',res)
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
                print('3',newInterval)
        res.append(newInterval)

        return res