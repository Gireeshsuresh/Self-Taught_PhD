from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        if nums[right] < target:
          return right + 1
        elif nums[left] >= target:
          return left

        while left <= right:
          pivot = left + ((right - left)>>1)
          if nums[pivot] == target:
            return pivot
          if target < nums[pivot]:
            if target > nums[pivot-1]:
              return pivot
            right = pivot - 1
          else:
            left = pivot + 1
        return left

mySolution = Solution()
list = [2,3,4,10,40]
x = 1
result = mySolution.searchInsert(list, x)
print(f'Resulting Index = {result}')