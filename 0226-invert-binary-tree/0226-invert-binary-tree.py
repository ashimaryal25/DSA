# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None

        inverted_left = self.invertTree(root.left)
        inverted_right = self.invertTree(root.right)

        root.left = inverted_right
        root.right = inverted_left

        return root

         

        