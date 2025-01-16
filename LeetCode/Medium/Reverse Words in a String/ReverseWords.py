from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.strip().split()[::-1])

if __name__ == "__main__":
    s1 = "  hello world  "
    s2 = "the sky is blue"
    s3 = "a good   example"
    s = Solution()
    print(s.reverseWords(s2))
