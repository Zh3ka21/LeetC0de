#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal1(self, root):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            result = []

            def traverse(r):
                if r:
                    traverse(r.left)
                    result.append(r.val)
                    traverse(r.right)
            
            traverse(root)
            return result
                
    def inorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        stack = []
        current = root

        while current or stack:
            # Reach the leftmost node of the current node
            while current:
                stack.append(current)
                current = current.left

            # Current must be None at this point
            current = stack.pop()
            res.append(current.val)  # Add the node value to result
            current = current.right  # Visit the right subtree

        return res
            
             
        
        
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
        
solution = Solution()
a = solution.inorderTraversal1(root)
b = solution.inorderTraversal1(root)


print(a, b)
#solution.inorderTraversal(root)
