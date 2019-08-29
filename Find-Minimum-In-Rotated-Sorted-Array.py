# Suppose an array sorted in ascending order is rotated at some pivot 
# unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
# 
# Example 1:
#
# Input: [3,4,5,1,2] 
# Output: 1
# Example 2:
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
# Note - this can easily be solved using Python's built-in min()
# function, or by sorted the list and then grabbing list[0], but
# another way to accomplish it is using "binary search".
#

# ========== Binary Search ==========================================
# A very brute way of solving this question is to search the entire 
# array and find the minimum element. The time complexity for that 
# would be O(N)O(N) given that N is the size of the array.
#
# A very cool way of solving this problem is using the Binary Search 
# algorithm. In binary search we find out the mid point and decide to 
# either search on the left or right depending on some condition.
#
# Since the given array is sorted, we can make use of binary search. 
# However, the array is rotated. So simply applying the binary search 
# won't work here.
#
# In this question we would essentially apply a modified version of 
# binary search where the condition that decides the search direction 
# would be different than in a standard binary search.
#
# We want to find the smallest element in a rotated sorted array. What 
# if the array is not rotated? How do we check that?
#
# If the array is not rotated and the array is in ascending order, 
# then last element > first element.
# 
#       [2, 3, 4, 5, 6, 7]
#
# In the above example 7 > 2. This means that the array is still 
# sorted and has no rotation.
#
#       [4, 5, 6, 7, 2, 3]
#
# In the above example 3 < 4. Hence the array is rotated. This happens 
# because the array was initially [2, 3 ,4 ,5 ,6 ,7]. But after the 
# rotation the smaller elements[2,3] go at the back. i.e. 
# [4, 5, 6, 7, 2, 3]. Because of this the first element [4] in the 
# rotated array becomes greater than the last element.
#
# This means there is a point in the array at which you would notice 
# a change. This is the point which would help us in this question. 
# We call this the Inflection Point.
#
# All the elements to the left of inflection point > first element of the array.
# 
# Algorithm
# 
# Find the mid element of the array.
#
# If mid element > first element of array this means that we need to 
# look for the inflection point on the right of mid.
#
# If mid element < first element of array this that we need to look 
# for the inflection point on the left of mid.
#
#       [4, 5, 6, 7, 2, 3]
#
# In the above example mid element 6 is greater than first element 4. 
# Hence we continue our search for the inflection point to the right 
# of mid.
#
# 4 . We stop our search when we find the inflection point, when 
# either of the two conditions is satisfied:
# 
# nums[mid] > nums[mid + 1] Hence, mid+1 is the smallest.
#
# nums[mid - 1] > nums[mid] Hence, mid is the smallest.
#
# In the above example. With the marked left and right pointers. 
# The mid element is 2. The element just before 2 is 7 and > 2, i.e. 
# nums[mid - 1] > nums[mid]. Thus we have found the point of 
# inflection and 2 is the smallest element.
#
# Time complexity: O(log(n)) - binary search typically takes log(n)
# time, making it faster than Python's built-in min() function, which
# runs at O(n) time, and faster than sorting the array which runs
# in n(log(n)) time.
#
# Space complexity: O(1) - we use two pointers and a return variable

def binarySearch(input, output_expected):
  result = 0

  # Example of a rotated array: [4, 5, 6, 7, 1, 2, 3]

  # Pointers to the first and last indexes
  L = 0
  R = len(input) - 1

  # If the input contains only 1 element, return
  if len(input) <= 1:
    result = input[0]
    print(result == output_expected, '\n', result, '\n', output_expected)
    return

  # If input[0] is less than input[-1] then the array has not been
  # rotated
  if input[L] < input[R]:
    result = input[L]
    print(result == output_expected, '\n', result, '\n', output_expected)
    return

  # Binary search
  while L < R:
    mid_pt = L + (R - L) // 2

    # If the inflection point is found then return it
    if input[mid_pt] > input[mid_pt + 1]:
      result = input[mid_pt + 1]
      print(result == output_expected, '\n', result, '\n', output_expected)
      return
    elif input[mid_pt] < input[mid_pt - 1]:
      result = input[mid_pt - 1]
      print(result == output_expected, '\n', result, '\n', output_expected)
      return

    # If the inflection point is not found, continue binary search by
    # moving L or R pointers in the general direction of the inflection 
    # point
    elif input[mid_pt] > input[R]:
      L = mid_pt
    elif input[mid_pt] < input[R]:
      R = mid_pt

  # print(result == output_expected, '\n', result, '\n', output_expected)
  
# This is a more condensed version of the above code.
#
# Time complexity: O(log(n))
#
# Space complexity: O(1)

def binarySearch2(input, output_expected):

  start = 0
  end = len(input) - 1

  while start < end:
    mid = (start + end) // 2
    if input[mid] > input[end]:
      start = mid + 1
    else:
      end = mid
      
  print(input[start] == output_expected, '\n', input[start], '\n', output_expected)
  return

# ========== Tests ==================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(', ')]
      else:
        output_expected = int(line.strip('\n'))
        if fn == 'binarySearch':
          binarySearch(input, output_expected)

# ========== Command Line Arguments =================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])