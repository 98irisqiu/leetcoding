from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = [root]

        while q:  # 每执行一次while就是计算每一层
            n = len(q)  # 这一层的子树数目
            level = []
            # 开始循环子树
            for i in range(n):
                node = q.pop(0)
                level.append(node.val)  # 将这一层的节点值加入到结果中
                # 如果该节点存在左子树，将左子树加到队列q中
                if node.left:
                    q.append(node.left)
                # 如果该节点存在右子树，将右子树加到队列q中
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res

if __name__ == "__main__":
    # root = [3, 9, 20, None, None, 15, 7]
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    s = Solution()
    print(s.levelOrder(root))