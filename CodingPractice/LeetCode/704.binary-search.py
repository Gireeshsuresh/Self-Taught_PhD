#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#
# https://leetcode.com/problems/binary-search/description/
#
# algorithms
# Easy (59.18%)
# Likes:    12445
# Dislikes: 271
# Total Accepted:    3M
# Total Submissions: 5.1M
# Testcase Example:  '[-1,0,3,5,9,12]\n9'
#
# Given an array of integers nums which is sorted in ascending order, and an
# integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# 
# 
# Example 2:
# 
# 
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
        
# @lc code=end

nums = [-1,0,3,5,9,12]
target = 2

s = Solution()
print(s.search(nums, target))
