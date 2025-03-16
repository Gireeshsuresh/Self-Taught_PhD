#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (66.19%)
# Likes:    12808
# Dislikes: 423
# Total Accepted:    4.5M
# Total Submissions: 6.8M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # x=sorted(s)
        # y=sorted(t)
        # if x==y:
        #     return True
        # else:
        #     return False
        s1={}
        for x in s:
            if x in s1:
                s1[x]+=1
            else:
                s1[x]=1
        for x in t:
            if x in s1:
                s1[x]-=1
            else:
                return False
        for x in s1:
            if s1[x]!=0:
                return False
        return True
            


        
# @lc code=end

