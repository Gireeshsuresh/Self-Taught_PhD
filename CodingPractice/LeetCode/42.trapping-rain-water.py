#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (64.35%)
# Likes:    33653
# Dislikes: 587
# Total Accepted:    2.7M
# Total Submissions: 4.2M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        count = 0
        
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                count += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                count += max(0, right_max - height[right])
        
        return count
# @lc code=end

s = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(input))

# [0,1] / [0,2] = 0
# [x,0,y] ->  (x > 0, y > 0 ) -> 1 unit / more depending on min(x , y)
# [x, x-i , .. , y-j, y] -> [ x > 0 , y > 0 ] -> 1 or more unit dep on min(x, y)

# row_scan:
# start=1, end = 1 , area = l*b - (existing heights)