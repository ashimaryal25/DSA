# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.res = float('-inf')

        def dfs(node):
            
            if node == None:
                return 0

            sumRight = dfs(node.right)
            sumLeft = dfs(node.left)

            largest = max(node.val, sumRight + node.val, sumLeft + node.val, sumRight + sumLeft + node.val) 
            self.res = max(self.res, largest)


            return max(node.val, sumRight + node.val, sumLeft + node.val)
        dfs(root)
        return self.res

        