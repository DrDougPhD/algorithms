# A Binary Heap is a binary tree with two additional constraints:
#  *  Shape property: a binary heap is a complete binary tree; that is,
#     all levels of the tree, except possibly the last one (deepest) are
#     fully filled, and, if the last level of the tree is not complete,
#     the nodes of that level are filled from left to right.
#  *  Heap property: the key stored in each node is either greater than or
#     equal to (>=) or less than or equal to (<=) the keys in the node's
#     children, according to some total order.

import binarytree

class BinaryHeap(object):
    def __init__(self, values=None):
        """Create an empty heap
        """
        self.tree = binarytree.CompleteBinaryTree()
        if values is not None:
            for v in values:
                self.insert(value=v)

    def insert(self, value):
        """Adding a new key to the heap (a.k.a., push)
        """

        # Add the element to the bottom level of the heap.
        node = self.tree.insert(value)

        # Compare the added element with its parent.
        new_node_is_root = node.parent is None
        if new_node_is_root:
            return node

        return self._upheap(node)

    def extract(self):
        """
        The procedure for deleting the root from the heap (effectively 
         extracting the maximum element in a max-heap or the minimum element 
         in a min-heap) and restoring the properties is called down-heap (
         also known as bubble-down, percolate-down, sift-down, trickle down, 
         heapify-down, cascade-down, and extract-min/max).
        :return: 
        """
        # Replace the root of the heap with the last element on the last level.
        root_value = self.tree.root.value
        last_node = self.tree.last()
        self.tree.root.value = last_node.value
        self.tree.remove_leaf(last_node)

        self._downheap(node=self.tree.root)

        return root_value

    def _upheap(self, node):
        # node.parent is never null
        if node.value <= node.parent.value:
            # If they are in the correct order, stop.
            return node

        else:
            # If not, swap the element with its parent and return to the
            # previous step.
            v = node.value
            node.value = node.parent.value
            node.parent.value = v
            if node.parent.parent is not None:
                return self._upheap(node.parent)
            else:
                return node.parent

    def _downheap(self, node):
        if node is None:
            return

        # Compare the new root with its children
        children = []
        if node.right is not None:
            children.append(node.right)
        if node.left is not None:
            children.append(node.left)

        if not children:
            return

        # If they are in the correct order, stop.
        if all(map(lambda x: x.value <= node.value, children)):
            return

        # If not, swap the element with one of its children and return to the
        #  previous step. (Swap with its smaller child in a min-heap and its
        #  larger child in a max-heap.)
        largest_child = max(children, key=lambda x: x.value)
        node.value, largest_child.value = largest_child.value, node.value
        self._downheap(node=largest_child)

    def __bool__(self):
        return bool(self.tree.root)

    def __str__(self):
        return str(self.tree)

    def assert_valid(self):
        if self.tree.root is None:
            return True

        if self.tree.root.left is None and self.tree.root.right is None:
            return True

        if self.tree.root.left is not None:
            valid_subtree = self._assert_on_subtree_rooted_at(
                node=self.tree.root.left
            )
            if not valid_subtree:
                return False

        if self.tree.root.right is not None:
            valid_subtree = self._assert_on_subtree_rooted_at(
                node=self.tree.root.right)
            if not valid_subtree:
                return False

        return True

    def _assert_on_subtree_rooted_at(self, node):
        assert node.parent is not None
        if node.parent.value < node.value:
            return False

        if node.left is not None:
            valid_subtree = self._assert_on_subtree_rooted_at(node=node.left)
            if not valid_subtree:
                return False

        if node.right is not None:
            valid_subtree = self._assert_on_subtree_rooted_at(node=node.right)
            if not valid_subtree:
                return False

        return True


def sort(values):
    heap = BinaryHeap(values=values)
    while heap:
        yield heap.extract()


if __name__ == '__main__':
    import random
    import time
    random.seed(time.time())

    values = [random.randrange(0, 1000) for _ in range(122)]
    sorted_array = list(sort(values))
    print('Sorted: {}'.format(sorted_array))

    for x, y in zip(sorted(values, reverse=True), sorted_array):
        assert x == y, 'Heap is not properly sorting!'
