class Solution():
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pt_i = 0
        pt_j = len(height) - 1
        max_area = 0
        while pt_i < pt_j:
            new_area = (pt_j - pt_i) * min(height[pt_i], height[pt_j])
            if new_area > max_area:
                max_area = new_area
            if height[pt_i] > height[pt_j]:
                pt_j = pt_j - 1
            else:
                pt_i = pt_i + 1
        return max_area
