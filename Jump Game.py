
list = []
hi = len(list)


def canJump(self, nums):
    if nums[0] == 0 and len(nums) == 1:


        """
    :type nums: List[int]
    :rtype: bool
    """
    '''
    lenNums = len(nums)
    ans = 0
    for i, value in enumerate(nums):
        if ans + value >= lenNums:
            ans += value
        else:
            return False
    return True
    '''
    '''
        if nums[0] == 0 and len(nums) == 1:
        return True
    for i, value in enumerate(nums):
        if value == 0 and i == len(nums) - 1:
                return True
            elif (value == 0 and i == (len(nums) - 2) and nums[::-1]) == 0):
                return True
            elif (value == 0 and i != len(nums)):
                return False

    return True
    '''



