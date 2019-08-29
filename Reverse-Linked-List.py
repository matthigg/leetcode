# Reverse a linked list.

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
    while ptr != None:
      nodes.append(ptr.data)
      ptr = ptr.next
    return nodes


# ========== Practice ==============================================

def iterative(ll, output_expected):
  ptr = ll.head
  prev_node = None
  while ptr != None:
    ptr.target = ptr.next
    ptr.next = prev_node
    prev_node = ptr
    ptr = ptr.target
  ll.head = prev_node

  print(ll.display_nodes() == output_expected, '\n', ll.display_nodes(), '\n', output_expected)

# ========== Test ==================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = int(line.strip('\n'))
      else:
        output_expected = line.strip('\n').split(', ')

        # Create a linked list
        ll = LinkedList()
        if input > 0:
          for i in range(input):
            ll.create_node('node {}'.format(input - i))

          # Reverse the linked list
          iterative(ll, output_expected)

# ========== Command Line Arguments ================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])