# Given an integer array nums, find the contiguous subarray (containing at least 
# one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# Follow up:
# If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle.

class MaximumSubarray:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice =========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = 0

    # blank, result = int
    import sys
    max_sum = -sys.maxsize
    current_sum = 0

    for i in input:
      current_sum += i
      max_sum = max(max_sum, current_sum)
      if current_sum < 0:
        current_sum = 0

    result = max_sum
    print(result == output_expected)

# ========== Test ==============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = int(line.strip('\n'))
        ms = MaximumSubarray(input, output_expected)
        if fn == 'blank':
          ms.blank()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])