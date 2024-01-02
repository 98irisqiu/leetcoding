from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def PreorderTraversal_recur(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        递归实现
        :param root:
        :return:
        """
        if not root:
            return []

        return [root.val] + self.PreorderTraversal_recur(root.left) + self.PreorderTraversal_recur(root.right)

    def PreorderTraversal_iter(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        迭代实现
        :param root:
        :return:
        """
        if not root:
            return []

        stack = []  # 用来存放未处理子树的节点
        res = []
        cur = root

        while stack or cur:
            # while代表每一个节点的处理
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop().right

        return res

if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    s = Solution()
    print('递归实现：', s.PreorderTraversal_recur(root))
    print('迭代实现：', s.PreorderTraversal_iter(root))