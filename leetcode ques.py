class Solution:
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        best = 0

        while left < right:
            h = min(height[left], height[right])
            best = max(best, h * (right - left))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return best
height = [9,4,6,2,4,5]
s1=Solution()
print(s1.maxArea(height))
