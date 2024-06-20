def binSer(nums, target):  
    r = 0
    l = len(nums) - 1
    
    while r <= l:
        m = l + (r - l) // 2 
        if nums[m] == target:
            return m
        elif nums[m] < target:
            r = m + 1
        else:
            l = m - 1
            
    else:
        return -1
    
    
a = binSer([1, 2, 3, 4, 5], target=2)    
print(a)