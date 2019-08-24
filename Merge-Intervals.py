# Given a collection of intervals, merge all overlapping intervals.
#
# Example 1:
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
#
# Example 2:
#
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class MergeIntervals:
  def __init__(self, input, output_expected):
    self.input = input
    self.output_expected = output_expected

# ========== Sort & Merge =======================================================
# The idea behind this approach is to sort each interval contained in a list,
# and to then sort the list itself, so we have an ascending list of lists that
# are ordered by each interval's first element, interval[0]. When we find two
# intervals that cover an overlapping range of numbers, we "stitch" them together 
# by making an entirely new interval that includes the ranges of the previous two.
# We then repeat this process over and over until all overlapping intervals have
# been merged.
# 
# This approach sorts each interval element contained in input[], as well as input[]
# itself. Using a WHILE loop containing a nested FOR loop, we look at each 
# interval and compare its max value against both the min and max value of the
# next element in the loop, and either a) insert the interval into a temporary
# list called merged_input[], or b) create a new interval representing the merging
# of the two intervals, assuming they overlap numerically, and then make sure to
# skip the next (now 'merged') interval using weird Python "guard code", aka. 
# the "continue" keyword, as we continue through the loop.
# 
# Afterwards we store the value of the length of sorted_input[] in prev_input_length,
# dump the contents of the temporary merged_input[] list into sorted_input[],
# reset merged_list[] to a blank list [], and continue on using the WHILE loop to
# check that the sorted_input[] list has decreased in length from the last 
# iteration. The idea is that when sorted_input[] stops decreasing in size, all
# intervals have been merged.
#
# Time complexity: O(n^2) - (I think) both the WHILE and its nested FOR loop depend
# upon the size of the input, input[], and 2x loops tend to run in O(n^2) time.
# Additionally, the sorting algorithm is used twice -- once as the *.sort() method,
# and again as the sorted() function, both of which are based upon Timsort and
# run in (n log(n)) time; however, O(n^2) time from the loops would have a 
# predominant effect.
# 
# Space complexity: O(n) - sorted() returns 'n' number of list elements, *.sort()
# has O(1) space complexity because it sorts in-place, and merged_input holds up 
# to 'n' elements.

  def sortMerge1(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # If there is 1 or fewer interval in input[], return
    if len(input) < 2:
      result = input
      print(result == output_expected)
      return

    # Sort each list element contained in input[], then sort input[] itself
    sorted_input = [sorted(x) for x in input]
    sorted_input.sort()

    # The loop will continue as long as the size of sorted_input[] is continually
    # shrinking
    from sys import maxsize
    prev_input_length = maxsize
    merged_input = []
    skip_next = False
    while len(sorted_input) < prev_input_length:
      for i in range(len(sorted_input)):

        # Skip the i'th interval if it was "merged" with the previous interval due 
        # to overlap
        if skip_next:
          skip_next = False
          continue

        # [ax, ay], [bx, by]
        try:
          ax = sorted_input[i][0]
          ay = sorted_input[i][1]
          bx = sorted_input[i + 1][0]
          by = sorted_input[i + 1][1]
        except IndexError:
          bx = None
          by = None
          pass

        # Merge [ax, ay] and [bx, by] if they overlap, otherwise just append 
        # [ax, ay]
        if bx != None and ay >= bx and by != None and ay <= by:
          interval = [ax, by]
          merged_input.append(interval)
          skip_next = True
        elif by and ay > by:
          interval = [ax, ay]
          merged_input.append(interval)
          skip_next = True   
        else:
          merged_input.append([ax, ay])
        
      prev_input_length = len(sorted_input)
      sorted_input = merged_input
      merged_input = []

    result = sorted_input
    print(result == output_expected)

# This is a much, much shorter version using sort. Instead of adding all interval
# pairs to a new list and creating a new interval/skipping the next interval
# when the current and the -next- intervals have overlap, this algorithm simply 
# looks at the current interval and the -previous- interval, which is stored in
# the merged[] list, and if there is overlap it will modify the current interval
# in place.
#
# Specifically, if the list is empty, or if the end of the last interval is less 
# than the beginning of the new interval, then the two intervals don't overlap 
# and the current interval can simply be appended to merged[]. Otherwise, merge 
# the intervals by adjusting merged[-1][1], ie. the upper bound of the interval.
#
# Time complexity: O(n log(n)) - the sort function & method are both Timsort, 
# which is (n log(n)) time.
#
# Space complexity: O(n) - we use merged[] to hold up to 'n' elements, however
# if you don't consider required output as something that adds to extra space
# complexity, then you could argue O(1) space complexity.

  def sortMerge2(self):
    input, output_expected = self.input, self.output_expected
    result = []

    # If there is 1 or fewer interval in input[], return
    if len(input) < 2:
      result = input
      print(result == output_expected)
      return

    # Sort input[] and its elements/intervals
    input = [sorted(x) for x in input]
    input.sort(key=lambda x: x[0])

    # Determine whether to "merge" new intervals or simply append them
    merged = []
    for value in input:

      # Append the current interval without merging
      if not merged or merged[-1][1] < value[0]:
        merged.append(value)

      # Merge intervals
      else:
        merged[-1][1] = max(merged[-1][1], value[1])

    result = merged
    print(result == output_expected)

# ========== Connected Components =============================================
# INCOMPLETE
#
# Intuition
# If we draw a graph (with intervals as nodes) that contains undirected edges 
# between all pairs of intervals that overlap, then all intervals in each 
# connected component of the graph can be merged into a single interval.
#
# Algorithm
# With the above intuition in mind, we can represent the graph as an adjacency 
# list, inserting directed edges in both directions to simulate undirected edges.
# Then, to determine which connected component each node is it, we perform graph
# traversals from arbitrary unvisited nodes until all nodes have been visited. To
# do this efficiently, we store visited nodes in a Set, allowing for constant
# time containment checks and insertion. Finally, we consider each connected 
# component, merging all of its intervals by constructing a new Interval with 
# start equal to the minimum start among them and end equal to the maximum end.
#
# This algorithm is correct simply because it is basically the brute force 
# solution. We compare every interval to every other interval, so we know exactly 
# which intervals overlap. The reason for the connected component search is that 
# two intervals may not directly overlap, but might overlap indirectly via a 
# third interval. See the example below to see this more clearly.
#
# Time complexity: O(n^2)
#
# Space complexity: 

  def overlap(self, a, b):
      return a[0] <= b[1] and a[1] >= b[0]

  # Create a graph using defaultdict(list), which conveniently sets all values in
  # its key:values pairs to lists[] so that you can start appending to them right
  # away without having to assign a list to them first
  def build_graph(self, nums):
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if self.overlap(nums[i], nums[j]):
          graph[tuple(nums[i])].append(tuple(nums[j]))
          graph[tuple(nums[j])].append(tuple(nums[i]))
    return graph

  def merge(self, nums, expected_result):
    graph = self.build_graph(nums)
    print(graph)
    
    # Iterate over the graph using a FOR...IN loop, just like a dict{}
    for node in graph:
      print(node, graph[node])

  # --- INCOMPLETE ---

# ========== Test =============================================================

def test(test_file, fn):
  with open(test_file) as tf:
    lines = tf.readlines()
    for i, line in enumerate(lines):
      if i % 2 == 0:
        input = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
      else:
        output_expected = [[int(y) for y in x.split(' ')] for x in line.strip('\n').split(', ')]
        mi = MergeIntervals(input, output_expected)
        if fn == 'sortMerge1':
          mi.sortMerge1()
        if fn == 'sortMerge2':
          mi.sortMerge2()
        # if fn == 'connectedComponents':
        #   mi.merge()

# ========== Command Line Arguments ===========================================

if __name__ == '__main__':
  import sys
  test(sys.argv[1], sys.argv[2])