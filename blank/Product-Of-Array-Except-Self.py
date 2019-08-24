# Given an array nums of n integers where n > 1,  return an array output such 
# that output[i] is equal to the product of all the elements of nums except 
# nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not 
# count as extra space for the purpose of space complexity analysis.)

class ProductOfArrayExceptSelf:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice =======================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # blank, result = []

    print(result == output_expected)

# ========== Test ==============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = [int(x) for x in line.strip('\n').split(' ')]
        poaes = ProductOfArrayExceptSelf(input, output_expected)
        if fn == 'blank':
          poaes.blank()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])