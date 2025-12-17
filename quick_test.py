import AVLTree

# בדיקה פשוטה עם מערך ממוין
tree = AVLTree.AVLTree()

arr = [1, 2, 3, 4, 5, 6, 7]

print("הכנסת מערך ממוין:")
for val in arr:
    node, edges, promotes = tree.finger_insert(val, "0")
    print(f"הכנסת {val}: edges={edges}, promotes={promotes}")

print(f"\nגודל העץ: {tree.size()}")

