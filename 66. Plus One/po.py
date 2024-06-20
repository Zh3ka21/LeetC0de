class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ss = int(''.join(str(x) for x in digits)) + 1
        s = int(ss)
        lst = []
        for i in str(s):
            lst.append(int(i))
        return lst