# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        first = preorder[0]
        mid = inorder.index(first)

        cur = TreeNode(first)

        cur.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        cur.right = self.buildTree(preorder[mid+1:], inorder[mid+1:]) 

        return cur           
        