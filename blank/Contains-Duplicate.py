# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in 
# the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class ContainsDuplicate:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice ==========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected

    # blank, result = True/False

    print(result == output_expected)

# ========== Tests ======================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.split(' ')]
      else:
        if line == 'True\n':
          output_expected = True
        else:
          output_expected = False
        cd = ContainsDuplicate(input, output_expected)
        if fn == 'blank':
          cd.blank()

# ========== Command Line Arguments ======================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])