# Given a 2d grid map of '1's (land) and '0's (water), count the number of 
# islands. An island is surrounded by water and is formed by connecting adjacent 
# lands horizontally or vertically. You may assume all four edges of the grid 
# are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class NumberOfIslands:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice =========================================================

  def bruteForce(self):
    grid, output_expected = self.input, self.output_expected
    result = 0

    # blank, result = int

    print(result == output_expected, output_expected, result)

# ========== Tests ============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    map_2d = []
    for i, line in enumerate(lines):
      if line.strip('\n').split(', ')[0] != 'output':
        row = [int(x) for x in line.strip('\n')]
        map_2d.append(row)
      else:
        output_expected = int(line.strip('\n').split(', ')[1])
        noi = NumberOfIslands(map_2d, output_expected)
        map_2d = []
        if fn == 'bruteForce':
          noi.bruteForce()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])