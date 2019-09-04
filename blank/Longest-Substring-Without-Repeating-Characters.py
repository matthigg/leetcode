# Given a string, find the length of the longest substring without repeating 
# characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# Note that the answer must be a substring, "pwke" is a subsequence and not a 
# substring.

class LongestSubstringWithoutRepeatingCharacters:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Practice ======================================================

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected

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
        lswrc = LongestSubstringWithoutRepeatingCharacters(input, output_expected)
        if fn == 'blank':
          lswrc.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])