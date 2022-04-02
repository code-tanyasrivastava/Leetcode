class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Method 2
        n = Counter(nums)
        if max(n.values()) > 1:
            return True
        return False        
        # Method 3:
        # log = set()
        # for i in nums:
        #     if i in log:
        #         return True
        #     log.add(i)
        # return False
           
        # Method 1
        # array sort
        # iter through element- if element present -> dic[val] = not null return true else skip.
        # nums.sort()
        # log = {}
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        #     else:
        #         continue
        # return False
        
        
        