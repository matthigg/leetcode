# This script is designed to pass input coming from tests/linked-list.txt in 
# the format:
# 
# line 1 - <create # of nodes>
# line 2 - <output expected>
# line 3 - <read node at index i> 
# line 3 - <output expected>
# 

# ========== Create a Linked List =============================================

class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = Node()

  # Create a node
  def create_node(self, data):
    ptr = self.head
    while ptr.next != None:
      ptr = ptr.next
    ptr.next = Node(data)

  # Return all nodes in a list
  def display_nodes(self):
    ptr = self.head
    nodes = []
    while ptr.next != None:
      nodes.append(ptr.next.data)
      ptr = ptr.next
    return nodes

  # Return the length of the list as an integer
  def list_length(self):
    ptr = self.head
    length = 0
    while ptr.next != None:
      length += 1
      ptr = ptr.next
    return length

  # Return data:value for node at a specific index
  def read_node(self, target_index):

    # Handle index that's out of range
    if target_index > self.list_length() or target_index < 0:
      return 'Error: index outside of index range'

    ptr = self.head
    index = 0
    while ptr.next != None:
      ptr = ptr.next
      if index == target_index:
        return ptr.data
      index += 1
    else:
      return 'Error: index not found'

  # Update the data:value for node at a specific index
  def update_node(self, target_index, new_data):

    # Handle index that's out of range
    if target_index > self.list_length() or target_index < 0:
      return 'Error: index outside of index range'

    ptr = self.head
    index = 0
    while ptr.next != None:
      ptr = ptr.next
      if index == target_index:
        ptr.data = new_data
        return ptr.data
      index += 1
    else:
      return 'Error: index not found'

  # Delete a node at a specific index
  def delete_node(self, target_index):

    # Handle index that's out of range
    if target_index > self.list_length() or target_index < 0:
      return 'Error: index outside of index range'

    ptr = self.head
    index = 0
    while ptr.next != None:
      prev_node = ptr
      ptr = ptr.next
      if index == target_index and ptr.next != None:
        print('x')
        prev_node.next = ptr.next
        return '{}-DELETED'.format(ptr.data)
      elif index == target_index and ptr.next == None:
        print(prev_node.data, ptr.data, ptr.next)
        prev_node.next = None
        return '{}-DELETED'.format(ptr.data)
      index += 1
    else:
      return 'Error: index not found'

# ========== Tests ============================================================

# Test - Create/Read
def testCreate(input, output_expected):
  ll = LinkedList()
  for i in range(input):
    ll.create_node('Node-{}'.format(i))

  # Result - Create
  result = ll.display_nodes()
  print('Create:', result == output_expected, '\n', result, '\n', output_expected)

# Test - Read
def testRead(input, output_expected):
  ll = LinkedList()
  for i in range(input[-1] + 1):
    ll.create_node('Node-{}'.format(i))

  # Result - Read
  result = []
  for j in range(len(input)):
    result.append(ll.read_node(input[j]))  
  print('Read:', result == output_expected, '\n', result, '\n', output_expected)

# Test - Update
def testUpdate(input, data, output_expected_1, output_expected_2):
  ll = LinkedList()
  for i in range(input[-1] + 1):
    ll.create_node('Node-{}'.format(i))
  
  # Results - Update
  result_1 = []
  result_2 = []
  for j in range(len(input)):
    result_1.append(ll.update_node(input[j], data[j]))
  print('Update - 1', result_1 == output_expected_1, '\n', result_1, '\n', output_expected_1)
  result_2 = ll.display_nodes()
  print('Update - 2', result_2 == output_expected_2, '\n', result_2, '\n', output_expected_2)

# Test - Delete
def testDelete(input, output_expected_1, output_expected_2):
  ll = LinkedList()
  for i in range(input[-1] + 1):
    ll.create_node('Node-{}'.format(i))

  # Results - Delete
  result_1 = []
  result_2 = []
  for j in range(len(input)):
    result_1.append(ll.delete_node(input[j]))
  print('Update - 1', result_1 == output_expected_1, '\n', result_1, '\n', output_expected_1)
  result_2 = ll.display_nodes()
  print('Update - 2', result_2 == output_expected_2, '\n', result_2, '\n', output_expected_2)



# Run all tests
def test(test_file):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):

      if i == 0:
        number_of_nodes = int(line.strip('\n'))
      if i == 1:
        create_test_output_expected = line.strip('\n').split(', ')
      if i == 2:
        indices_to_check = [int(x) for x in line.strip('\n').split(' ')]
      if i == 3:
        read_test_output_expected = line.strip('\n').split(', ')
      if i == 4:
        indices_to_update = [int(x) for x in line.strip('\n').split(' ')]
      if i == 5:
        data_to_update = line.strip('\n').split(', ')
      if i == 6:
        update_test_output_expected_1 = line.strip('\n').split(', ')
      if i == 7:
        update_test_output_expected_2 = line.strip('\n').split(', ')
      if i == 8:
        indices_to_delete = [int(x) for x in line.strip('\n').split(' ')]
      if i == 9:
        delete_test_output_expected_1 = line.strip('\n').split(', ')
      if i == 10:
        delete_test_output_expected_2 = line.strip('\n').split(', ')



    # testCreate(number_of_nodes, create_test_output_expected)
    # testRead(indices_to_check, read_test_output_expected)
    # testUpdate(indices_to_update, data_to_update, update_test_output_expected_1, update_test_output_expected_2)
    testDelete(indices_to_delete, delete_test_output_expected_1, delete_test_output_expected_2)

# ========== Command Line Argument(s) =========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1])

