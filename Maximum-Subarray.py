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

# ========== Kadane's Algorithm =================================================
# This is "Kadane's Algorithm" which is basically perfect for this problem. It
# works similarly to an algorithm in the Buy-And-Sell-Stock.py problem.
#
# Time complexity: O(n) - each element 'n' in the input[] list is traversed
#
# Space complexity: O(1) - all we need are a couple of variables

  def kadanesAlgorithm(self):
    input, output_expected = self.input, self.output_expected

    # Set the current and max (ie. result) sums
    from sys import maxsize
    current_sum = 0
    result = -sys.maxsize

    # Kadane's Algorithm
    for value in input:
      current_sum += value
      if current_sum > result:
        result = current_sum
      elif current_sum < 0:
        current_sum = 0

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
        if fn == 'kadanesAlgorithm':
          ms.kadanesAlgorithm()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])