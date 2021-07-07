from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    # recursive constraining
    def valid(root, lo, hi):
        if not root:
            return True

        if not (lo <= root.data and root.data <= hi):
            return False

        return valid(root.left, lo, root.data) and valid(root.right, root.data, hi)

    # iterative inorder - still suboptimal
    def valid2(root):
        stack = []
        stack.append((root, False))
        prev = float('-inf')
        while stack:
            node, processed = stack.pop()
            if processed:
                if prev > node.data:
                    return False
                prev = node.data
            else:
                if node.right:
                    stack.append((node.right, False))

                stack.append((node, True))

                if node.left:
                    stack.append((node.left, False))

        return True

    # bfs constraining - optimal
    def valid3(root):
        from collections import deque
        q = deque()
        q.append((root, float('-inf'), float('inf')))
        while q:
            node, lo, hi = q.popleft()
            if not (lo <= node.data and node.data <= hi):
                return False

            if node.left:
                q.append((node.left, lo, node.data))

            if node.right:
                q.append((node.right, node.data, hi))

        return True

    return valid3(tree)

    return valid2(tree)

    return valid(tree, float('-inf'), float('inf'))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
