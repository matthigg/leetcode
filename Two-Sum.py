# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.

# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.

class TwoSum:
  def __init__(self, input, output_expected, target):
    self.input = input
    self.output_expected = output_expected
    self.target = target

# ========== Brute Force =====================================================
# Time complexity: O(n^2) - double FOR loops
#
# Space complexity: O(n) - each FOR loop creates a shallow copy of the list 
# containing up to 'n' - 1 number of items

  def bruteForce(self):
    input, output_expected, target = self.input, self.output_expected, self.target

    # 2x FOR loop
    result = []
    for i in range(len(input) - 1):
      for j in range(i + 1, len(input)):
        if input[i] + input[j] == target:
          result = [i, j]

    print(result == output_expected, '\n', output_expected, '\n', result)

# ========== Two-pass Hash Table =============================================
# On the first pass, create a hash table which contains each element in the
# input[] list as a key, and a list of indices as each key's value. 
#
# Time complexity: O(n) - we traverse the list containing 'n' elements exactly 
# twice, each look-up in the table costs O(1) time
#
# Space complexity: O(n) - the created hash table stores 'n' number of items

  def twoPass(self):
    input, output_expected, target = self.input, self.output_expected, self.target

    # Hash table
    from collections import defaultdict
    hash_table = defaultdict(list)
    for index, value in enumerate(input):
      hash_table[value].append(index)

    # Check whether each input[] value has corresponding value in hash_table{} that
    # can be added to == target
    result = []
    for index, value in enumerate(input):
      complement = target - value

      # Handle the case where a + a = b; make sure that at least two a's exist in
      # the hash_table{} via len(hash_table[complement]) > 1
      if complement in hash_table and value == complement and len(hash_table[complement]) > 1:
        result = hash_table[complement]

      # Handle the case where a + b = c
      elif complement in hash_table and value != complement:
        result = [hash_table[complement][0], index]

    print(result == output_expected, '\n', output_expected, '\n', result)

# ========== One-pass Hash Table =============================================
# Similar to the Two-pass Hash Table approach, except we check if the complement
# exists during the construction of hash_table{}
#
# Time complexity: O(n) - traverse the list of 'n' elements only once, each 
# look-up in the table costs O(1) time
#
# Space complexity: O(n) - extra space depends on items stored in the hash
# table, which is at -most- equal to 'n'

  def onePass(self):
    input, output_expected, target = self.input, self.output_expected, self.target

    # Hash table & searching for the complement in the same FOR loop
    from collections import defaultdict
    hash_table = defaultdict(list)
    result = []
    for index, value in enumerate(input):
      complement = target - value
      if complement in hash_table:
        result = hash_table[complement][:] + [index]
        break
      else:
        hash_table[value].append(index)

    print(result == output_expected, '\n', output_expected, '\n', result)

# ========== Test ============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        target = int(line.strip('\n').split(', ')[0])
        input = [int(x) for x in line.strip('\n').split(', ')[1].split(' ')]
      else:
        output_expected = [int(x) for x in line.strip('\n').split(' ')]
        ts = TwoSum(input, output_expected, target)
        if fn == 'bruteForce':
          ts.bruteForce()
        elif fn == 'twoPass':
          ts.twoPass()
        elif fn == 'onePass':
          ts.onePass()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])