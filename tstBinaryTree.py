from customDataType import TreeNode

class treeInstance:
    def createBtree(self):
        root = TreeNode(3)
        root.left = TreeNode(9)
        subBranch = TreeNode(20)
        subBranch.left = TreeNode(15)
        subBranch.right = TreeNode(7)
        root.right = subBranch
        return root