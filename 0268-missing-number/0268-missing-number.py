class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        rs = (n*(n+1))/2
        ans = rs - s
        return int(ans)