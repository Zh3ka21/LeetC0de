import unittest
from merge_sorted_array import Solution

class TestMyModule(unittest.TestCase):
    def __init__(self, methodName: str = "runTestMerge") -> None:
        super().__init__(methodName)
        self.s = Solution()
        
    def test_merge(self):
        self.assertEqual(self.s.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3), [1,2,2,3,5,6])
        
        self.assertEqual(self.s.merge(nums1 = [1], m = 1, nums2 = [], n = 0), [1])
        self.assertEqual(self.s.merge(nums1 = [0], m = 0, nums2 = [1], n = 1), [1])
        

if __name__ == '__main__':
    unittest.main()
