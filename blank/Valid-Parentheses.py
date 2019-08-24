# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
#
# An input string is valid if:
#
#   1. Open brackets must be closed by the same type of brackets.
#   2. Open brackets must be closed in the correct order.
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
#
# Example 2:
#
# Input: "()[]{}"
# Output: true
#
# Example 3:
#
# Input: "(]"
# Output: false
#
# Example 4:
#
# Input: "([)]"
# Output: false
#
# Example 5:
#
# Input: "{[]}"
# Output: true

class ValidParentheses:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Brute Force ========================================================
# Create two FOR loops, where the outer loop traverses 1/2 of the length of the
# list of parentheses, and the inner loop looks for pairs of parentheses --
# specifically, (), [], or {}, and removes them if found. 
#
# Time complexity: O(n^2) - double FOR loop
#
# Space complexity: O(n) - since the list of parentheses actually comes in as a
# string, and part of the algorithm is removing pairs of parentheses, we need to
# convert the immutable string into a mutable object like a list, and the list
# takes up 'n' elements of space.

  def blank(self):
    input, output_expected = self.input, self.output_expected
    result = 'False'

    # blank, result = 'True'/'False'

    print(result == output_expected)

# ========== Test ==============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n')
      else:
        output_expected = line.strip('\n')
        vp = ValidParentheses(input, output_expected)
        if fn == 'blank':
          vp.blank()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])