#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (36.48%)
# Likes:    32452
# Dislikes: 3054
# Total Accepted:    4.5M
# Total Submissions: 12.3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
# 
# Example 1:
# 
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not
# matter.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left_ptr, right_ptr = i + 1, len(nums) - 1
            while left_ptr < right_ptr:
                sum = nums[i] + nums[left_ptr] + nums[right_ptr]
                if sum == 0:
                    output.append([nums[i], nums[left_ptr], nums[right_ptr]])
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr + 1]:
                        left_ptr += 1
                    while left_ptr < right_ptr and nums[right_ptr] == nums[right_ptr - 1]:
                        right_ptr -= 1
                    left_ptr += 1
                    right_ptr -= 1
                elif sum < 0:
                    left_ptr += 1
                else:
                    right_ptr -= 1
        return output
        
# @lc code=end

s = Solution()
input = [-1,0,1,0]
print(s.threeSum(input))