class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        nums = [0,1] + [None]*(n-1)
        for i in range(1,n):
            if (2*i) <=n:
                nums[2*i] = nums[i]
            if (2*i + 1) <=n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums)
            
        