#
# @lc app=leetcode id=535 lang=python3
#
# [535] Encode and Decode TinyURL
#
# https://leetcode.com/problems/encode-and-decode-tinyurl/description/
#
# algorithms
# Medium (86.63%)
# Likes:    2065
# Dislikes: 3799
# Total Accepted:    279.9K
# Total Submissions: 323.1K
# Testcase Example:  '"https://leetcode.com/problems/design-tinyurl"'
#
# Note: This is a companion problem to the System Design problem: Design
# TinyURL.
# 
# TinyURL is a URL shortening service where you enter a URL such as
# https://leetcode.com/problems/design-tinyurl and it returns a short URL such
# as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a
# tiny URL.
# 
# There is no restriction on how your encode/decode algorithm should work. You
# just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
# can be decoded to the original URL.
# 
# Implement the Solution class:
# 
# 
# Solution() Initializes the object of the system.
# String encode(String longUrl) Returns a tiny URL for the given longUrl.
# String decode(String shortUrl) Returns the original long URL for the given
# shortUrl. It is guaranteed that the given shortUrl was encoded by the same
# object.
# 
# 
# 
# Example 1:
# 
# 
# Input: url = "https://leetcode.com/problems/design-tinyurl"
# Output: "https://leetcode.com/problems/design-tinyurl"
# 
# Explanation:
# Solution obj = new Solution();
# string tiny = obj.encode(url); // returns the encoded tiny url.
# string ans = obj.decode(tiny); // returns the original url after decoding
# it.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= url.length <= 10^4
# url is guranteed to be a valid URL.
# 
# 
#

# @lc code=start
class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.url_map = {}
        self.counter = 0
        shortUrl = "http://tinyurl.com/" + str(self.counter)
        self.url_map[shortUrl] = longUrl
        self.counter += 1
        return shortUrl
        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_map.get(shortUrl, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
c = Codec()
print(c.decode(c.encode("https://leetcode.com/problems/design-tinyurl")))
