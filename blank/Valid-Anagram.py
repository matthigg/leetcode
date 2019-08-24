# Given two strings s and t , write a function to determine if t is an anagram 
# of s.
#
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?

class ValidAnagram:
  def __init__(self, input_A, input_B, output_expected):
    self.input_A = input_A
    self.input_B = input_B
    self.output_expected = output_expected

# ========== Practice =========================================================

  def blank(self):
    input_A, input_B, output_expected = self.input_A, self.input_B, self.output_expected
    result = 'False'

    # blank, result = 'True'/'False'

    print(output_expected == result)

# ========== Test =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input_A = line.strip('\n').split(' ')[0]
        input_B = line.strip('\n').split(' ')[1]
      else:
        output_expected = line.strip('\n')
        va = ValidAnagram(input_A, input_B, output_expected)
        if fn == 'blank':
          va.blank()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])