from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def PostorderTraversal_recur(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        递归实现
        :param root:
        :return:
        """

    def PostorderTraversal_iter(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        迭代实现
        :param root:
        :return:
        """
        if not root:
            return []

        stack = []
        res = []
        cur = root

        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop().left

        return res[::-1]

if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    s = Solution()
    # print('递归实现：', s.PostorderTraversal_recur(root))
    print('迭代实现：', s.PostorderTraversal_iter(root))