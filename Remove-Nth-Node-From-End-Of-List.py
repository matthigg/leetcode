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

# ========== Two Pass =========================================================
# This approach goes through the linked list to get its length, then calculates
# the 'index' of the nth node-from-the-end-of-the-list to remove, goes through
# the linked list again, and removes the node.
# 
# Time complexity: O(n) - we are traversing the list twice, so the time complexity
# is O(2n) which is simply O(n).
# 
# Space complexity: O(1) - we are using a few variables and pointers


  def twoPass(self):
    input, output_expected = self.input, self.output_expected

    # Walk through the linked list to get its length in order to determine the 
    # target_index
    ptr = ll.next
    ll_length = 0
    nth_node = input
    while ptr != None:
      ll_length += 1
      ptr = ptr.next
    target_index = ll_length - int(nth_node)

    # Remove the node at the target_index
    ptr = ll.next
    index = 0
    prev_node = ll
    while ptr != None:
      if index == target_index:
        prev_node.next = ptr.next
        break
      prev_node = ptr
      ptr = ptr.next
      index += 1

    # Reach end of linked list
    if ptr == None:
      print('Nth node not found')

    result = ll.display_nodes()
    print(result == output_expected, '\n', output_expected, '\n', result)

# ========== One Pass =========================================================
# Instead of going through the linked list twice, this approach goes through
# the linked list once using two pointers, which are separated by a distance
# of 'n' -- when the pointer that is 'further along' the linked list reaches
# the end, the other pointer lags behind by exactly 'n' nodes, therefore it will
# be pointing directly at the node that needs to be removed.
#
# Time complexity:
#
# Space complexity:

  def twoPass(self):
    input, output_expected = self.input, self.output_expected

    # --- Need to complete ---

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
        if fn == 'twopass':
          rnnfeol.twoPass()
        elif fn == 'onepass':
          rnnfeol.onePass()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])