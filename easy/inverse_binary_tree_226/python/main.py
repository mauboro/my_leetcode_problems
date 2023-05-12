#recursive approach, time complexity = O(n), space complexity = O(n)
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root

from collections import deque

#iterative approach, time complexity = O(n), space complexity = O(n)
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        queue = deque([root])
        while queue: 
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root
