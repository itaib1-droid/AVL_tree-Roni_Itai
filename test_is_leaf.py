import AVLTree

def test_is_leaf():
	"""
	Comprehensive test of is_leaf() function
	Inserts 10 elements into AVL tree and thoroughly tests each node
	"""
	print("="*60)
	print("Testing is_leaf() Function")
	print("="*60)
	
	# Create tree and insert 10 elements
	tree = AVLTree.AVLTree()
	arr = [5, 3, 7, 2, 4, 6, 8, 1, 9, 10]
	
	print("\nInserting elements into tree:")
	for val in arr:
		node, edges, promotes = tree.finger_insert(val, str(val))
		print(f"  Inserted {val}: edges={edges}, promotes={promotes}")
	
	print(f"\nTree size: {tree.size()}")
	print(f"Tree height: {tree.get_root().height}")
	
	# Test 1: Check root
	print("\n" + "-"*60)
	print("Test 1: Root Node")
	print("-"*60)
	root = tree.get_root()
	print(f"Root: {root.key}")
	print(f"is_leaf(): {root.is_leaf()}")
	print(f"Expected: False (root should have children)")
	assert root.is_leaf() == False, "Root should return False"
	print("✓ PASS")
	
	# Test 2: Check leaf nodes
	print("\n" + "-"*60)
	print("Test 2: Leaf Nodes (nodes with no real children)")
	print("-"*60)
	
	leaf_count = 0
	nodes_checked = []
	
	# Check every element to see if it's a leaf
	for val in arr:
		node, _ = tree.search(val)
		if node:
			is_leaf = node.is_leaf()
			has_left = node.left.is_real_node()
			has_right = node.right.is_real_node()
			nodes_checked.append({
				'key': node.key,
				'is_leaf': is_leaf,
				'has_left': has_left,
				'has_right': has_right
			})
			
			# A leaf is a real node with no real children
			if is_leaf:
				leaf_count += 1
				assert has_left == False and has_right == False, \
					f"Node {node.key} marked as leaf but has children"
				print(f"  ✓ Node {node.key} is a leaf (no children)")
			else:
				assert has_left == True or has_right == True, \
					f"Node {node.key} marked as non-leaf but has no children"
				print(f"  ✓ Node {node.key} is not a leaf (has children: L={has_left}, R={has_right})")
	
	print(f"\nTotal leaves: {leaf_count}")
	print("✓ PASS")
	
	# Test 3: Check internal nodes
	print("\n" + "-"*60)
	print("Test 3: Internal Nodes (non-leaf, non-root)")
	print("-"*60)
	
	internal_count = 0
	for item in nodes_checked:
		if not item['is_leaf'] and item['key'] != root.key:
			internal_count += 1
			assert item['has_left'] or item['has_right'], \
				f"Node {item['key']} should be a leaf if it has no children"
			print(f"  ✓ Node {item['key']} is internal (L={item['has_left']}, R={item['has_right']})")
	
	print(f"\nTotal internal nodes: {internal_count}")
	print("✓ PASS")
	
	# Test 4: Check minimum and maximum (should typically be leaves)
	print("\n" + "-"*60)
	print("Test 4: Minimum and Maximum Nodes")
	print("-"*60)
	
	min_node = tree.min_node()
	max_node = tree.max_node()
	
	print(f"Minimum: {min_node.key}")
	print(f"  is_leaf(): {min_node.is_leaf()}")
	print(f"  Expected: True (minimum is typically a leaf)")
	assert min_node.is_leaf() == True, "Minimum should be a leaf"
	print("  ✓ PASS")
	
	print(f"\nMaximum: {max_node.key}")
	print(f"  is_leaf(): {max_node.is_leaf()}")
	print(f"  Expected: True (maximum is typically a leaf)")
	assert max_node.is_leaf() == True, "Maximum should be a leaf"
	print("  ✓ PASS")
	
	# Test 5: In-order traversal verification
	print("\n" + "-"*60)
	print("Test 5: In-order Traversal - Overall Verification")
	print("-"*60)
	
	arr_result = tree.avl_to_array()
	traversal_keys = [key for key, _ in arr_result]
	expected_keys = sorted(arr)
	
	print(f"In-order traversal: {traversal_keys}")
	print(f"Expected sorted order: {expected_keys}")
	assert traversal_keys == expected_keys, "In-order traversal should return sorted elements"
	print("✓ PASS")
	
	print("\n" + "="*60)
	print("All Tests Passed Successfully! ✓")
	print("="*60)

if __name__ == "__main__":
	test_is_leaf()
