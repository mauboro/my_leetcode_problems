#this approach is no fun, uses a lot of builtin functions, maybe I should refactor it. I really believe that that the time complexity of this algo is something in the likes of O(3n) since sum, max and min probably iterate over the array passed as a parameter

class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        s = sum(salary) - max(salary) - min(salary)

        return float(s) / float((len(salary) - 2))
