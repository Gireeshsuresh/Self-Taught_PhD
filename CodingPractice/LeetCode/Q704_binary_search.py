from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
      left = 0
      right = len(nums) - 1
      while left <= right:
        # https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
        pivot = left + (right - left)//2
        pivot_val = nums[pivot]
        if target == pivot_val:
          return pivot
        elif target < pivot_val:
          right = pivot - 1
        else:
          left = pivot + 1
      return -1
 
mySolution = Solution()
list = [2,3,4,10,40]
x = 10
result = mySolution.binary_search(list, x)
print(f'Resulting Index = {result}')
    