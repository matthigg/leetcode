# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's 
# key.
#
# The right subtree of a node contains only nodes with keys greater than the 
# node's key.
#
# Both the left and right subtrees must also be binary search trees.
# 
#
# Example 1:
#
#     2
#    / \
#   1   3
#
# Input: [2, 1, 3]
# Output: true
#
# Example 2:
#
#     5
#    / \
#   1   4
#      / \
#     3   6
#
# Input: [5, 1, 4, null, null, 3, 6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# ========== Binary Tree =======================================================

# Binary Tree Node
class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

# Binary Tree
class BinaryTree:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected
    self.root = None

  # Insert a node into binary tree (level-order insertion, FIFO)
  # https://www.youtube.com/watch?v=aM-oswPn19o&list=PL5tcWHG-UPH2fmYC6kgey1RIxP2iK9EEL&index=2
  def insert(self, data):

    # If there is no root node, create one
    if self.root is None:
      self.root = Node(data)

    # Once a root node has been established, insert remaining nodes
    else:
      self._insert(data, self.root)

  # insert() helper function
  def _insert(self, data, cur_node):

    # Search for an empty spot to place a new node
    queue = []
    queue.append(cur_node)
    while queue:
      cur_node = queue.pop(0)

      # Insert current node into left spot
      if cur_node.left == None:
        cur_node.left = Node(data)
        return

      # Insert current node into right spot
      elif cur_node.right == None:
        cur_node.right = Node(data)
        return

      # Both left and right nodes are taken, enqueue them and search again. Since
      # we're filling spots from left-to-right, it's important to enqueue the left
      # node first.
      else:
        queue.append(cur_node.left)
        queue.append(cur_node.right)

# ========== Validate Binary Search Tree ======================================

  def validateBST(self):
    input, output_expected = self.input, self.output_expected
  
    # Perform 
    def _traverseBT(cur_node, lower=float('-inf'), upper=float('inf')):

      # Base case
      if not cur_node:
        return True

      # Check to make sure that the current node's value is within bounds
      val = cur_node.data
      if val <= lower or val >= upper:
        return False

      # Recursion, adjusting the upper or lower bound as needed
      if not _traverseBT(cur_node.right, val, upper):
        return False
      if not _traverseBT(cur_node.left, lower, val):
        return False
      return True

    result = _traverseBT(self.root)
    print(result == output_expected, '\n', output_expected, '\n', result)

# ========== Tests ============================================================

def test(test_file):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = []
        for x in line.strip('\n').split(' '):
          if x == 'None':
            input.append(None)
          else:
            input.append(int(x))
        # input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = line.strip('\n') == 'True'

        # Create a binary tree
        bt = BinaryTree(input, output_expected)

        # Populate the binary tree with nodes
        for j in input:
          bt.insert(j)

        # Validate whether or not the binary tree is a binary -search- tree
        bt.validateBST()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1])