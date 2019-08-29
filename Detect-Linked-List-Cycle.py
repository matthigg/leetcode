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

  def create_cycle(self, cycle_index):
    ptr = self.head
    nodes = []
    while ptr.next != None:
      nodes.append(ptr)
      ptr = ptr.next
    nodes.append(ptr)
    ptr.next = nodes[cycle_index]

  

# ========== Practice =============================================

def iterative(input, ll, output_expected):
  cycle_index = input[1]

  ptr = ll.head
  current_index = 0

  while ptr != None:
    if ptr.data[-1] == 'x':
      print('cycle detected at {}'.format(ptr.data))
      return cycle_index
    current_index += 1
    ptr.data += 'x'
    ptr = ptr.next
  else:
    print('no cycle detected')
    return -1

# ========== Tests ================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = int(line.strip('\n'))

        # Create linked list
        ll = LinkedList()
        for i in range(input[0]):
          ll.create_node('node {}'.format(input[0] - i - 1))

        # Create a cycle in the linked list
        ll.create_cycle(input[1])

        # Detect the cycle 
        iterative(input, ll, output_expected)


# ========== Command Line Arguments ===============================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])