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

# ========== Brute Force ======================================================
# This method uses a 2x FOR loop to go through the 2D grid. When it finds land,
# it automatically ups the 'islands' counter and then marks any adjacent islands
# with a hash-mark '#' using the dfs() function (depth-first search?). I'm not
# sure why it's necessary to segregate code into a dfs() function as opposed to
# just including it in the main function, but doing so causes one of the tests
# to fail and I need to look into this later.
# 
# Time complexity: O(n^2) - 2X FOR loops
# 
# Space complexity: O(1) - We're using several variables and the land[] list
# which at most would contain 4 tuples representing coordinates of surrounding
# land

  def bruteForce(self):
    grid, output_expected = self.input, self.output_expected
    result = 0

    islands = 0

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
      for j in range(n):
        if grid[i][j] == 1:
          islands += 1
          self.dfs(grid, i, j, m, n)

    result = islands
    print(result == output_expected, output_expected, result)

  def dfs(self, grid, i, j, m, n):
    land = [(i, j)]
    while land:
      i, j = land.pop()
      grid[i][j] = '#'

      if j > 0 and grid[i][j - 1] == 1:
        land.append((i, j - 1))
      if j < n - 1 and grid[i][j + 1] == 1:
        land.append((i, j + 1))
      if i > 0 and grid[i - 1][j] == 1:
        land.append((i - 1, j))
      if i < m - 1 and grid[i + 1][j] == 1:
        land.append((i + 1, j))

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