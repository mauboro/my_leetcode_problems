#first solution, time complexity is O(n) where n is the number of nodes and space complexity is O(n) because we are copying each node to a array, in other words, creating a data structure with a size proportional to our input, so its not constant, like in the previous exercises.

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[len(res)//2]

#this approach uses only linked-list concepts to keep track of the linked-list, using two pointers, the mid pointers, that's increased every two steps of the linked list iteration and the end pointer, that's increased every step of the linked list iteration, cool, huh? Time complexity remains the same, but the space complexity is now O(1)(constant) because we do not create a data structure proportional to our input.
class SolutionRefactored(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mid = head
        end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        return mid




