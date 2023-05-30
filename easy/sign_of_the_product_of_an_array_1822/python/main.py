#this is brute force approach, very inefficient because the product of the array is being stored unnecessarily. Time complexity is maybe O(n) because we iterate one time through the array with the reduce function, and space complexity is maybe O(n) because x stores a number proportional to the array, or not? I really couldn't grasp this complexity analysis stuff.

from functools import reduce

class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = reduce(lambda a, b: a * b, nums)
        return 1 if x > 0 else -1 if x < 0 else 0


#I like this approach, it counts the number of negative numbers, if the number is even, the product should be positive since two negative numbers cancel each other, otherwise it's positive, and if it encounters a zero, it directly returns a zero, cool, huh? Time complexity = O(n) and space complexity = O(1).
class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        negatives = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                negatives += 1
        if not negatives % 2:
            return 1
        else:
            return -1
