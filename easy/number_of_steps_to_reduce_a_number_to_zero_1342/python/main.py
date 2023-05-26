#first solution, time complexity is O(logn) because the number of the steps necessary to reduce the number to zero depends on the amount of times we have to divide our input by two and space complexity is O(1) because we do not create a data structure proportional to the size of our input.

class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            if num % 2:
                num -= 1
                steps += 1
            else:
                num /= 2
                steps += 1
        return steps

#here is a solution that uses bitwise operations to obtain the same results, instead of using the modulo operator to assert if the number is even or not, it compares its binary representation if a bitmask, and, instead of halving it the "regular way" it shifts all the bits of the number's binary representation to the right by one position, essentially halving it.
class SolutionRefactored(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        steps = 0
        while num != 0:
            if not num & 1:
                num = num >> 1
            else:
                num -= 1

            steps += 1
        return steps
