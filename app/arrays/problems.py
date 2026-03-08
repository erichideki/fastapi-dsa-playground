"""
Problem: Two Sum

Given an array of integers nums and an integer target,
return the indices of the two numbers such that they add up to target.

Rules:
- Each input has exactly one solution
- You may not use the same element twice
- You can return the answer in any order

Example:

Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

Constraints:
2 <= nums.length <= 10^4
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], i]

        hashmap[num] = i

    return []