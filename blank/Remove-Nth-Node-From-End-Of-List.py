# Given a linked list, remove the n-th node from the end of list and return its 
# head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

# Create a linked list with 5 nodes
class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
class LinkedList:
  def __init__(self):
    self.next = None
  def create_node(self, data):
    new_node = Node(data, self.next)
    self.next = new_node
  def display_nodes(self):
    nodes = []
    ptr = self.next
    while ptr != None:
      nodes.append(ptr.data)
      ptr = ptr.next
    return nodes
ll = LinkedList()
for i in range(5):
  ll.create_node('Node {}'.format(i))
# print(ll.display_nodes())

# Remove any arbitrary nth node from the linked list created above
class RemoveNthNodeFromEndOfList:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice =========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected

    # blank, result = ll.display_nodes()

    result = ll.display_nodes()
    print(result == output_expected, '\n', output_expected, '\n', result)

# ========== Tests ============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n')
      else:
        output_expected = line.strip('\n').split(', ')
        rnnfeol = RemoveNthNodeFromEndOfList(input, output_expected)
        if fn == 'blank':
          rnnfeol.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])