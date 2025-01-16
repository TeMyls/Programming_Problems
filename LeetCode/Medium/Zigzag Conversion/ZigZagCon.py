from typing import *
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Do not return anything, modify nums in-place instead.
        """
        if numRows == 1:
            return s
       
        s_len = len(s)
    
        
        arr = [[] for _ in range(numRows)]
       
        bln = True
        i = 0
        #alternated between 0 and numrows, y
        y = 0
        # increments column, x
        x = 0
        while i < s_len:
            
            arr[y].append(s[i])
            

            
            #arr[y] = {}
            #arr[i] = s[i]
            #print(y, x)
            
            if y == numRows - 1:
                
                bln = False
                x += 1
            if i != 0 and y == 0:
                bln = True
                x += 1

            if bln:
                y += 1
            else:
                y -= 1
            
            #print(i)
            i += 1
        return "".join(list(map(lambda w: "".join(w), arr)))

if __name__ == "__main__":
    s1 = "PAYPALISHIRING"
    
    s = Solution()
    print(s.convert(s1, 3))
