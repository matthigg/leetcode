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

# ========== Brute Force ======================================================
# 
# 
# Time complexity:
# 
# Space complexity:

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected
    result = ''
    s, t = input[0], input[1]

    import sys
    min_size = sys.maxsize
    L = 0
    R = 0

    t_set = set()
    def regenerate_t_set():
      for i in t:
        t_set.add(i)
    regenerate_t_set()

    recording = False
    current_string = ''
    while R < len(s):

      if s[R] in t_set:
        t_set.remove(s[R])
        recording = True
      R += 1

      if len(t_set) == 0:
        print(min_size, R - L)
        min_size = min(min_size, R - L)
        L = R
        regenerate_t_set()
        recording = False

      if recording == False:
        L = R

    # print(t_set, min_size)





    # print(s, t, output_expected)
    # print(result = output_expected, output_expected, result)

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
        if fn == 'bruteForce':
          mws.bruteForce()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])
