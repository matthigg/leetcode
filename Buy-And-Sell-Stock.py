# Say you have an array for which the ith element is the price of a given stock 
# on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one 
# and sell one share of the stock), design an algorithm to find the maximum 
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class BuyAndSellStock:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Brute Force =======================================================
# Double FOR loops, with inner loop creating a slice
#
# Time complexity: O(n^2) - 2x FOR loops run n(n - 1) / 2 times.
#
# Space complexity: O(n) - the inner FOR loop continuously takes slices from the
# prices list, up to 'n' - 1 elements in length

  def bruteForce(self):
    input, output_expected = self.input, self.output_expected

    result = 0
    for i in range(len(input) - 1):
      for j in range(i + 1, len(input)):
        if input[j] - input[i] > result:
          result = input[j] - input[i]

    print(result == output_expected)

# ========== One Pass ==========================================================
# Moving from left-to-right, we find each local minimum value and continually
# update the maximum value, ie. max_profit, until we find a new local minimum.
#
# Time complexity: O(n) - single pass
#
# Space complexity: O(1) - max_profit and min are the only created variables

  def onePass(self):
    input, output_expected = self.input, self.output_expected

    # Set min and max profit (ie. result) values
    min = sys.maxsize
    result = 0

    for value in input:
      if value < min:
        min = value
      elif value - min > result:
        result = value - min

    print(result == output_expected)

# ========== Tests =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [int(x) for x in line.split(' ')]
      else:
        output_expected = int(line)
        bass = BuyAndSellStock(input, output_expected) 
        if fn == 'bruteForce':
          bass.bruteForce()
        if fn == 'onePass':
          bass.onePass()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])