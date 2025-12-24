class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        a, b = strs[0], strs[-1]
        res =""
        for i in range(min(len(b),len(a))):
            if a[i] != b[i]:
                return res
            res += a[i]
        return res