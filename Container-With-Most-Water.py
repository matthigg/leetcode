# Given n non-negative integers a1, a2, ..., an , where each 
# represents a point at coordinate (i, ai). n vertical lines are 
# drawn such that the two endpoints of line i is at (i, ai) and 
# (i, 0). Find two lines, which together with x-axis forms a 
# container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# ========== Practice =============================================

def iterative(input, output_expected):

  L = 0
  R = len(input) - 1
  area = min(input[L], input[R]) * (R - L)

  while L < R:
    current_area = min(input[L], input[R]) * (R - L)
    if current_area > area:
      area = current_area
    if input[L] < input[R]:
      L += 1
    else:
      R -= 1

  print(area == output_expected, '\n', area, '\n', output_expected)

# ========== Tests ================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(', ')]
      else:
        output_expected = int(line.strip('\n'))
        iterative(input, output_expected)

# ========== Command Line Arguments ===============================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])