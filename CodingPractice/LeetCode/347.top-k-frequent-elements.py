#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (64.12%)
# Likes:    18070
# Dislikes: 711
# Total Accepted:    2.7M
# Total Submissions: 4.2M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

from typing import List

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # key: number, value: frequency
        output=[]

        for n in nums:
            count[n] = 1 + count.get(n,0)

        freq_array = [[] for _ in range(len(nums)+1)] # index: frequency, value: number
        for key, val in count.items():
            freq_array[val].append(key)
        for i in range(len(freq_array)-1, 0 , -1):
            for val in freq_array[i]:
                output.append(val)
            if len(output) == k:
                return output
                
# @lc code=end

s = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums, k)) #[1,2]
