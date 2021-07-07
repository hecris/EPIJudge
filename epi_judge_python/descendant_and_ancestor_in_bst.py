import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    if middle is possible_anc_or_desc_0 or middle is possible_anc_or_desc_1:
        return False

    def search(root, target):
        return root if root is target or not root else (
                search(root.left, target) if target.data < root.data
                else search(root.right, target)
                )

    desc = search(middle, possible_anc_or_desc_0)

    if desc is None:
        return (search(middle, possible_anc_or_desc_1) is not None and
                search(possible_anc_or_desc_0, middle) is not None)

    return search(possible_anc_or_desc_1, middle) is not None



@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
