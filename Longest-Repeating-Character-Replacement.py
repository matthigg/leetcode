# Given a string s that consists of only uppercase English letters, 
# you can perform at most k operations on that string.
#
# In one operation, you can choose any character of the string and 
# change it to any other uppercase English character.
#
# Find the length of the longest sub-string containing all repeating 
# letters you can get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 104.
#
# Example 1:
# 
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
# Example 2:
# 
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

class LongestRepeatingCharacterReplacement:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Sliding Window =========================================

  def slidingWindow(self):
    input, output_expected = self.input, self.output_expected
    s = input[0]
    k = input[1]

    longest_window = 0
    from collections import defaultdict
    window_counts = defaultdict(int)
    l = 0
    for r in range(len(s)):
      window_counts[s[r]] += 1
      print(window_counts.values(), max(window_counts.values()))
      while r - l + 1 - max(window_counts.values()) > k:
        window_counts[s[l]] -= 1 
        l += 1
      longest_window = max(longest_window, r - l + 1)
    return longest_window

# ========== Tests ==================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        s = line.strip('\n').split(', ')[0]
        k = int(line.strip('\n').split(', ')[1])
        input = [s, k]
      else:
        output_expected = int(line.strip('\n'))
        lrcr = LongestRepeatingCharacterReplacement(input, output_expected)
        lrcr.slidingWindow()

# ========== Command Line Arguments =================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])