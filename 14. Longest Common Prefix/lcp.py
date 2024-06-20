class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        '''
            Input: strs = ["flower","flow","flight"]
            Output: "fl"
        '''
        pref = strs[0]
        for i in range(1, len(strs)):
            last = 0
            for lp, lw in zip(pref, strs[i]):
                if lw != lp:
                    break                
                last += 1
            pref = pref[:last] 
        return pref


s = Solution()

print(s.longestCommonPrefix(strs = ["flower","flown","flowsght"]))
print(s.longestCommonPrefix(strs = ["dog","racecar","car"]))
