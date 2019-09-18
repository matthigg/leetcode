# Given an array of integers, return indices of the two numbers such that they 
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may 
# not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
#
# return [0, 1].

class TwoSum:
  def __init__(self, input, output_expected, target):
    self.input = input
    self.output_expected = output_expected
    self.target = target

# ========== Practice =========================================================

  def blank(self):
    input, output_expected, target = self.input, self.output_expected, self.target
    N = len(input)
    result = []

    # Create hash table
    from collections import defaultdict
    hash_table = defaultdict(list)

    # First pass
    for i in range(N):
      if input[i] not in hash_table:
        hash_table[input[i]].append(i)
      else:
        hash_table[input[i]].append(i)

    # Second pass
    for j in range(N):
      complement = target - input[j]
      if complement in hash_table and len(hash_table[complement]) == 1:
        result = [hash_table[complement][0], j]
      elif complement in hash_table and len(hash_table[complement]) > 1:
        result = hash_table[complement]

    # print(hash_table)

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
        if fn == 'blank':
          ts.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])