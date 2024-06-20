class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """       
        return len(s.split()[-1])


s = Solution()

assert s.lengthOfLastWord(s = "   fly me   to   the moon  ") == 4
assert s.lengthOfLastWord(s = "Hello World") == 5
assert s.lengthOfLastWord(s = "luffy is still joyboy") == 6
assert s.lengthOfLastWord("Today is a nice day") == 3