# Given an array of integers, find if the array contains any duplicates.
#
# Your function should return true if any value appears at least twice in 
# the array, and it should return false if every element is distinct.
#
# Example 1:
#
# Input: [1,2,3,1]
# Output: true
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: false
#
# Example 3:
#
# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true

class ContainsDuplicate:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Linear Search, J Sweeps to Right ===================================
# Loop through the input[] list using 2x FOR loops to detect duplicates, where
# the inner FOR loop pointer, 'j', starts at i + 1 and sweeps -right-.
#
# Time complexity: O(n^2) - double FOR loops.
#
# Space complexity: O(n) - the inner FOR loop creates a shallow copy of
# the list through each iteration of the outer FOR loop.

  def linearSearchRight(self):
    input, output_expected = self.input, self.output_expected

    result = False
    for i in range(len(input) - 1):
      for j in range(i + 1, len(input)):
        if input[i] == input[j]:
          result = True
          break

    print(result == output_expected)

# ========== Linear Search, J Sweeps from Left ==================================
# This is basically the same idea as the brute force method above, except
# the inner FOR loop sweeps from 0 towards the i'th element from the -left-.
#
# Time complexity: O(n^2) - although it may be possible that a duplicate
# is found early in the list, in the worst case a duplicate exists at the
# end, and since this a double FOR loop the time complexity is O(n^2).
#
# Space complexity: O(n) - in the worst case, the inner FOR loop slice will
# take up n - 1 space (since the last index's element in a slice is not 
# inclusive).

  def linearSearchLeft(self):
    input, output_expected = self.input, self.output_expected

    result = False
    for i in range(len(input)):
      for j in range(i):
        if input[i] == input[j]:
          result = True
          break

    print(result == output_expected)

# ========== Sorting ===========================================================
# If there are any duplicate integers, they will be consecutive after 
# sorting.
#
# Time complexity: O(n log(n)) - Python's *.sort() method is a hybrid between
# merge sort and insertion sort, also known as "Timsort" after its creator,
# Tim Peters.
# 
# Space complexity: O(1) - since the nums list is sorted in place, no extra
# memory allocation is necessary

  def sortList(self):
    input, output_expected = self.input, self.output_expected

    input.sort()
    result = False
    for i, v in enumerate(input):
      if v == input[i - 1] and (i - 1) >= 0: # len(list) == 1, false positive
        result = True

    print(result == output_expected)

# ========== Hash Table =================================================
# This is a one-pass hash table where we are checking for duplicates while
# constructing the hash table
#
# Time complexity: O(n) - one-pass hash table that checks for duplicates
# as the table is being constructed
#
# Space complexity: O(n) - the constructed hash table consists of up to 'n'
# elements

  def hashTable(self):
    input, output_expected = self.input, self.output_expected

    hash = {}
    result = False
    for value in input:
      if value in hash.keys():
        result = True
        break
      hash[value] = 'exists'

    print(result == output_expected)
  
# ========== Set ========================================================
# Since sets eliminate duplicates, you can deduce whether or not a list 
# contains duplicates by comparing the length of the list to the length of
# the set
#
# Time complexity: O(n) - the len() function takes O(1) time, but the set()
# function takes O(n) time (I think), since the set() function in Python
# has to iterate over an iterable (like a list) and then insert the elements
# into a hash table. Sets, therefore, are basically hash tables -- this
# accounts for why they will only allow unique values, since hash tables will
# only allow unique keys.
#
# Space complexity: O(n) - creation of a set takes up (n - # of duplicates)
# in terms of space

  def createSet(self):
    input, output_expected = self.input, self.output_expected

    result = False
    if len(input) != len(set(input)):
      result = True

    print(result == output_expected)

# ========== Tests ======================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.split(' ')]
      else:
        if line == 'True\n':
          output_expected = True
        else:
          output_expected = False
        cd = ContainsDuplicate(input, output_expected)
        if fn == 'linearSearchRight':
          cd.linearSearchRight()
        if fn == 'linearSearchLeft':
          cd.linearSearchLeft()
        if fn == 'sortList':
          cd.sortList()
        if fn == 'hashTable':
          cd.hashTable()
        if fn == 'createSet':
          cd.createSet()

# ========== Command Line Arguments ======================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])