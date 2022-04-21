def find_duplicate(nums):
    """ Faça o código aqui. """
    try:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] < 0:
                return False
            if nums[i] == nums[i+1]:
                return nums[i]
        return False
    except TypeError:
        return False
        
