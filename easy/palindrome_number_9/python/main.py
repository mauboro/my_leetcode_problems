#I suppose the time complexity is O(n) where n is the number of digits of x and the space complexity is O(3n) because we create three additional data structures proportional to our input, I could be seriously wrong though.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if str(x)[::-1] == str(x) else False
