# Given a string, your task is to count how many palindromic substrings in this 
# string.
#
# The substrings with different start indexes or end indexes are counted as 
# different substrings even they consist of same characters.
#
# Example 1:
#
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
#
# Example 2:
#
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class PalindromicSubstrings:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice ========================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = 0

    # blank, result = int

    print(result == output_expected, output_expected, result)

# ========== Tests ============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n')
      else:
        output_expected = int(line.strip('\n'))
        ps = PalindromicSubstrings(input, output_expected)
        if fn == 'blank':
          ps.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])