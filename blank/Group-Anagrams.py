# Given an array of strings, group anagrams together.
# 
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

class GroupAnagrams:
  def __init__(self, input, output_expected):
    self.fn_name = 'hash table'
    self.input = input
    self.output_expected = output_expected

# ========== Practice =========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # blank, result = [[], []]

    print(result == output_expected)
    
# ========== Test =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n').split(' ')
      else:
        output_expected = [x.split(' ') for x in line.strip('\n').split(', ')]
        ga = GroupAnagrams(input, output_expected)        
        if fn == 'blank':
          ga.blank()
# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])