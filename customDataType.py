# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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