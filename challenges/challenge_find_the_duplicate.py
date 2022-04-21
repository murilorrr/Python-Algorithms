def find_duplicate(nums):
    """ Faça o código aqui. """
    try:
        return duplicate_searches(nums)
    except TypeError:
        return False


def duplicate_searches(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] < 0:
            return False
        if nums[i] == nums[i+1]:
            return nums[i]
    return False
