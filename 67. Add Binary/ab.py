class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        na = len(a) - 1
        nb = len(b) - 1
        val = []
        carrier = 0
        
        while na >= 0 or nb >= 0 or carrier:
            nd = carrier
            if na >= 0:
                nd += int(a[na])
                na -= 1
            if nb >= 0:
                nd += int(b[nb])
                nb -= 1
            
            carrier = nd // 2
            val.append(str(nd % 2))
        
        val.reverse()
        return ''.join(val)
    
s = Solution()

s.addBinary(a = "11", b = "1") == "100"

aa = ["1010", "1011"]
s.addBinary(*aa) == "10101"
