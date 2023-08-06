from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1

        while(True):
            if numbers[left_pointer] + numbers[right_pointer] == target:
                return [left_pointer + 1, right_pointer + 1]
            
            if numbers[left_pointer] + numbers[right_pointer] > target:
                right_pointer -= 1
            
            elif numbers[left_pointer] + numbers[right_pointer] < target:
                left_pointer += 1

if __name__ == "__main__":

    numbers = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(numbers, target))