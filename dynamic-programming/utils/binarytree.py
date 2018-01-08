# -*- coding: utf-8 -*-

class CompleteBinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, x):
        if self.root is None:
            node = self.root = BinaryTreeNode(value=x)

        else:
            node = self.root.insert(x)

        return node

    def remove_leaf(self, node):
        assert node.left is None and node.right is None, '{} is not a leaf ' \
                                                         'node'.format(node)
        node_is_root = node.parent == None
        if node_is_root:
            self.root = None
            return

        parent = node.parent
        if parent.left == node:
            parent.left = None
            parent.is_complete = True

            while parent.parent is not None and parent.parent.left == parent:
                parent = parent.parent
                parent.is_complete = True

        else:
            parent.right = None
            parent.is_complete = False

            while parent.parent is not None and parent.parent.right == parent:
                parent = parent.parent
                parent.is_complete = False

    def last(self):
        if self.root is None:
            return None

        return self.root.last()

    def __str__(self):
        if self.root is None:
            return '<empty>'

        levels_str = []
        subroots = [self.root]
        while any(subroots):
            current_level = [
                str(subroot) if subroot is not None
                else '∅'
                for subroot in subroots
            ]
            levels_str.append('|'.join(current_level))

            holder = list(subroots)
            subroots = []
            for subroot in holder:
                if subroot is not None:
                    subroots.extend([subroot.left, subroot.right])

        return '\n'.join(levels_str)


class BinaryTreeNode(object):
    def __init__(self, parent=None, left=None, right=None, value=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value
        self.is_complete = True

    def insert(self, value):
        if self.is_complete:
            if self.left is None:
                self.is_complete = False
                self.left = BinaryTreeNode(parent=self, value=value)
                return self.left

            else:
                self.is_complete = False
                return self.left.insert(value=value)

        else:
            if self.right is None:
                self.is_complete = True
                self.right = BinaryTreeNode(parent=self, value=value)
                return self.right

            else:
                if not self.left.is_complete:
                    return self.left.insert(value=value)

                else:
                    node = self.right.insert(value=value)
                    if self.right.is_complete:
                        self.is_complete = True
                    return node

    def last(self):
        if self.is_complete:
            if self.left is None: # and self.right is None:
                return self
            else:
                return self.right.last()

        else:
            if self.right is None:
                return self.left

            if self.right.is_complete:
                return self.left.last()
            else:
                return self.right.last()

    def __str__(self):
        return str(self.value) + ('T' if self.is_complete else 'F')


if __name__ == '__main__':
    tree = CompleteBinaryTree()
    for v in range(111):
        tree.insert(v)

    print(tree)
