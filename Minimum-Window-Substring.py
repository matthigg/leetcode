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

# ========== Sliding Window ===================================================
# In any sliding window based problem we have two pointers. One right pointer 
# whose job is to expand the current window and then we have the left pointer 
# whose job is to contract a given window. At any point in time only one of 
# these pointers move and the other one remains fixed.
#
# The solution is pretty intuitive. We keep expanding the window by moving the 
# right pointer. When the window has all the desired characters, we contract 
# (if possible) and save the smallest window till now.
#
# The answer is the smallest desirable window.
# 
# Time complexity: O(n) - we traverse the 's' string with 2 pointers, and the 't'
# string once when we create a Counter dictionary.
# 
# Space complexity:

  def slidingWindow(self):
    input, output_expected = self.input, self.output_expected
    result = ''
    s, t = input[0], input[1]

    # If 's' == 't', then 's' is the smallest string that contains all of the 
    # characters in 't' and we can return
    if s == t:
      result = s
      print(result == output_expected, output_expected, result)
      return
    if len(s) < len(t):
      result = 'no_substring_found'
      print(result == output_expected, output_expected, result)
      return

    # Create a Counter dictionary
    from collections import Counter
    tcount = Counter(t)

    # Sliding window
    R = L = 0
    substring_found = False
    substring = ()
    min_substring = (len(s), 0, 0)
    while R < len(s):
      if s[R] in tcount:
        tcount[s[R]] -= 1

        while all(value <= 0 for value in tcount.values()):
          substring = (R - L, L, R)
          if substring[0] < min_substring[0]:
            substring_found = True
            min_substring = substring
          if s[L] in tcount:
            tcount[s[L]] += 1
          L += 1

      R += 1

    # Return results
    result = s[min_substring[1]:min_substring[2] + 1]
    if substring_found == False:
      result = 'no_substring_found'
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
        if fn == 'slidingWindow':
          mws.slidingWindow()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])
