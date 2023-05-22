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


#refactored solution based on the solution video, very clever, indeed
class SolutionRefactoredYetAgain(object):

    def runningSum(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        res = [nums[0]]

        for i in range(1, len(nums)):

            res.append(nums[i] + res[i - 1])

        return res

#here is another solution extracted from the same video, but it overwrites the original input, dangerous, but nonetheless interesting
class SolutionRefactoredOneMoreTime(object):

    def runningSum(self, nums):

        """

        :type nums: List[int]

        :rtype: List[int]

        """

        for i in range(1, len(nums)):

            nums[i] += nums[i - 1]

        return nums

