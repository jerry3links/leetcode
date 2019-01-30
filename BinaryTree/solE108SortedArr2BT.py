"""
    from BinaryTree.solE108SortedArr2BT import Solution
    nums = [-10,-3,0,5,9]
    print("nums: {}".format(nums))
    ans = Solution().sortedArrayToBST(nums)
    print("Tree: ")
    Solution().printTree(ans)
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        L = len(nums)

        if L == 0:
            return None

        m = int(L / 2)

        node = TreeNode(nums[m])

        node.left = self.sortedArrayToBST(nums[:m])
        node.right = self.sortedArrayToBST(nums[m+1:])

        return node


    def printTree(self, root):
        from customDataType import TreeNode
        TreeNode.printTree(root)
