from typing import *

class Solution:
    def __init__(self) -> None:
        pass

    def removeElement(self, nums: List[int], val: int) -> int:
        i = len(nums) - 1
        n  = 0
        while i > -1:
            if nums[i] == val:
                nums.pop(i)
                #nums.append(' ')
            else:
                if i < len(nums):
                    n += 1
                
            i -= 1
        print(n, nums)
        return n

s = Solution()
s.removeElement([3,2,2,3] , 3)
            
