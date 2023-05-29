#first solution, done by brute force approach, time complexity = O(n**2) and space complexity = O(1)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in nums:
            index = nums.index(n)
            for i, num in enumerate(nums):
                if n + num == target and index != i:
                    return [index, i]

#second solution, done by using one pass hashtable, since hashtables(dictionaries) lookups are O(1), we can reduce the time complexity seen in the previous solution(O(n**2)) to O(n) by increasing the space complexity(O(1) in the previous one) to O(n), very interesting solution.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {} 
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hashmap:
                return [i, hashmap[x]]
            hashmap[nums[i]] = i 


