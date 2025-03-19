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
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        """ Two sum to find all unique pairs that add up to a target number, given a sorted array as input """
        output = []
        left, right = 0, len(numbers)-1
        
        while left < right:
            actual_sum = numbers[left] + numbers[right]
            if actual_sum == target:
                # Check if pair already exists to avoid duplicates
                if [numbers[left], numbers[right]] not in output:
                    output.append([numbers[left], numbers[right]])
                left += 1
                right -= 1
                # Skip duplicates
                while left < right and numbers[left] == numbers[left-1]:
                    left += 1
                while left < right and numbers[right] == numbers[right+1]:
                    right -= 1
            elif actual_sum > target:
                right -= 1
            else:
                left += 1
        return output
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            # Skip duplicates to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            # Find pairs that sum to -nums[i]
            # a + b + c = 0 ==> b+c = (-a)
            target = -nums[i] 
            pairs = self.twoSum(nums[i+1:], target)
            
            # Add current number to each pair to form triplets
            for pair in pairs:
                result.append([nums[i]] + pair)
                
        return result

# @lc code=end

s = Solution()
numbers = [-1,0,1,2,-1,-4]
# print(s.twoSum(numbers, 0))
print(s.threeSum(numbers))