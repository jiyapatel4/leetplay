import unittest

class Solution():
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        before = []
        overlap = []
        after = []
        merged_interval = []
        if len(intervals) == 0:
            return newInterval
        for interval in intervals:
            if interval[1] < newInterval[0]:
                before.append(interval)
            elif newInterval[1] < interval[0]:
                after.append(interval)
            else:
                overlap.append(interval)
        if len(overlap) > 0:
            merged_interval = [min(newInterval[0], overlap[0][0]), max(newInterval[1], overlap[len(overlap) - 1][1])]
            return before + [merged_interval] + after
        return before + [newInterval] + after

    
class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_smallest_no_overlap(self):
        intervals = [[4, 6], [7, 9], [10, 11], [12, 15]]
        newInterval = [1, 2]
        output = [[1, 2], [4, 6], [7, 9], [10, 11], [12, 15]]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, output)
    
    def test_largest_no_overlap(self):
        intervals = [[4, 6], [7, 9], [10, 11], [12, 15]]
        newInterval = [16, 20]
        output = [[4, 6], [7, 9], [10, 11], [12, 15], [16, 20]]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, output)

    def test_single_interval_overlap_not_containing_end(self):
        intervals = [[4, 6], [7, 9], [13, 14], [16, 19]]
        newInterval = [8, 11]
        output = [[4, 6], [7, 11], [13, 14], [16, 19]]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, output)

    def test_single_interval_overlap_not_containing_start(self):
        intervals = [[4, 6], [7, 9], [13, 14], [16, 19]]
        newInterval = [10, 13]
        output = [[4, 6], [7, 9], [10, 14], [16, 19]]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, output)

    def test_multiple_interval_overlap(self):
        intervals = [[4, 6], [7, 9], [13, 14], [16, 19]]
        newInterval = [8, 17]
        output = [[4, 6], [7, 19]]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, output)

    def test_empty(self):
        intervals = []
        newInterval = [8, 17]
        output = [8, 17]
        result = self.sol.insert(intervals, newInterval)
        self.assertEqual(result, output)




if __name__ == '__main__':
    unittest.main()
