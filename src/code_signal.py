# Balanced Binary Tree
# You are given a binary tree and you need to write a function that can determine if it is height-balanced.
#
# A height-balanced tree can be defined as a binary tree in which the left and right subtrees of every node
#  differ in height by a maximum of 1.
#
# Example 1:
# Given the following tree [5,10,25,None,None,12,3]:
#
#     5
#    / \
#  10  25
#     /  \
#    12   3
# return True.
#
# Example 2:
# Given the following tree [5,6,6,7,7,None,None,8,8]:
#
#        5
#       / \
#      6   6
#     / \
#    7   7
#   / \
#  8   8
# return False.
#
#
#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def height(root):
    # An empty tree has height -1
    if not root:
        return -1
    return 1 + max(height(root.left), height(root.right))


def balancedBinaryTree(root):
    # An empty tree satisfies the definition of a balanced tree
    if not root:
        return True

    # Check if subtrees have height within 1. If they do, check if the
    # subtrees are balanced
    return abs(height(root.left) - height(root.right)) < 2 \
           and balancedBinaryTree(root.left) \
           and balancedBinaryTree(root.right)


# You are given a binary tree and you are asked to write a function that finds its minimum depth.
        # The minimum depth can be defined as the number of nodes along the shortest path from the root down
# to the nearest leaf node. As a reminder, a leaf node is a node with no children.
#
# Example:
# Given the binary tree [5,7,22,None,None,17,9],
#
#     5
#    / \
#   7  22
#     /  \
#    17   9
#your function should return its minimum depth = 2.
# Minimum Depth Binary Tree
def minDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    # wehn root is none
    if not root:
        return 0

    children = [root.left, root.right]
    # if we're at leaf node

    # when childrens are none
    # depth is just one, the root itself
    if not any(children):
        return 1

    min_depth = float('inf')
    # recursively look for the min
    for c in children:
        if c:
            min_depth = min(self.minDepth(c), min_depth)
    return min_depth + 1


""" Extra Problems """


# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up
# all the values along the path equals the given sum.
# Note: A leaf is a node with no children.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# how am i going to add all the nodes together?
# if if the node is none then return 0
# treat the given sum as a limit
# recurisvely  add up all the values in the tree
# if the sum for that pathway is equal to the sum return True

def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    # same thing as say if root is False
    # this is the case where the difference btw the sum and the last value isnt 0, then return False
    if not root:
        return False

    sum -= root.val
    if not root.left and not root.right:  # if reach a leaf
        return sum == 0
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
