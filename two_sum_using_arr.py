def two_sum(nums,target):
    nums.sort()
    left = 0
    right = len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [nums[left],nums[right]]
        elif total < target:
            left = left + 1
        else:
            right = right - 1
    return ["target not achieved"]

nums = [2,8,3,7,56,23,4,1,13,5,7]
target = int(input("Enter target: "))
print(two_sum(nums,target))

