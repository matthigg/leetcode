# Given a string S and a string T, find the minimum window in S which will 
# contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the 
# empty string "".
# If there is such window, you are guaranteed that there will always be only 
# one unique minimum window in S.

class MinimumWindowSubstring:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice =========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = ''
    s, t = input[0], input[1]

    # blank, result = string

    print(result == output_expected, output_expected, result)

# ========== Tests ============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n').split(', ')
      else:
        output_expected = line.strip('\n')
        mws = MinimumWindowSubstring(input, output_expected)
        if fn == 'blank':
          mws.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])
