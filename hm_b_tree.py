class BNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []


class BTree:
    def __init__(self, t):
        self.root = BNode(leaf=True)
        self.t = t

    def split(self, node, i):
        t = self.t
        new_node = BNode(leaf=node.leaf)
        split_key = node.keys[t - 1]
        new_node.keys = node.keys[t:]
        node.keys = node.keys[:t - 1]

        if not node.leaf:
            new_node.children = node.children[t:]
            node.children = node.children[:t]

        node.children.insert(i + 1, new_node)
        node.keys.insert(i, split_key)

    def insert(self, k):
        root = self.root
        t = self.t

        if len(root.keys) == (2 * t) - 1:
            new_node = BNode()
            self.root = new_node
            new_node.children.append(root)
            self.split(new_node, 0)
            self._insert_non_full(new_node, k)
        else:
            self._insert_non_full(root, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1

        if node.leaf:
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1

            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def search(self, k, node=None):
        if node is None:
            node = self.root

        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and k == node.keys[i]:
            return True

        if node.leaf:
            return False

        return self.search(k, node.children[i])

    def delete(self, k):
        self._delete_recursive(self.root, k)

    def _delete_recursive(self, node, k):
        t = self.t
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1

        if i < len(node.keys) and k == node.keys[i]:
            if node.leaf:
                node.keys.pop(i)
            else:
                # TODO: implement deletion for non-leaf nodes
                pass
        else:
            if node.leaf:
                return False

            child = node.children[i]
            if len(child.keys) < t:
                # TODO: implement merging or rebalancing
                pass

            self._delete_recursive(node.children[i], k)

    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root

        if not node.leaf:
            for i in range(len(node.children)):
                self.inorder_traversal(node.children[i])

        for i in range(len(node.keys)):
            print(node.keys[i], end=' ')

        if not node.leaf:
            print()


# Пример использования:

b_tree = BTree(6)
b_tree.insert(5)
b_tree.insert(3)
b_tree.insert(7)
b_tree.insert(2)
b_tree.insert(8)
b_tree.insert(4)

b_tree.inorder_traversal()
print(" ")
print("Есть ли в дереве 3", b_tree.search(3))  # True
print("Есть ли в дереве 9", b_tree.search(9))  # False

b_tree.delete(3)
b_tree.inorder_traversal()