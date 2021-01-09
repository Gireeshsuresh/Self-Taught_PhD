from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for idx,num in enumerate(nums):
            print(idx, num)
        
        return out



if __name__ == "__main__":
    mySolution = Solution()
    
    nums = [10,2,5,3]
    target = 13

    out = mySolution.twoSum(nums, target)
    print("Input  : {}".format(nums))
   
    print("Output : {}".format(out)) 