# Given a linked list, remove the n-th node from the end of list and return its 
# head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?

class RemoveNthNodeFromEndOfList:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== One Pass =========================================================

  def onePass(self):
    input, output_expected = self.input, self.output_expected
    print(input, output_expected)

  # print(result == output_expected, output_expected, result)

# ========== Tests ============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = line.strip('\n')
      else:
        output_expected = line.strip('\n')
        rnnfeol = RemoveNthNodeFromEndOfList(input, output_expected)
        if fn == 'onepass':
          rnnfeol.onePass()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])