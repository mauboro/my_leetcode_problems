#my initial solution, time and space complexities are unkown

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        return max([sum(a) for a in accounts])

#the solution based on the solution video, more explicit and clever, time complexity = 0(n x m), space complexity = O(1)
class SolutionRefactored(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """

        max_wealth = 0

        for c in accounts:
            c_wealth = 0
            for b in c:
                c_wealth += b
            max_wealth = max(max_wealth, c_wealth)

        return max_wealth
