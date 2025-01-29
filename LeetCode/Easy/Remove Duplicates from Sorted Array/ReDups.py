from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = len(nums) - 1
        n  = 1
        while i > 0:
            if nums[i - 1] == nums[i]:
                nums.pop(i)
            else:
                
                n += 1
                
                
            i -= 1
        print(nums, n)
        return n

s = Solution()
s.removeDuplicates([1,1,2])
