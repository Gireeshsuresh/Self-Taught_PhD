from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = [-1,-1]
        for idx,num in enumerate(nums):
            y = target - num
            if y in nums[idx+1:]:
                out[0] = idx
                out[1] = nums.index(y, idx+1)
                break
        return out




if __name__ == "__main__":
    mySolution = Solution()
    
    nums = [3,2,4]
    target = 6

    out = mySolution.twoSum(nums, target)
    print("Input  : {}".format(nums))
   
    print("Output : {}".format(out)) 