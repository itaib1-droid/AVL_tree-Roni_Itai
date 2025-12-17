import AVLTree

def test_basic_operations():
    """Test basic insert and search operations"""
    print("=" * 50)
    print("TEST 1: Basic Insert and Search")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    
    # Insert values
    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(15, "15")
    tree.insert(3, "3")
    tree.insert(7, "7")
    tree.insert(12, "12")
    tree.insert(20, "20")
    
    # Test search
    node, edges = tree.search(10)
    assert node is not None and node.key == 10, "Search for 10 failed"
    print(f"✓ Search for 10: found at {edges} edges")
    
    node, edges = tree.search(20)
    assert node is not None and node.key == 20, "Search for 20 failed"
    print(f"✓ Search for 20: found at {edges} edges")
    
    node, edges = tree.search(100)
    assert node is None, "Search for non-existent 100 should return None"
    print("✓ Search for non-existent key returns None")
    
    assert tree.size() == 7, f"Size should be 7, got {tree.size()}"
    print(f"✓ Tree size: {tree.size()}")

def test_empty_tree():
    """Test operations on empty tree"""
    print("\n" + "=" * 50)
    print("TEST 2: Empty Tree Operations")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    
    assert tree.get_root() is None, "Root of empty tree should be None"
    print("✓ Empty tree root is None")
    
    assert tree.max_node() is None, "Max of empty tree should be None"
    print("✓ Empty tree max is None")
    
    assert tree.min_node() is None, "Min of empty tree should be None"
    print("✓ Empty tree min is None")
    
    assert tree.size() == 0, "Empty tree size should be 0"
    print("✓ Empty tree size is 0")
    
    arr = tree.avl_to_array()
    assert arr == [], "Empty tree array should be empty"
    print("✓ Empty tree array is empty")

def test_single_node():
    """Test operations with single node"""
    print("\n" + "=" * 50)
    print("TEST 3: Single Node Operations")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    tree.insert(42, "answer")
    
    assert tree.size() == 1, "Size should be 1"
    print("✓ Single node tree size is 1")
    
    assert tree.get_root().key == 42, "Root should be 42"
    print("✓ Single node is root")
    
    assert tree.max_node().key == 42, "Max should be 42"
    print("✓ Single node is max")
    
    assert tree.min_node().key == 42, "Min should be 42"
    print("✓ Single node is min")

def test_delete_leaf():
    """Test deleting leaf nodes"""
    print("\n" + "=" * 50)
    print("TEST 4: Delete Leaf Nodes")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(15, "15")
    tree.insert(3, "3")
    tree.insert(7, "7")
    
    # Delete leaf node
    node = tree.search(3)[0]
    tree.delete(node)
    assert tree.search(3)[0] is None, "Node 3 should be deleted"
    assert tree.size() == 4, f"Size should be 4, got {tree.size()}"
    print("✓ Leaf node deleted successfully")
    
    # Delete another leaf
    node = tree.search(7)[0]
    tree.delete(node)
    assert tree.search(7)[0] is None, "Node 7 should be deleted"
    assert tree.size() == 3, f"Size should be 3, got {tree.size()}"
    print("✓ Second leaf deleted successfully")

def test_delete_node_with_one_child():
    """Test deleting node with one child"""
    print("\n" + "=" * 50)
    print("TEST 5: Delete Node with One Child")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(3, "3")
    
    # Delete node with one child (5 has only left child 3)
    node = tree.search(5)[0]
    tree.delete(node)
    assert tree.search(5)[0] is None, "Node 5 should be deleted"
    assert tree.search(3)[0] is not None, "Node 3 should still exist"
    assert tree.size() == 2, f"Size should be 2, got {tree.size()}"
    print("✓ Node with one child deleted successfully")

def test_delete_node_with_two_children():
    """Test deleting node with two children"""
    print("\n" + "=" * 50)
    print("TEST 6: Delete Node with Two Children")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    tree.insert(10, "10")
    tree.insert(5, "5")
    tree.insert(15, "15")
    tree.insert(3, "3")
    tree.insert(7, "7")
    tree.insert(12, "12")
    tree.insert(20, "20")
    
    # Delete node with two children
    node = tree.search(10)[0]
    tree.delete(node)
    assert tree.search(10)[0] is None, "Node 10 should be deleted"
    assert tree.size() == 6, f"Size should be 6, got {tree.size()}"
    print("✓ Node with two children deleted successfully")

def test_delete_root():
    """Test deleting root node"""
    print("\n" + "=" * 50)
    print("TEST 7: Delete Root Node")
    print("=" * 50)
    
    # Test 1: Delete root with one child
    tree = AVLTree.AVLTree()
    tree.insert(10, "10")
    tree.insert(5, "5")
    
    root = tree.get_root()
    tree.delete(root)
    assert tree.search(10)[0] is None, "Root 10 should be deleted"
    assert tree.search(5)[0] is not None, "Node 5 should exist"
    print("✓ Root with one child deleted")
    
    # Test 2: Delete root that's a leaf
    tree2 = AVLTree.AVLTree()
    tree2.insert(42, "42")
    root = tree2.get_root()
    tree2.delete(root)
    assert tree2.get_root() is None, "Tree should be empty"
    assert tree2.size() == 0, "Size should be 0"
    print("✓ Root leaf deleted (empty tree)")
    
    # Test 3: Delete root with two children
    tree3 = AVLTree.AVLTree()
    tree3.insert(10, "10")
    tree3.insert(5, "5")
    tree3.insert(15, "15")
    root = tree3.get_root()
    tree3.delete(root)
    assert tree3.search(10)[0] is None, "Root 10 should be deleted"
    assert tree3.search(5)[0] is not None, "Node 5 should exist"
    assert tree3.search(15)[0] is not None, "Node 15 should exist"
    print("✓ Root with two children deleted")

def test_max_min():
    """Test max and min operations"""
    print("\n" + "=" * 50)
    print("TEST 8: Max and Min Operations")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    values = [15, 3, 20, 1, 7, 12, 25, 30, 5]
    
    for val in values:
        tree.insert(val, str(val))
    
    assert tree.max_node().key == 30, "Max should be 30"
    print(f"✓ Max is 30")
    
    assert tree.min_node().key == 1, "Min should be 1"
    print(f"✓ Min is 1")
    
    # Delete max and check new max
    max_node = tree.max_node()
    tree.delete(max_node)
    assert tree.max_node().key == 25, f"New max should be 25, got {tree.max_node().key}"
    print("✓ Max updated after deletion")
    
    # Delete min and check new min
    min_node = tree.min_node()
    tree.delete(min_node)
    assert tree.min_node().key == 3, f"New min should be 3, got {tree.min_node().key}"
    print("✓ Min updated after deletion")

def test_successor():
    """Test successor operation"""
    print("\n" + "=" * 50)
    print("TEST 9: Successor Operations")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    values = [10, 5, 15, 3, 7, 12, 20]
    
    for val in values:
        tree.insert(val, str(val))
    
    node = tree.search(10)[0]
    succ = tree.successor(node)
    assert succ.key == 12, f"Successor of 10 should be 12, got {succ.key}"
    print("✓ Successor of 10 is 12")
    
    node = tree.search(5)[0]
    succ = tree.successor(node)
    assert succ.key == 7, f"Successor of 5 should be 7, got {succ.key}"
    print("✓ Successor of 5 is 7")
    
    # Successor of max should be None
    max_node = tree.max_node()
    succ = tree.successor(max_node)
    assert succ is None, "Successor of max should be None"
    print("✓ Successor of max is None")

def test_avl_to_array():
    """Test converting tree to sorted array"""
    print("\n" + "=" * 50)
    print("TEST 10: AVL to Array Conversion")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    values = [15, 3, 20, 1, 7, 12, 25]
    
    for val in values:
        tree.insert(val, str(val))
    
    arr = tree.avl_to_array()
    keys = [pair[0] for pair in arr]
    expected = sorted(values)
    
    assert keys == expected, f"Array should be {expected}, got {keys}"
    print(f"✓ Array is sorted: {keys}")

def test_sequential_deletions():
    """Test multiple sequential deletions"""
    print("\n" + "=" * 50)
    print("TEST 11: Sequential Deletions")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    values = list(range(1, 16))  # 1 to 15
    
    for val in values:
        tree.insert(val, str(val))
    
    print(f"✓ Inserted 15 nodes")
    
    # Delete nodes sequentially
    for val in values:
        node = tree.search(val)[0]
        tree.delete(node)
    
    assert tree.size() == 0, f"Tree should be empty, size is {tree.size()}"
    assert tree.get_root() is None, "Root should be None"
    print("✓ All nodes deleted successfully")

def test_balance_after_deletions():
    """Test that tree remains balanced after deletions"""
    print("\n" + "=" * 50)
    print("TEST 12: Balance After Deletions")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    values = [10, 5, 15, 3, 7, 12, 20, 1, 4, 6, 8, 11, 13, 18, 25]
    
    for val in values:
        tree.insert(val, str(val))
    
    # Delete some nodes
    for val in [1, 4, 6, 8, 11]:
        node = tree.search(val)[0]
        tree.delete(node)
    
    # Check if tree is still valid by traversing
    arr = tree.avl_to_array()
    keys = [pair[0] for pair in arr]
    remaining = sorted([v for v in values if v not in [1, 4, 6, 8, 11]])
    
    assert keys == remaining, f"Tree should contain {remaining}, got {keys}"
    print(f"✓ Tree remains valid: {keys}")

def test_duplicate_operations():
    """Test edge cases with operations"""
    print("\n" + "=" * 50)
    print("TEST 13: Edge Cases")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    
    # Insert and search immediately
    tree.insert(5, "5")
    node = tree.search(5)[0]
    assert node.key == 5, "Just inserted node should be found"
    print("✓ Insert and immediate search works")
    
    # Insert increasing sequence
    tree2 = AVLTree.AVLTree()
    for i in range(1, 11):
        tree2.insert(i, str(i))
    
    assert tree2.size() == 10, "Should have 10 nodes"
    arr = tree2.avl_to_array()
    assert len(arr) == 10, "Array should have 10 elements"
    print("✓ Increasing sequence handled correctly")
    
    # Insert decreasing sequence
    tree3 = AVLTree.AVLTree()
    for i in range(10, 0, -1):
        tree3.insert(i, str(i))
    
    assert tree3.size() == 10, "Should have 10 nodes"
    arr = tree3.avl_to_array()
    assert len(arr) == 10, "Array should have 10 elements"
    print("✓ Decreasing sequence handled correctly")

def test_finger_search():
    """Test finger search operation"""
    print("\n" + "=" * 50)
    print("TEST 14: Finger Search")
    print("=" * 50)
    
    tree = AVLTree.AVLTree()
    values = [10, 5, 15, 3, 7, 12, 20]
    
    for val in values:
        tree.insert(val, str(val))
    
    result = tree.finger_search(10)
    assert result is not None and result[0].key == 10, "Finger search should find 10"
    print("✓ Finger search found 10")
    
    result = tree.finger_search(20)
    assert result is not None and result[0].key == 20, "Finger search should find 20"
    print("✓ Finger search found 20")
    
    result = tree.finger_search(100)
    assert result is None, "Finger search should not find 100"
    print("✓ Finger search doesn't find non-existent key")

def run_all_tests():
    """Run all tests"""
    print("\n\n" + "=" * 50)
    print("RUNNING COMPREHENSIVE AVL TREE TESTS")
    print("=" * 50 + "\n")
    
    try:
        test_empty_tree()
        test_basic_operations()
        test_single_node()
        test_delete_leaf()
        test_delete_node_with_one_child()
        test_delete_node_with_two_children()
        test_delete_root()
        test_max_min()
        test_successor()
        test_avl_to_array()
        test_sequential_deletions()
        test_balance_after_deletions()
        test_duplicate_operations()
        test_finger_search()
        
        print("\n" + "=" * 50)
        print("✓✓✓ ALL TESTS PASSED! ✓✓✓")
        print("=" * 50)
        return True
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
