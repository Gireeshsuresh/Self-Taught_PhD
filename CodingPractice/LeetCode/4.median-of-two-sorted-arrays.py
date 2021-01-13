#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (30.75%)
# Likes:    8890
# Dislikes: 1370
# Total Accepted:    831.8K
# Total Submissions: 2.7M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
# 
# Follow up: The overall run time complexity should be O(log (m+n)).
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
# 
# 
# Example 4:
# 
# 
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
# 
# 
# Example 5:
# 
# 
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
# 
# 
# 
# Constraints:
# 
# 
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
# 
# 
#

# @lc code=start
import math
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p = sorted(nums1 + nums2)
        v = len(p) % 2
        a = int(len(p)/2)
        if v is 1 :
            x = p[math.floor(len(p)/2)]
        else:
            x =  (p[a-1] + p[a])/2
        return x

# @lc code=end

