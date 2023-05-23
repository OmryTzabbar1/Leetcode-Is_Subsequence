'''

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

'''

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    dict = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dict:
            return [list(dict).index(target - nums[i]), i]

        dict[nums[i]] = i
    return []

nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))






