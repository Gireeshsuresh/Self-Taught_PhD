#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# https://leetcode.com/problems/sort-array-by-parity/description/
#
# algorithms
# Easy (76.27%)
# Likes:    5490
# Dislikes: 154
# Total Accepted:    888.2K
# Total Submissions: 1.2M
# Testcase Example:  '[3,1,2,4]'
#
# Given an integer array nums, move all the even integers at the beginning of
# the array followed by all the odd integers.
# 
# Return any array that satisfies this condition.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be
# accepted.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0]
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# 0 <= nums[i] <= 5000
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left ,right = 0 , len(nums)-1 
        while left < right:
            if nums[left] % 2 != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right-=1
            else:
                left+=1
        return nums
        
# @lc code=end

s= Solution()
i = [0]
print(s.sortArrayByParity(i))
