# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None

        first = postorder[-1]

        cur = TreeNode(first)

        mid = inorder.index(first)

        cur.left = self.buildTree(inorder[:mid+1], postorder[0:mid])
        cur.right = self.buildTree(inorder[mid+1:], postorder[mid:len(postorder)-1])

        return cur

        