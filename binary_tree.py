class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

class BinaryTree:
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, key, parent=None):
        if not parent:
            parent = self.root

        if parent.key < key:
            if not parent.right:
                parent.right = Node(key)
                return
            self.insert(key, parent.right)
        else:
            if not parent.left:
                parent.left = Node(key)
                return
            self.insert(key, parent.left)

    def inorder(self, parent=None):
        if not parent:
            return
        self.inorder(parent.left)
        print(parent.key,end=' ')
        self.inorder(parent.right)

    def preorder(self, parent=None):
        if not parent:
            return
        print(parent.key, end=' ')
        self.inorder(parent.left)
        self.inorder(parent.right)

    def postorder(self, parent=None):
        if not parent:
            return
        self.inorder(parent.left)
        self.inorder(parent.right)
        print(parent.key, end=' ')

    def max_depth(self, root):
        if not root:
            return 0
        l_depth = self.max_depth(root.left)
        r_depth = self.max_depth(root.right)
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1

    def sorted_array_to_bst(self, arr):
        if not arr:
            return
        mid = arr//2
        node = Node(arr[mid])
        node.left = self.sorted_array_to_bst(arr[:mid])
        node.right = self.sorted_array_to_bst(arr[mid+1:])
        return node



if __name__ == "__main__":
    b = BinaryTree(5)
    b.insert(3)
    b.insert(2)
    b.insert(4)
    b.insert(7)
    b.insert(6)
    b.insert(8)
    print("Inorder traversal: ")
    b.inorder(b.root)
    print("\nPreorder traversal: ")
    b.preorder(b.root)
    print("\nPostorder traversal: ")
    b.postorder(b.root)
