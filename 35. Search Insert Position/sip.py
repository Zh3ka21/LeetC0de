class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0, len(nums) - 1
        m = 0
        
        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return l
        
s = Solution()


#assert s.searchInsert(nums = [1,2,3,6,7], target = 5) == 2

assert s.searchInsert(nums = [1,3,5,6], target = 5) == 2
assert s.searchInsert(nums = [1,3,5,6], target = 2) == 1

            