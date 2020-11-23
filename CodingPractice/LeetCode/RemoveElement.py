# Given an array nums and a value val, remove all instances of that value in-place and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]
# Explanation: Your function should return length = 2, with the first two elements of nums being 2.
# It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] 

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]
# Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        out_len = 0
        for k,x in enumerate(nums):
            if x == val:
                continue
            else:
                nums[out_len]=nums[k]
                out_len +=1
        return out_len

if __name__ == "__main__":
    mySolution = Solution()

    nums1 = [3,2,2,3]
    m = 3
    print("Input List : {}".format(nums1))
    out = mySolution.removeElement(nums1,m)
    print("Output : {}, {}".format(out,nums1))