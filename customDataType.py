# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x = None):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def printTree(root):

        depth = TreeNode.checkDepth(root, 0)
        toCheck = [(root, 0)]
        node_list = []
        prv = 0
        line = ""
        while toCheck:
            node, lvl = toCheck.pop(0)
            if lvl > prv:
                # print("lvl {}".format(lvl))
                print("{}".format(line))
                line = ""
            prv = lvl
            # if node:
            #     node_list.append((str(node.val), lvl))
            # else:
            #     node_list.append(('N', lvl))
            if node:
                line += "".join([" " for _ in range((2 ** (depth - lvl)) - 1)])
                line += str(node.val)
                toCheck.append((node.left, lvl + 1))
                toCheck.append((node.right, lvl + 1))


        # cnt = 0
        # for i in range(depth):
        #     line = ""
        #     for j in range(2**i):
        #         # val = str(node_list[cnt].val) if node_list[cnt] else 'N'
        #         # val = str(cnt)
        #         # val = node_list[cnt]
        #         # cnt += 1
        #         if node_list[0][1] > i:
        #             break
        #         val, lvl = node_list.pop(0)
        #         line += "".join([" " for _ in range((2 ** (depth - i)) - 1)])
        #         line += "{}".format(val)
        #
        #     print(line)

    @staticmethod
    def checkDepth(node, level_from):

        if node is None:
            return level_from

        return max(TreeNode.checkDepth(node.left, level_from+1),
                   TreeNode.checkDepth(node.right, level_from+1))


class Queue:
    def __init__(self, x):
        self.maxS = x
        self.list = []
        self.size = 0

    def enQ(self, x):

        if self.size >= self.maxS:
            return False

        self.list.append(x)
        return True
