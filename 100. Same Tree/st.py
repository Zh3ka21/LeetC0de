# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        '''
        Algorithm:
            If Tree1 is null and Tree2 is null, return true.
            If Tree1 is null and Tree2 is not null, return false.
            If Tree1 is not null and Tree2 is null, return false.
            If the value of Tree1's root node is not equal to the value of Tree2's root node, return false.
            
            
            Recursively call isSameTree(Tree1.left, Tree2.left) and isSameTree(Tree1.right, Tree2.right).
            If both recursive calls return true, return true. Otherwise, return false.
        '''
        
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
                
        if p.val != q.val:
            return False
        else:
           if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
               return True
           else:
               return False

           

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)


root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(4)

root2.right.left = TreeNode(3)

sol = Solution()
print(sol.isSameTree(root1, root2))