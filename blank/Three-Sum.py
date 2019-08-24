# Given an array nums of n integers, are there elements a, b, c in nums such 
# that a + b + c = 0? Find all unique triplets in the array which gives the sum 
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ] 

class ThreeSum:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice ==========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # blank, return = [[], []]

    print(result == output_expected)

# ========== Test ==============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
        ts = ThreeSum(input, output_expected)
        if fn == 'blank':
          ts.blank()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])