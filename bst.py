class Node:
    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root


def delete(root, key):
    if root is None:
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


root = None

while True:
    print("\n1.Insert 2.Delete 3.Inorder 4.Preorder 5.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        root = insert(root, int(input("Enter value: ")))
    elif ch == 2:
        root = delete(root, int(input("Enter value: ")))
    elif ch == 3:
        inorder(root)
        print()
    elif ch == 4:
        preorder(root)
        print()
    elif ch == 5:
        break
    else:
        print("Invalid choice")1