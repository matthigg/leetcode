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
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), 
# profit = 6 - 1 = 5. Not 7 - 1 = 6, as selling price needs to be larger than 
# buying price.
#
# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

class BuyAndSellStock:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ===== Practice ===============================================================

  def blank(self):
    input, output_expected = self.input, self.output_expected

    # blank, result = int
    max_profit = 0
    l = 0
    r = 0
    while r < len(input):
      if input[r] - input[l] > max_profit:
        max_profit = input[r] - input[l]
      if input[r] - input[l] < 0:
        l = r
      r += 1      

    result = max_profit
    print(result == output_expected, output_expected, result)

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
        bass.blank()

# ========== Command Line Arguments ============================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])