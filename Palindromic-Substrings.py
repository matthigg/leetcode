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

# ========== Expand From Center ================================================
# The center of a palindrome exists at a single letter (if the palindrome has an
# odd number of characters) or between two letters (if the palindrome has an even
# number of letters). 
#
# In this approach, the FOR loop iterates over a range of numbers with an iterator
# that points to either a character in the 'input' string, -or- the idea of a 
# 'space' between each character. The iterator represents the center of a 
# potential palindrome substring.
# 
# For example, for a string with an odd number of characters like 'abc', that string
# would contain a range of 2 * 3 - 1 = 5 possible palindromic 'centers', where 5 
# accounts for 3 characters and 2 spaces.
# 
# For a string with an even number of characters like 'abcd', that string would
# contain a range of 2 * 4 - 1 = 7 possible palindromic 'centers', where 7 
# represents 4 characters and 3 spaces.
#
# The pointers L and R are designed to point to locations on the string and,
# unlike the range in the FOR loop, the pointers ignore the idea of a "space"
# between characters -- they actually move across the string in a pattern that
# resembles walking, were the L pointer moves forward, then the R pointer moves
# forward, over and over again across the length of the string. This puts them in
# a position where, if the conditions for a palindrome are met, they can start
# to expand outward.
#
# Time complexity: O(n^2) - As the L and R pointers walk across the string, as if
# they were being dragged by 'i' acting as a puppet master, they can potentially
# visit each character in the entire string for each corresponding 'center'
# character or space-between-characters in the range of 2 * N - 1.
# 
# Space complexity: O(1) - We're only using a few variables and pointers.

  def expandFromCenter(self):
    input, output_expected = self.input, self.output_expected
    result = 0

    # result = int
    N = len(input)
    for i in range(2 * N - 1):
      L = i // 2
      R = L + i % 2
      while L >= 0 and R < N and input[L] == input[R]:
        result += 1
        L -= 1
        R += 1

    print(result == output_expected, output_expected, result)

# ========== Manacher's Algorithm =============================================
# This algorithm basically has one purpose, which is to find the longest 
# palindrome substring in O(n), or linear time. In the 'expand at the center'
# algorithm we visit each character in the string potentially N^2 times; however,
# since palidromes are symmetric about their center (whether the center is a 
# character or a space between characters), during iteration if we have found a
# palindromic center then we know -something- about the remaining characters in
# the string that we have not yet visited -- we know that some of them will mirror
# the previous characters that have already been visited, since the definition of
# a palindrome is that the characters on the left of its center mirror the 
# characters on the right.
#
# The first step involves using the concept of 'separation', which basically 
# involves putting hash symbols, #, between characters to account for the idea of
# 'spaces' between characters, as well as putting hash symbols at the beginning
# and end of the string.
#
# The second step involves 'mirroring'. This step involves using an array with
# numbers that somehow correspond to the string which has had hash characters
# inserted between each pair of characters in the string in order to represent
# spaces between characters, ie. a string represented via 'separation'. For
# example:
#
#   string:               abaabc
#   string w/separation:  # a # b # a # a # b # c #
#   array 'p':            0 1 0 3 0 1 4 1 0 1 0 1 0
#   mirroring:              1 0 3 0 1
#
# So in this example, an array named 'p' has numbers that somehow correspond to
# the 'separated' string. Part of the array 'p' has numbers that seem to 'mirror'
# around a central number, in this case the number 3 (there are also other 
# mirrors, but 1 0 3 0 1 is the biggest and is easy to use for this example).
# 
# For the rest of the explanation, watch this:
# https://www.youtube.com/watch?v=nbTSfrEfo6M
#
# Time complexity: O(n)
# 
# Space complexity: O(n)

  def manachers(self):
    input, output_expected = self.input, self.output_expected
    result = 0

    # Pre-process the string using the concept of 'separation' -- basically,
    # add some hash marks between characters, and also to the beginning and
    # end of the string.
    separated_str = ''
    for char in input:
      separated_str += '#' + char
    separated_str += '#'
    print(separated_str)

    # 



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
        if fn == 'expandFromCenter':
          ps.expandFromCenter()
        if fn == 'manachers':
          ps.manachers()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])