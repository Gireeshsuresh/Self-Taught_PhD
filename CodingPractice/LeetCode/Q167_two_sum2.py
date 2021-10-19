class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) ==2:
            return [1,2]
        d = {}
        for e,i in enumerate(numbers):
            if (target - numbers[e]) in d:
                return [d[target - i] , e+1]
            d[i] = e + 1