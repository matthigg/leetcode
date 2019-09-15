# This script is designed to pass input coming from tests/linked-list.txt in 
# the format:
# 
# line 1  - # of nodes to create
# line 2  - expected output
# line 3  - run read_node() method at specified indices
# line 4  - expected output
# line 5  - run update_node() method at specified indices
# line 6  - run update_node() method to change old data to this new data
# line 7  - expected output from update_node()
# line 8  - expected output from display_nodes()
# line 9  - run delete_node() method at specified index
# line 10  - expected output from delete_node()
# line 11 - expected output from display_nodes()
#
# Note: test/linked-list.txt assumes that the linked list is constructed by 
# adding nodes to the beginning of the list rather than the end

# ========== Create a Linked List =============================================

class Node:
  pass

class LinkedList:
  pass

  # Create a node
  def create_node(self, data):
    pass

  # Display all nodes in a list[]
  def display_nodes(self):
    pass

  # Return the length of the linked list as an integer
  def list_length(self):
    pass

  # Return data:value for node at a specific index
  def read_node(self, target_index):
    pass

  # Update the data:value for node at a specific index
  def update_node(self, target_index, new_data):
    pass

  # Delete a node at a specific index
  def delete_node(self, target_index):
    pass

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

      # Create nodes
      if i == 1:
        number_of_nodes = int(line.strip('\n'))
      if i == 2:
        create_test_output_expected = line.strip('\n').split(', ')

      # Search for nodes at specific indices
      if i == 3:
        indices_to_check = [int(x) for x in line.strip('\n').split(' ')]
      if i == 4:
        read_test_output_expected = line.strip('\n').split(', ')

      # Update nodes at specific indices with new data
      if i == 5:
        indices_to_update = [int(x) for x in line.strip('\n').split(' ')]
      if i == 6:
        data_to_update = line.strip('\n').split(', ')
      if i == 7:
        update_test_output_expected_1 = line.strip('\n').split(', ')
      if i == 8:
        update_test_output_expected_2 = line.strip('\n').split(', ')

      # Delete nodes at specific indices
      # if i == 9:
      #   indices_to_delete = [int(x) for x in line.strip('\n').split(' ')]
      # if i == 10:
      #   delete_test_output_expected_1 = line.strip('\n').split(', ')
      # if i == 11:
      #   delete_test_output_expected_2 = line.strip('\n').split(', ')



    testCreate(number_of_nodes, create_test_output_expected)
    testRead(indices_to_check, read_test_output_expected)
    testUpdate(indices_to_update, data_to_update, update_test_output_expected_1, update_test_output_expected_2)
    # testDelete(indices_to_delete, delete_test_output_expected_1, delete_test_output_expected_2)

# ========== Command Line Argument(s) =========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1])

