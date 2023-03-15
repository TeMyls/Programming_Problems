class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        mid = len(nums)//2
        #print(mid)
        if len(nums) % 2 == 1:
            return float(nums[mid])
        else:
            return (float(nums[mid])+float(nums[mid-1]))/2