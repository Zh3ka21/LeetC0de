# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
               
        if root.right is None and root.left is None:
            return True
        
        if (root.right is not None and root.left is not None) and (root.left.val == root.right.val) and self.isSymmetric(root.left) == self.isSymmetric(root.right):
            return True
          

root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.left = TreeNode(3)


root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right.right = TreeNode(4)

root2.right.left = TreeNode(3)

sol = Solution()
print(sol.isSameTree(root1, root2))