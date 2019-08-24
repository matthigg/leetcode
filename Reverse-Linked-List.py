# Reverse a singly linked list.
#
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you 
# implement both?

class ReverseLinkedList:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Iterative Solution ===============================================
# x
#
# Time complexity:
#
# Space complexity:

  def iterative(self):
    input = self.input
    output_expected = self.output_expected
    print(input, output_expected)

# ========== Recursive Solution ===============================================
# x
#
# Time complexity:
#
# Space complexity:

  def recursive(self):
    input = self.input
    output_expected = self.output_expected
    print(input, output_expected)

# ========== Test =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n')
      else:
        output_expected = line.strip('\n')
        rll = ReverseLinkedList(input, output_expected)
        if fn == 'iterative':
          rll.iterative()
        if fn == 'recursive':
          rll.recursive()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])