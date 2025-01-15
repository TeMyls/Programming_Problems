class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        focus = 0
        amount = 0
        for ele in nums:
            if amount == 0:
                focus = ele
                amount = 1
            elif ele == focus:
                amount = amount + 1
            else:
                amount = amount - 1
        return focus

if __name__ == "__main__":
    s = Solution() 
    print(s.majorityElement([3,2,3]))
