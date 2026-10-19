class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        shortest = min(strs, key=len)

        for i, ch in enumerate(shortest):
            for s in strs:
                if s[i] != ch:
                    return shortest[:i]

        return shortest
strs = ["flower","flow","flight"]

s1 = Solution()   
print(s1.longestCommonPrefix(strs))
