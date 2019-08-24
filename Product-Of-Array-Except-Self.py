# Given an array nums of n integers where n > 1,  return an array output such 
# that output[i] is equal to the product of all the elements of nums except 
# nums[i].
#
# Example:
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not 
# count as extra space for the purpose of space complexity analysis.)

class ProductOfArrayExceptSelf:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Brute Force =======================================================
# Double FOR loops iterate over the entire input[] list and outputs a new list 
# where each element in the output[] list is the product of every element in the 
# input[] list, excluding the input[] list element with the same index as the 
# output[] list element.
#
# Time complexity: O(n^2) - 2x FOR loops.
#
# Space complexity: O(n) - the output[] list takes up 'n' elements worth of space

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # 2x FOR loop
    for i, v in enumerate(input):
      product = 1
      for j, k in enumerate(input):
        if i != j:
          product *= k
      result.append(product)

    print(result == output_expected)

# ========== Division ==========================================================
# Multipling all values in the array and dividing this "max product" value by
# an element will give a result that represents the product of the array -except-
# self, or except that element/the divisor.
#
# In other words,
#
#   max product (dividend) / element (divisor) = product of array except self
#
# Doing this for each of the elements would solve the problem. However, there's 
# a note in the problem which says that we are not allowed to use division 
# operation. However, this example uses it anyways just for illustration.
#
# Note -- also, this problem doesn't clarify whether or not 0's are allowed, in
# which case divison by 0 messes up this approach due to division by zero, unless 
# you account for that
#
# Time complexity: O(n^2) - there are two FOR loops, each of which loop over 'n'
# elements in input[].
#
# Space complexity: O(n) - the output[] list is 'n' elements long.

  def division(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # Find the product of every element in the list, ie. the "max product"
    product = 1
    for x in input:
      product *= x

    # Whenever a 0 is encountered, a new "max product", called the "zero_product",
    # is calculated - whether there is a single 0 or multiple 0's in the list, 
    # the IF condition prevents division by zero
    for i, value in enumerate(input):
      if value == 0:
        zero_product = 1
        for j, k in enumerate(input):
          if i != j:
            zero_product *= k
        result.append(zero_product)     
      else:
        result.append(product // value)

    print(result == output_expected)

# ========== Log ===============================================================
# This approach uses the property of logarithms, aka exponents (since logs are
# exponents), that allows you to add the exponents of two numbers together when
# those two numbers are being multiplied. For example, (x^2) * (x^3) == (x^5).
# The same holds true with division & subtraction.
#
# With logs, a similar example would be x = log(10 * 20) = log(10) + log(20). With
# division, x = log(10 / 20) == log(10) - log(20). After that, take the antilog 
# via 10^x.
#
# Note: in Python, to use the log() function, you have to import the log() 
# function from the math module. The log() function's syntax is log(value, base), 
# where base == e by default.
#
# Note: you can't take the log of a negative number.
#
# Note: there are rounding issues that prevent this method from passing some
# tests.
#
# Time complexity: O(n) - there are several loops that iterate over input.
#
# Space complexity: O(n) - the output[] list contains 'n' elements.

  def logDivision(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # Find the product of every element in the list, ie. the "max product"
    product = 1
    for x in input:
      product *= x

    # Whenever a 0 is encountered, a new "max product", called the "zero_product",
    # is calculated - whether there is a single 0 or multiple 0's in the list, 
    # the IF condition prevents division by zero
    for i, value in enumerate(input):
      if value == 0:
        zero_product = 1
        for j, k in enumerate(input):
          if i != j:
            zero_product *= k
        result.append(zero_product)     
      else:
        if product == 0:
          result.append(0)
        else:

          # Note - rounding issues prevent this algorithm from passing some tests
          from math import ceil, floor, log
          result.append(ceil(10 ** (log(product, 10) - log(value, 10))))

    print(result == output_expected)

# ========== Left and Right Arrays =============================================
# This is somewhat similar to the brute force method, the difference is that
# you traverse the array from both the right and left sides and omit the current
# index, as opposed to just going straight from left to right and omitting it/
# ignoring it later, and there is no nested FOR loop with this algorithm.
#
# Both L[] and R[] start off with a value of 1, which means that they will both
# have an extra element at the end after the first FOR loop. To get rid of those,
# this algorithm uses *.pop().
#
# Time complexity: O(n) - we traverse nums[]
#
# Space complexity: O(n) -we're creating an L, R, and result array, each of which 
# contain 'n' elements

  def leftAndRightArrays(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # Set up L and R, populate them with numbers, pop the last number from both
    # arrays, and then reverse R
    L = [1]
    R = [1]
    for i, value in enumerate(input):
      L.append(L[i] * value)
      R.append(R[i] * input[len(input) - i - 1])
    L.pop()
    R.pop()
    R.reverse()

    # Multiplying the corresponding elements in R and L arrays gives the "product
    # of array except self" at each index in the input[] list
    for j, l in enumerate(L):
      result.append(l * R[j])

    print(output_expected == result)

# ========== Test ==============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.strip('\n').split(' ')]
      else:
        output_expected = [int(x) for x in line.strip('\n').split(' ')]
        poaes = ProductOfArrayExceptSelf(input, output_expected)
        if fn == 'bruteForce':
          poaes.bruteForce()
        if fn == 'division':
          poaes.division()
        if fn == 'logDivision':
          poaes.logDivision()
        if fn == 'leftAndRightArrays':
          poaes.leftAndRightArrays()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])