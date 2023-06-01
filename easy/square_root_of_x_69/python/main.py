# I mean, time complexity must be O(1) because we do not iterate over anything I guess, the same applies to the space complexity. 

from math import sqrt

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(sqrt(x))
