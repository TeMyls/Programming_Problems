class Solution:
	def __init__(self, s):
		self.s = s
		print(s)
		print(self.isValid(self.s))
		
	def __str__(self):
		return self.s
		
	def isValid(self, s) -> bool:
		open_matches = {
			'(':')',
			'[':']',
			'{':'}',
		}
		open_stack = []
		close_queue= []
		i = 0
		j = 1
		if len(s) > 1:
			if s[0] in [')','}',']'] or s[len(s) - 1] in ['(','{','[']:
				return False
			while i < len(s):
									
					
				if s[i] in [')','}',']']:
					close_queue.append(s[i])
				elif s[i] in ['(','{','[']:
					open_stack.append(s[i])
				end = len(open_stack) - 1
				if open_stack and close_queue:
					if open_matches[open_stack[end]] == close_queue[0]:
						open_stack.pop()
						close_queue.pop(0)
					else:
						return False
				i += 1
				
			print(open_stack,close_queue,sep = '\n')
			
			
						
		elif len(s) <= 1:
			return False
		return True


Solution("([])")
Solution("([)]")
Solution("[([]])")
Solution("()[]{}")

				
		
			