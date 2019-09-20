# Binary trees are data structures that are similar to linked lists in that they 
# are composed of a collections of connected nodes; however, while each node in 
# a singly-linked list is connected to the next node (except for the last node, 
# which points to None), each node in a binary tree can be connect to a left node,
# a right node, both a left and a right node, or no nodes.
#
# When one node points to another node, that node is the "parent" node and the
# node that it points to is the "child". Each child node has a parent node,
# which is a child node of some other parent node, etc. and this parent-child
# relationship can be traced all the way back to the starting node, or "root"
# node.
#
# The starting node, or "root" node, sits at the top of the tree structure and
# is the only node that will not have a "parent node", ie. another node that
# points to it. Parent nodes are sometimes called "ancestor" nodes, so the root 
# node is effectively an ancestor node to every other node in the binary tree.
#
# Nodes with no children are called "leaf" nodes.
#
# For example:
#
#               Binary Tree
#                   
#                    5      root node
#                   / \
#                  3   2    parent & children nodes
#                 / \   \
#                4   1   6  children & leaf nodes
#
# Binary search trees are -ordered- binary trees. One common way to order binary
# trees is to create a rule where each node contains a value, and if that node
# contains any child nodes then the left child node's value must be less than the
# current/parent node's value, and the right child node's value must be greater 
# than the current/parent node's value. For example:
#
#               Binary Search Tree
#                   
#                    4      root node
#                   / \
#                  3   5    parent & children nodes
#                 / \   \
#                1   2   6  children & leaf nodes
#

# ========== Binary Search Tree =======================================================

# Binary Search Tree Node
class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None

# Binary Search Tree
class BinarySearchTree:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected
    self.root = None

  # Insert a node into binary search tree
  def insert(self, data):

    # If there is no root node, create one
    if self.root is None:
      self.root = Node(data)
    else:
      self._insert(data, self.root)

  # Insert helper function
  def _insert(self, data, cur_node):

    # Look left
    if data < cur_node.data:
      if cur_node.left is None:
        cur_node.left = Node(data)
      else:
        self._insert(data, cur_node.left)

    # Look right
    elif data > cur_node.data:
      if cur_node.right is None:
        cur_node.right = Node(data)
      else:
        self._insert(data, cur_node.right)

    # Prevent duplicate nodes from being inserted into the binary search tree
    else:
      print('Node.data {} is already present in tree'.format(data))

  # Find the node that has some specified data, if it exists
  def find(self, data):

    # Make sure that a root node exists
    if self.root:
      is_found = self._find(data, self.root)
      if is_found:
        return True
      return False
    else:
      return None

  # Find helper function
  def _find(self, data, cur_node):
    if data < cur_node.data and cur_node.left:
      return self._find(data, cur_node.left)
    elif data > cur_node.data and cur_node.right:
      return self._find(data, cur_node.right)
    if data == cur_node.data:
      return True

# ========== Tests ============================================================

def test(test_file):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 3 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      elif i % 3 == 1:
        test_case = [int(x) for x in line.strip('\n').split(' ')]
      elif i % 3 == 2:
        output_expected = [x == 'True' for x in line.strip('\n').split(' ')]

        # Create a binary search tree
        bst = BinarySearchTree(input, output_expected)

        # Populate the binary search tree with nodes
        for j in input:
          bst.insert(j)

        # Find nodes in binary search tree
        result = []
        for k in test_case:
          result.append(bst.find(k))

        print(result == output_expected, '\n', output_expected, '\n', result)

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1])