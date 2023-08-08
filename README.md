## Intuition:

When we look at an elevation map (represented as a list), we can notice that for any given position, the water trapped above that position is determined by the smaller of the two highest walls on either side of it. Why? Because water will rise up to the level of the shorter wall before it starts spilling over.

For example, if you have an elevation like `[0,1,0,2,1,0,1,3,2,1,2,1]`, the intuition is as follows:

- For the position at index 2 (with height `0`), water trapped is `1` (because the left highest wall is `1` and the right highest wall is `2` and water will rise up to the height of the shorter wall, which is `1`).

- Similarly, for the position at index 5 (with height `0`), the left highest wall is `2` and the right highest wall is `3`. Thus, the water trapped is `2`.

This pattern is consistent for all positions.

## Approach:

1. **Initialization**: Begin with two pointers, one at the start (`left`) and the other at the end (`right`) of the list. Also, initialize two variables to keep track of the highest walls encountered so far from both directions: `max_left` and `max_right`.

2. **Iterative Calculation**: As long as `left` does not cross `right`:
   - If `max_left` is less than `max_right`, then the water trapped at the `left` position is determined by `max_left`. Increment the `left` pointer and update the `max_left` if needed.
   - If `max_left` is greater than or equal to `max_right`, then the water trapped at the `right` position is determined by `max_right`. Decrement the `right` pointer and update the `max_right` if needed.
   - In each case, the amount of trapped water is the difference between the height of the shorter wall (`max_left` or `max_right`) and the elevation at the current position.

3. **Result Accumulation**: Keep a running sum of trapped water for every position and return the total.

## Complexity:

- **Time Complexity**: \(O(n)\)
  - The list is traversed only once, ensuring linear time complexity.

- **Space Complexity**: \(O(1)\)
  - A constant amount of space is used, irrespective of the input size.

## Code:

```python
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
```
