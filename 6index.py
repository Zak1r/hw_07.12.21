#task 7

def nearestValue(nums, target):
    if len(nums) == 0:  return 'Error'
    nums = list(nums)
    distances_to_target = []
    for num in nums:
        distances_to_target.append(abs(target - num))
    return nums[distances_to_target.index(min(distances_to_target))]

print(nearestValue({4, 7, 10, 11, 12, 17}, 9))
print(nearestValue({4, 7, 10, 11, 12, 17}, 8))
print(nearestValue({1, 2, 3}, 8))
print(nearestValue({100, 2}, 9))