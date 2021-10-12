from typing import List

def binary_search(nums:List, Target:int):
    if Target not in nums:
        return -1
    else:
        left = 0
        mid_idx = len(nums)//2
        mid_val = nums[mid_idx]
        if Target == mid_val:
            return mid_idx
        elif Target < mid_val:
            return binary_search(nums[0:mid_idx], Target)
        else:
            return binary_search(nums[mid_idx+1:len(nums)], Target)            

# if __name__ == 'main':
list = [2,3,4,10,40]
x = 10
r = binary_search(list, x)
print(f'Resulting Index = {r}')
    