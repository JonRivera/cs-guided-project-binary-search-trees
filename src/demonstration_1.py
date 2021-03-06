"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the binary tree [5,12,32,None,None,8,4],

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""


class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def maxDepth(self, root: BinaryTreeNode) -> int:
    if root is None:  # for when the last node/leaf is encountered
        return 0
    # increment by 1 and do recursive call on both children
    # max will choose which the biggest length from either the left branch(left subtree) or the right one
    # we need +1 to account for the root
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


tree = BinaryTreeNode(5)
tree.left = BinaryTreeNode(12)
right = BinaryTreeNode(32)
right.right = BinaryTreeNode(4)
right.left = BinaryTreeNode(8)
tree.right = right

print(tree.value)