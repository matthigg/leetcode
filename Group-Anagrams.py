# Given an array of strings, group anagrams together.
# 
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

class GroupAnagrams:
  def __init__(self, input, output_expected):
    self.fn_name = 'hash table'
    self.input = input
    self.output_expected = output_expected

# ========== Hash Table ======================================================
# This approach creates a hash table using defaultdict(list) and inserts each
# string in the input list into the hashtable at a key that corresponds to
# that string's alphabetically-sorted list of characters, ie. the string 'cat'
# would get inserted into the hashtable at the key 'act', where 'act' is the
# alphabetically-sorted list of characters contained in 'cat'.
#
# The alphabetically-sorted list of characters, then, is the key that determines
# whether or not a string belongs to that "group" of anagrams.
# 
# Time complexity: O(n log(n)) - we have two seperate FOR loops, each of which run
# in O(n) time, and the sorted() function, which runs in O(n log(n)) time. This
# gives an overall time complexity of O(n log(n)), since it has a greater effect
# than O(n).
# 
# Space complexity: O(n) - each 'n' elements in the input list are stored in the 
# anagram_dict{}, as well as the anagram_list[], each of which adds O(n) space
# complexity. However, some people debate as to whether extra space needed to
# return the output from the input is counted towards space complexity, ie.,
# anagram_list would not in this case.

  def hashTable1(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # If there is only one string then return it
    if len(input) < 2:
      result.append(input)
      print(result == output_expected)
      return

    # Create an anagram dictionary of key:list[] pairs
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    for string in input:
      anagram_key = ''.join(sorted(string))
      anagram_dict[anagram_key].append(string)

    # Append each group of anagrams to anagram_list[]
    anagram_list = []
    for key in anagram_dict:
      anagram_list.append(anagram_dict[key])
    
    result = [sorted(x) for x in anagram_list]
    print(result == output_expected)

# This is the same as the solution above, except that it turns the anagram_dict
# keys into sorted characters in tuples instead of sorted strings, and it uses
# the dictionary *.values() method to return a view object, which is then 
# converted into a list via the list() function.
# 
# Time complexity: O(n log(n)) - the sorted() function's time complexity dominates
# over the time complexity of the FOR loop.
# 
# Space complexity: O(n) - this could also be considered O(1) if you do -not-
# count the space used to return the output from the input.

  def hashTable2(self):
    input, output_expected = self.input, self.output_expected

    # If there is only one string then return it
    if len(input) < 1:
      result = input
      print(result == output_expected)
      return

    # Create an anagram dictionary of key:list[] pairs
    from collections import defaultdict
    anagram_dict = defaultdict(list)
    for string in input:
      anagram_dict[tuple(sorted(string))].append(string)

    # Convert the View Object returned by *.values() into a list
    anagram_list = list(anagram_dict.values())
    
    result = [sorted(x) for x in anagram_list]
    print(result == output_expected)
    
# ========== Test =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n').split(' ')
      else:
        output_expected = [x.split(' ') for x in line.strip('\n').split(', ')]
        ga = GroupAnagrams(input, output_expected)        
        if fn == 'hashTable1':
          ga.hashTable1()
        if fn == 'hashTable2':
          ga.hashTable2()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])