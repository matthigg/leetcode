# Given an array nums of n integers, are there elements a, b, c in nums such 
# that a + b + c = 0? Find all unique triplets in the array which gives the sum 
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ] 

class ThreeSum:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Brute Force =======================================================
# This approach uses a 3x FOR loop.
# 
# Time complexity: O(n^3) - I think it's O(n^3) because it has 3 loops, one of
# which is nested inside 1 loop, and one of which is nested inside of 2 loops.
# 
# Space complexity: O(n) - you could theoretically have 'n' number of elements
# inside of results[]

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected
    results = []

    # Exit function of input[] has fewer than 3 elements
    if len(input) < 3:
      results.append(input)
      print(results == output_expected)
      return

    # 3x loop
    for i in range(len(input) - 2):
      for j in range(i + 1, len(input) - 1):
        for  k in range(j + 1, len(input)):
          if (input[i] + input[j] + input[k]) == 0:
            sorted_triplets = sorted([input[i], input[j], input[k]])
            if sorted_triplets not in results:
              results.append(sorted_triplets)

    # print(results, output_expected)
    print(result == output_expected)

# ========== Hash Table =========================================================
# Create a counter hash table that keeps count of how many occurences of each
# integer occur within the input[] list. Use a 2x FOR loop to go through input[],
# calculating a hypothetical 'triplet' integer for each i'th and j'th element
# that satisfies the condition a + b + c = 0, check that this 'triplet' integer
# actually exists, and then insert it into the result[] list and return the list.
# 
# Time complexity: O(n^2) - the 2x FOR loop has the largest effect on time.
# 
# Space complexity: O(n) - a hash table of 'n' elements is created, as well as
# a result list which could contain up to 'n' elements

  def hashTable(self):
    input, output_expected = self.input, self.output_expected
    result = []  

    # Exit function of input[] has fewer than 3 elements
    if len(input) < 3:
      result.append(input)
      print(result == output_expected)
      return

    # Create hash table
    hash_table = {}
    for value in input:
      if value not in hash_table:
        hash_table[value] = 1
      else:
        hash_table[value] += 1
    
    for i in range(len(input) - 1):
      for j in range(i + 1, len(input)):

        # Create a hypothetical 'triplet' value to satisfy the a + b + c = 0 
        # condition
        negative_triplet = input[i] + input[j]
        triplet = -(negative_triplet)
        triplet_actually_exists = True
        
        # Make sure calculated 'triplet' value occurs at least twice in input[] if 
        # it equals a value that actually occurs in input[]
        if (triplet == input[i] or triplet == input[j]) and hash_table[triplet] < 2:
          triplet_actually_exists = False

        # Handles case when triplet, input[i], and input[j] all == 0
        if triplet == input[i] and triplet == input[j] and hash_table[triplet] < 3:
          triplet_actually_exists = False

        # Handle cases when the calculated triplet actually exists in input[]
        if triplet in hash_table  and triplet_actually_exists and sorted([input[i], input[j], triplet]) not in result:
          result.append(sorted([input[i], input[j], triplet]))

    print(result == output_expected)

# ========== Pointers ==========================================================
# This problem uses a sorted list and 3 pointers that traverse it: left, right, and
# 'i'. The left pointer starts from the left end with the lower values and quickly
# moves right, the right pointer starts at the right end with the higher values and
# quickly moves left, and the 'i' pointer starts left and slowly sweeps right.
# 
# So for example, in a sorted list with an L pointer at the beginning, an R pointer
# at the end, and an 'i' pointer represented by a FOR loop counter, we can evaluate
# the values at the three pointers and see if they add up to 0. 
#
# As we iterate through the FOR loop via the 'i' counter, if the sum of the values
# at the indices of the pointers adds up to greater than 0, that means that we 
# need to decrement the R pointer by 1 space to the left, or towards the 
# beginning/lower numbers. If the sum is still greater than 0, we can do it again.
#
# Similarly, if the sum is less than 0, we can bump up the L pointer by one space
# to the right, towards greater numbers, and start to approach 0.
#
# This means that as the 'i' pointer/counter traverses the list, the R and L
# pointers are continuously moving, or "honing in" on the two triplets that,
# in conjunction with the value at 'i', can potentially add up to be 0.
#
# As for the initial positioning of the pointers, 'i' acts like any counter and
# traverses the entire list, from list[0] to list[n]. L starts at the second
# element, i + 1, and R starts at the last element, list[len(input) - 1].
#
# Time complexity: O(n^2)
#
# Space complexity:

  def threePointers(self):
    input, output_expected = self.input, self.output_expected
    input.sort()
    result = []
    
    # Exit function of input[] has fewer than 3 elements
    if len(input) < 3:
      result.append(input)
      print(result == output_expected)
      return

    # Traverse the list using 3 pointers to find sum == 0 if it exists
    skip_duplicate = False
    for i in range(len(input)):

      # Set up a "guard" that will skip an i'th element in the loop if it is a
      # duplicate of the previous element
      if skip_duplicate:
        if i + 1 < len(input) and input[i] == input[i + 1]:
          continue
        else:
          skip_duplicate = False
          continue

      L = i + 1
      R = len(input) - 1
      while L < R:
        total = input[i] + input[L] + input[R]
        if total == 0:
          result.append([input[i], input[L], input[R]])

          # Allow L pointer to skip duplicates
          L_val = input[L]
          while L < len(input) and input[L] == L_val:
            L += 1

          # Allow R pointer to skip duplicates
          R_val = input[R]
          while R > L and input[R] == R_val:
            R -= 1

        elif total < 0:
          L += 1
        elif total > 0:
          R -= 1

      # Allow 'i' pointer to skip duplicates
      if i + 1 < len(input) and input[i] == input[i + 1]:
        skip_duplicate = True

    print(sorted(result) == output_expected)

# ========== Test ==============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
        ts = ThreeSum(input, output_expected)
        if fn == 'bruteForce':
          ts.bruteForce()
        if fn == 'hashTable':
          ts.hashTable()
        if fn == 'threePointers':
          ts.threePointers()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])