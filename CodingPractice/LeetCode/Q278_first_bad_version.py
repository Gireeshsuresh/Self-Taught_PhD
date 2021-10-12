from typing import List

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n:int):
      """
      :type n: int
      :rtype: int
      """
      left = 0
      right = n-1
      while left <= right:
        pivot = left + (right - left)//2
        if isBadVersion(pivot)!=True: # Good version
          if isBadVersion(pivot+1)==True: # Bad version
            return pivot+1
          else:
            left = pivot + 1
        else:
          right = pivot - 1
      return 1
