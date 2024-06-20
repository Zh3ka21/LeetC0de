class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nl = len(needle)
        hl = len(haystack)
        
        for i in range(hl):
            if haystack[i:nl+i] == needle:
                return i
        else:
            return -1
        
    
s = Solution()

assert s.strStr(haystack = "ssadbutsad", needle = "sad") == 1

assert s.strStr(haystack = "leetcode", needle = "leeto") == -1

assert s.strStr("hello", "ll") == 2

assert s.strStr("mississippi", "issi") == 1