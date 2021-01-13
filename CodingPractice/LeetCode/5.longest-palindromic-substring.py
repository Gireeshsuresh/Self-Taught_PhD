#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (30.12%)
# Likes:    9215
# Dislikes: 622
# Total Accepted:    1.2M
# Total Submissions: 3.8M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# Example 3:
# 
# 
# Input: s = "a"
# Output: "a"
# 
# 
# Example 4:
# 
# 
# Input: s = "ac"
# Output: "a"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters (lower-case and/or upper-case),
# 
# 
#

# @lc code=start
class Solution:
    def _string_reverse(self, s: str) -> str:
        return s[::-1] 
    
    def is_pallindrome(self, src:str) -> bool: 
        if src == self._string_reverse(src):
            return True
        else:
            return False
    def max_dict_val(self, p:dict) -> str:
        max_str = list(p.keys())[list(p.values()).index(max(p.values()))]
        return max_str

    def longestPalindrome(self, s: str) -> str:
        p_dict = {}
        s_len = len(s)
        start = 0
        end = s_len
        max_len = 0
        for i in range(s_len ):
            for j in range (s_len-1, -1, -1):
                x = s[start+i : end - j + i]
                if self.is_pallindrome(x):
                    if max_len < len(x):
                        max_len = len(x)
                        p_dict[x] = len(x)
        # print(p_dict)

        return self.max_dict_val(p_dict)

if __name__ == "__main__":
    mySolution = Solution()

    input_str = 'a'
    out = mySolution.longestPalindrome(input_str)
    print("Output : {}".format(out))
       
# @lc code=end

