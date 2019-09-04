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

# ========== Brute Force ======================================================
# This brute force method uses a combination of 2x FOR loops + a hash table.
# The idea is to find the longest contiguous substring of -unique- characters,
# we use the 2X FOR loop to go through the string and add individual characters
# to the hash table if they are not already stored and add +1 to the current
# string length, ie. cur_len. However, if the character is already stored in
# the hash table then we break out of the inner FOR loop and continue.
#
# Time complexity: O(n^2) - 2X FOR loops
#
# Space complexity: O(k) - the extra space we need includes a few variables, which
# take up O(1) space, and a hash table. The size of the has table, 'k', has an
# upper bound of 'n', the size of the string, and 26, which is the size of the
# alphabet

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected
    result = 0

    if len(input) == 0:
      result = 0
      print(result == output_expected, output_expected, result)
      return
    elif len(input) == 1:
      result = 1
      print(result == output_expected, output_expected, result)
      return
    
    hash_table = set()
    cur_len = 0
    for i in range(len(input) - 1):
      for j in range(i, len(input)):
        if input[j] not in hash_table:
          hash_table.add(input[j])
          cur_len += 1
          if cur_len > result:
            result = cur_len
        else:
          cur_len = 0
          hash_table = set()
          break

    print(result == output_expected, output_expected, result)

# ========== Sliding Window ===================================================
# This solution uses 2 pointers to move across a string. If the character in the
# string at the R pointer does not currently exist in the hash table, then the
# character is added to the hash table and the R pointer increases by 1.
#
# If the character -does- exist in the hash table, representing a duplicate
# character, then the -last- character in the hash table is removed (or more
# specifically, the character at hash_table[L], since hash tables are unordered)
# and the L pointer increases by 1.
#
# It may seem strange to remove the "last" character in the hash table (which is
# actually the character pointed at by the L pointer), but since the R and L 
# pointers represent a sliding window, the L pointer will continually remove 
# characters from the hash table until the duplicate character is removed. This
# ensures that the hash table, while unordered, represents a contiguous string
# of unique characters.
#
# By using the R and L pointers as a "sliding window" over a substring of the
# parent string, this algorithm updates the hash table to reflect the contents
# of the substring by adding and removing characters when necessary.
#
# Time complexity: O(n) - the R pointer traverses the string once, and the L 
# pointer may or may not traverse the entire string, so time complexity at worst
# is O(2n) which is usually just expressed as O(n)
#
# Space complexity: O(k) - the size of the hash table is upper bound by the size
# of the string and the letters of the alphabet (or whatever set of letters/
# capitalized letters/numbers/etc. that you want to include in the input string).

  def slidingWindow(self):
      input, output_expected = self.input, self.output_expected
      result = 0

      if len(input) == 0:
        result = 0
        print(result == output_expected, output_expected, result)
        return
      elif len(input) == 1:
        result = 1
        print(result == output_expected, output_expected, result)
        return

      hash_table = set()
      L = 0
      R = 0
      while L < len(input) and R < len(input):
        if input[R] not in hash_table:
          hash_table.add(input[R])
          R += 1
          result = max(result, R - L)
        else:
          hash_table.remove(input[L])
          L += 1
          
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
        if fn == 'bruteForce':
          lswrc.bruteForce()
        elif fn == 'slidingWindow':
          lswrc.slidingWindow()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])