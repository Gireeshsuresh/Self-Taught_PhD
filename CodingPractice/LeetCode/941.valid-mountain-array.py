#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (33.53%)
# Likes:    785
# Dislikes: 89
# Total Accepted:    133.8K
# Total Submissions: 400.4K
# Testcase Example:  '[2,1]'
#
# Given an array of integers arr, return true if and only if it is a valid
# mountain array.
# 
# Recall that arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# 
# Example 1:
# Input: arr = [2,1]
# Output: false
# Example 2:
# Input: arr = [3,5,5]
# Output: false
# Example 3:
# Input: arr = [0,3,2,1]
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        STATUS_INIT = 0
        STATUS_UP = 1
        STATUS_DOWN = 2
        
        if len(arr) < 3:
            return False
        status = STATUS_INIT
        for i in range(1,  len(arr)):
            
            if (arr[i-1] == arr[i]):
                return False
            
            if status == STATUS_INIT:
                if arr[i-1] < arr[i]:
                    status = STATUS_UP
                    continue
                else:
                    return False
            elif status == STATUS_UP:
                if arr[i-1] < arr[i]:
                    continue
                else:
                    status = STATUS_DOWN
                    continue
            else:
                if arr[i-1] > arr[i]:
                    continue
                else:
                    return False
        if status == STATUS_DOWN:
            return True
        else:
            return False        
# @lc code=end

