class Solution:
	def __init__(self, nums, k):
		self.nums = nums
		self.k = k
	def __str__(self):
		return 	str(self.rotate(self.nums,self.k))
		
	
	
	def rotate(self, nums, k):
		"""
		Do not return anything, modify nums in-place instead.
		"""
		while k > 0:
			num = nums.pop()
			nums.insert(0,num)
			k -= 1
		
		
		return nums

print(Solution([1,2,3,4,5,6,7],3))