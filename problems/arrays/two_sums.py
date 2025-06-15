# LeetCode 1: Two Sum
# Problem link: https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

# Example
print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
