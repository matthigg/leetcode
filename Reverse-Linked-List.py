# Reverse a singly linked list.
#
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you 
# implement both?

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def create_node(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def display_nodes(self):
    ptr = self.head
    nodes = []
    while ptr:
      nodes.append(ptr.data)
      ptr = ptr.next
    return nodes

class ReverseLinkedList:
  def __init__(self, input, ll, output_expected):
    self.input = input
    self.ll = ll
    self.output_expected = output_expected

# ========== Iterative Solution ===============================================
# x
#
# Time complexity:
#
# Space complexity:

  def iterative(self):
    input, output_expected = self.input, self.output_expected

    # Reverse linked list
    # print(self.ll.display_nodes())
    ptr = self.ll
    print(ptr)


# ========== Recursive Solution ===============================================
# x
#
# Time complexity:
#
# Space complexity:

  def recursive(self):
    input = self.input
    output_expected = self.output_expected
    print(input, output_expected)

# ========== Test =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n')
      else:
        output_expected = line.strip('\n')
        
        # Create Linked List
        ll = LinkedList()
        ll.create_node('node 3')
        ll.create_node('node 2')
        ll.create_node('node 1')

        # Reverse Linked List
        rll = ReverseLinkedList(input, ll, output_expected)
        if fn == 'iterative':
          rll.iterative()
        if fn == 'recursive':
          rll.recursive()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])