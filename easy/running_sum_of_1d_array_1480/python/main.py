class Solution(object):

    def runningSum(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        res = []

        for i in range(len(nums)):

            res.append(sum(nums[:i+1]))

        return  res

#refactored solution, time complexity = O(n), space complexity = O(1)

class SolutionRefactored(object):

    def runningSum(self, nums):

        res = []
        for i in range(len(nums)):
            res.append(sum(nums[:i]) + nums[i])

        return  res


#a faster solution, because sum is not being used, time and space complexities remain the same, I guess =)
class SolutionRefactoredAgain(object):

    def runningSum(self, nums):

        res = []
        temp = 0
        for n in nums:
            res.append(temp + n)
            temp += n

        return  res


