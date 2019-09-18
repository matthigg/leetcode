# Given an m x n matrix of non-negative integers representing the height of each 
# unit cell in a continent, the "Pacific ocean" touches the left and top edges 
# of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell 
# to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and 
# Atlantic ocean.
#
# Note:
#
# - The order of returned grid coordinates does not matter.
# - Both m and n are less than 150.
# - Water can -start- at any grid location, and possibly flows from that grid 
# location towards either ocean as per the rules stated above. It is this starting
# location that you are supposed to return as an answer in the form of coordinates
# as [y, x] or [row, col], if that coordinate has a "path" for water to flow to
# both the "Pacific" and "Atlantic" oceans.
#
# Example:
#
# Given the following 5x5 matrix:
#
#  Pacific ~   ~   ~   ~   ~ 
#       ~  1   2   2   3  (5) *
#       ~  3   2   3  (4) (4) *
#       ~  2   4  (5)  3   1  *
#       ~ (6) (7)  1   4   5  *
#       ~ (5)  1   1   2   4  *
#          *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with 
# parentheses in above matrix).

class PacificAtlanticWaterFlow:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Brute Force =======================================================
# https://leetcode.com/problems/pacific-atlantic-water-flow/discuss/90764/Python-solution-using-bfs-and-sets.
# 
# 
# 
# 
# 

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected
    
    # result = [[0, 1], [2, 8]...]

    # print(result == output_expected, '\n', output_expected, '\n', result)    

# ========== Tests =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
      else:
        output_expected = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
        pawf = PacificAtlanticWaterFlow(input, output_expected)
        if fn == 'bruteforce':
          pawf.bruteForce()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])