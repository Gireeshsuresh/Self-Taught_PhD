#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (76.58%)
# Likes:    21936
# Dislikes: 1019
# Total Accepted:    2.3M
# Total Submissions: 2.9M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        
        def backtrack(s='', left=0, right=0):
            if len(s) == 2 * n:
                out.append(s)
                return
            if left < n:
                backtrack(s + '(', left + 1, right)
            if right < left:
                backtrack(s + ')', left, right + 1)

        backtrack()
        return out
        
# @lc code=end

