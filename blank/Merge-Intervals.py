# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class MergeIntervals:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Pracice ===========================================================

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
        input = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
      else:
        output_expected = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
        mi = MergeIntervals(input, output_expected)
        if fn == 'blank':
          mi.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])