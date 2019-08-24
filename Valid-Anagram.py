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

# ========== Sort =============================================================
# An anagram is produced by rearranging the letters of s into t. Therefore, if 
# t is an anagram of s, sorting both strings will result in two identical 
# strings. Furthermore, if s and t have different lengths, t must not be an 
# anagram of s and we can return early (not shown, but useful optimization trick)
#
# Time complexity: O(n log(n)) - sorting costs O(n log(n)) time, and comparing
# two strings costs O(n), but sorting time is the larger of the two so it 
# dominates.
#
# Space complexity: O(n) - the sorted() function returns a new list, either as a
# copy of an existing list, or as a list that represents the characters of a
# string. 

  def sortStrings(self):
    input_A, input_B, output_expected = self.input_A, self.input_B, self.output_expected
    result = 'False'

    # Empty string is an anagram of itself
    if len(s) == 0 and len(t) == 0: 
      result = 'True'
      print(output_expected == result)
      return

    # Anagram requires 2 strings of equal length
    if len(s) != len(t):
      print(output_expected == result)
      return

    if sorted(input_A) == sorted(input_B):
      result = 'True'

    print(output_expected == result)

# ========== Hash Table =======================================================
# We can make 3 passes -- on the first pass we create a hash table out of string
# 's'. On the second pass we subtract every character in string 't' from the
# hash table. On the third pass we check that the count for each character/key in
# the hash table == 0.
#
# Time complexity: O(n) - each pass takes O(n) time
#
# Space complexity: O(n) - a hash table of length == 'n' elements is created

  def hashTable1(self):
    input_A, input_B, output_expected = self.input_A, self.input_B, self.output_expected
    result = 'False'

    # Empty string is an anagram of itself
    if len(input_A) == 0 and len(input_B) == 0: 
      result = 'True'
      print(output_expected == result)
      return

    # Anagram requires 2 strings of equal length
    if len(input_A) != len(input_B):
      print(output_expected == result)
      return

    # Loop I
    # Use one of the input strings to create a hash table with values that represent 
    # counters for each individual character in the string
    hash_table = {}
    for i in input_A:
      if i not in hash_table:
        hash_table[i] = 1
      else:
        hash_table[i] += 1
    
    # Loop J
    # Use the other input string's individual characters to decrement the 
    # corresponding counts in the hash table, and exit early if a corresponding 
    # character isn't found
    for j in input_B:
      if j not in hash_table:
        print(output_expected == result)
        return
      else:
        hash_table[j] -= 1

    # Loop K
    # Iterate through the hash table to check whether or not all counts are 0 --
    # if not, then it means that at least one counter was not decremented by Loop J,
    # and the two strings are not anagrams, otherwise they are
    for k in hash_table:
      if hash_table[k] != 0:
        print(output_expected == result)
        return
      else:
        result = 'True'

    print(output_expected == result)

# This hash table uses the Counter() function from the 'collections' module, which
# turns an iterable into a dictionary with key:value pairs where key == iterable's 
# value, and value == an integer counter. For example, Counter('aabc') == 
# {'a': 2, 'b': 1, 'c': 1}. Additionally, the all() function returns True when 
# all elements in the given iterable are true. If not, it returns False.
# 
# Time complexity: O(n) - Counter is a subclass of dict, and it turns iterables
# into dictionaries in O(n) time. The list comprehension's FOR loop traverses
# the cs and ct dictionary in O(n) time, and the len() function operates in O(1)
# time.
# 
# Space complexity: O(n) - two hash tables are created, 'cs' and 'ct'

  def hashTable2(self):
    input_A, input_B, output_expected = self.input_A, self.input_B, self.output_expected
    result = 'True'

    # Create hash tables using the Counter() function, which act like a normal
    # dict{}'s except that they return 0 for missing items instead of raising a 
    # KeyError
    from collections import Counter
    hash_table_A = Counter(input_A)
    hash_table_B = Counter(input_B)

    # If the hash tables contain a different number of keys, result is False
    if len(hash_table_A) != len(hash_table_B):
      result = 'False'

    # If a key in hash_table_A is not found in hash_table_B, then 
    # hash_table_B[key] returns 0.
    for key in hash_table_A:
      if hash_table_A[key] != hash_table_B[key]:
        result = 'False'

    print(output_expected == result)

    # Evaluate everything and return the result on one line
    # return all([hash_table_A[key] == hash_table_B[key] for key in hash_table_A]) and len(hash_table_A) == len(hash_table_B)

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
        if fn == 'sortStrings':
          va.sortStrings()
        if fn == 'hashTable1':
          va.hashTable1()
        if fn == 'hashTable2':
          va.hashTable2()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])