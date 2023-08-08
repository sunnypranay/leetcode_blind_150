from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        result = 0

        while left < right:

            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                result += max_left - height[left]
            
            else:
                right -= 1
                max_right = max(max_right, height[right])
                result += max_right - height[right]
            
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))