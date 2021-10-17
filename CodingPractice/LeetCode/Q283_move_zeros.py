# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            len_nums = len(nums)
            nums[:] = [x for x in nums if x!=0]
            new_len = len(nums)
            nums[:] = nums[:] + [0]*(len_nums - new_len)