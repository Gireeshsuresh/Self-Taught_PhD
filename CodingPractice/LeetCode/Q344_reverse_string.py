class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s)==1:
            s[0] = s[0]
        else:
            s[:] = s[::-1]