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

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected
    result = 'False'

    # Convert the input string to a list
    input = list(input)

    # If the input list is empty or only contains one parens, return
    if len(input) == 0:
      result = 'True'
      print(output_expected == result)
      return
    elif len(input) == 1:
      print(output_expected == result)
      return

    # 2x FOR loop
    for j in range(len(input) // 2):
      for i, paren in enumerate(input):
        
        # Assign open parentheses complements for closing parentheses characters
        complement = ''
        if paren == ')':
          complement = '('
        elif paren == ']':
          complement = '['
        elif paren == '}':
          complement = '{'

        # Remove adjacent opening/closing parentheses
        if input[i - 1] == complement:
          input[i - 1:i + 1] = []

        # If all parentheses have been removed, then the input string represents
        # valid parentheses
        if len(input) == 0:
          result = 'True'

    print(result == output_expected)

# ========== Stack =============================================================
# Create a hash table with key:value pairs consisting of key=CLOSING parens,
# ie. ), value=OPENING parens, ie. (, as well as a virtual "stack". Iterate 
# through the list of parentheses characters and compare them to the table --
# OPENING parens get pushed/appended to the stack, whereas CLOSING parens are
# evaluated and compared to the parens that currently exists on top of the 
# virtual stack, ie. stack[-1], which is essentially at the end of the stack[] 
# list. 
#
# If stack[-1] == hash[i] it means that the element on top of the virtual stack is 
# an OPENING parens that matches the value of the current closing parens according
# to the hash{} table, and if this is the case then then stack[-1] gets popped and
# that i, the current CLOSING parens, is ignored.
#
# Time complexity: O(n) - we traverse the list of parens once.
#
# Space complexity: O(n) - the virtual stack[] could potentially be up to 'n'
# elements in length.

  def stack(self):
    input, output_expected = self.input, self.output_expected
    result = 'False'

    # Convert the input string to a list
    input = list(input)

    # Create a hash table and stack[]
    hash_table = {')': '(', ']': '[', '}': '{'}
    stack = []

    # If the input list is empty or only contains one parens, return
    if len(input) == 0:
      result = 'True'
      print(output_expected == result)
      return
    elif len(input) == 1:
      print(output_expected == result)
      return

    # For each parens character in input[], append that character to the stack[]
    # if it is an opening tag.
    #
    # Otherwise, evalute whether or not its complement opening tag current exists
    # at the top of the stack -- if so, do nothing with it, and pop its complement
    # off of the top of the stack. Note -- if it does not have a complement at 
    # the top of the stack at this point, you could return, because the list of
    # parens is not valid
    for i in input:
      if i in hash_table and stack and hash_table[i] == stack[-1]:
        stack.pop()
      else:
        stack.append(i)

    # If the stack is valid then all parens should have been popped off of the
    # stack
    if len(stack) == 0:
      result = 'True'

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
        if fn == 'bruteForce':
          vp.bruteForce()
        if fn == 'stack':
          vp.stack()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])