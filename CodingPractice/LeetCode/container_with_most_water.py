from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) -1
        max_area = 0
        local_area = 0
        
        while (start != end): 
            # area = max(area, min(height[start], height[end]) * (end - start))         
            if height[start] <= height[end]:
                local_area = height[start] * (end - start)
                start += 1
            else: 
                local_area = height[end] * (end - start)
                end -= 1
            if local_area > max_area:
                max_area = local_area
            
        return max_area 

if __name__ == "__main__":
    sample_sol = Solution()

    height = [1,8,6,2,5,4,8,3,7]
    output_len = sample_sol.maxArea(height)
    print("Output = {}".format(output_len))