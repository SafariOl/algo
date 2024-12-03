class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def delete_root(self):
        if self.root is not None:
            self.root = self._delete_node(self.root)

    def _delete_node(self, node):
        # Видалення вузла без нащадків або з одним нащадком
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # Пошук мінімального значення у правому піддереві
        min_larger_node = self._get_min(node.right)
        node.key = min_larger_node.key
        node.right = self._delete_node_recursive(node.right, min_larger_node.key)
        return node

    def _get_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete_node_recursive(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_node_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_node_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._get_min(node.right)
            node.key = temp.key
            node.right = self._delete_node_recursive(node.right, temp.key)

        return node

    def get_possible_new_roots(self):
        possible_roots = []
        if self.root.left:
            possible_roots.append(self.root.left.key)
        if self.root.right:
            possible_roots.append(self.root.right.key)
        return possible_roots

# Побудова дерева з ключами 20, 25, 10, 13, 15, 8, 22, 9, 35
bst = BST()
keys = [20, 25, 10, 13, 15, 8, 22, 9, 35]
for key in keys:
    bst.insert(key)

# Вставка числа 12
bst.insert(12)

# Видалення кореня
bst.delete_root()

# Пошук можливих нових коренів
new_roots = bst.get_possible_new_roots()
print(",".join(map(str, new_roots)))
