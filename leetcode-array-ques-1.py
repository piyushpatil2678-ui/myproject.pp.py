class Solution:
    def twoSum(self, nums, target):
        seen = {}    
        for i, n in enumerate(nums):      # enumerate values(n) ko index numder(i) deta hai
            need = target - n
            if need in seen:
                return [seen[need], i]
            seen[n] = i
nums = [2,7,3,8,5,6]
target = 9

s1 = Solution()
print(s1.twoSum(nums,target))
