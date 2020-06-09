# Given an array nums of integers, return how many of them contain an even number of digits.
 

# Example 1:

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation: 
# 12 contains 2 digits (even number of digits). 
# 345 contains 3 digits (odd number of digits). 
# 2 contains 1 digit (odd number of digits). 
# 6 contains 1 digit (odd number of digits). 
# 7896 contains 4 digits (even number of digits). 
# Therefore only 12 and 7896 contain an even number of digits.
# Example 2:

# Input: nums = [555,901,482,1771]
# Output: 1 
# Explanation: 
# Only 1771 contains an even number of digits.
 

# Constraints:

# 1 <= nums.length <= 500
# 1 <= nums[i] <= 10^5

import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def get_count_digits(number: int):
            """Return number of digits in a number."""

            if number == 0:
                return 1

            number = abs(number)

            if number <= 999999999999997:
                return math.floor(math.log10(number)) + 1

            count = 0
            while number:
                count += 1
                number //= 10
            return count
        even_count=0
        for num in nums:
            count = get_count_digits(num)
            if(count%2)==0:
                even_count+=1
            # print("Num = ", num , "| Count = ",count)
                
        return even_count
        