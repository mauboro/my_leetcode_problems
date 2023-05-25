# first, unbiased solution. I suppose the time complexity is O(n) and the space complexity is probabaly O(n) too, I am going to fact check this. I've just checked and it's actually O(1)(constant), because the space used by the output does not count towards the total space complexity, only the data structures used in the solution counts towards the space complexity

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if not i % 15:
                res.append("FizzBuzz")
            elif not i % 5:
                res.append("Buzz")
            elif not i % 3:
                res.append("Fizz")
            else:
                res.append(str(i))
        return res


