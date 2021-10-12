from typing import List

class Solution:
    def binary_search(self, nums: List[int], target: int) -> int:
      if target not in nums:
          return -1
      else:
          left = 0
          mid_idx = len(nums)//2
          mid_val = nums[mid_idx]
          if target == mid_val:
              return mid_idx
          elif target < mid_val:
              return self.binary_search(nums[0:mid_idx], target)
          else:
              return self.binary_search(nums[mid_idx+1:len(nums)], target)            
 
 
mySolution = Solution()
list = [2,3,4,10,40]
x = 10
result = mySolution.binary_search(list, x)
print(f'Resulting Index = {result}')
    