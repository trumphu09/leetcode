class Solution:
    def romanToInt(self, s: str) -> int:
        arr = list(s)
        change = {"I":1, "V":5, "X" : 10, "L" : 50, "C":100,"D":500, "M":1000}
        total = 0
        for idx, num in enumerate(arr) :
            arr[idx] = change[num]
        for idx, num in enumerate(arr):
            if idx + 1 < len(arr):
                if num < arr[idx + 1]:
                    total -= num
                else :
                    total += num
        total += arr[-1]
        return total
