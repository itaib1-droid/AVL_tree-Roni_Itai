"""
Search cost analysis for AVL Finger Tree.
Tests search cost (number of comparisons) for different array types.
"""

import random
from AVLTree import AVLTree

def generate_sorted_ascending(n):
    """Trial 1: Array sorted in ascending order (small to large)"""
    return list(range(1, n + 1))

def generate_sorted_descending(n):
    """Trial 2: Array sorted in descending order (large to small)"""
    return list(range(n, 0, -1))

def generate_random(n):
    """Trial 3: Array with random order"""
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    return arr

def generate_partially_shuffled(n):
    """Trial 4: Start with sorted array, then randomly swap adjacent elements with 50% probability"""
    arr = list(range(1, n + 1))
    
    # For each index i from 0 to n-2 (n-1 excluded as per requirement)
    for i in range(n - 1):
        # Swap with next element with 50% probability
        if random.random() < 0.5:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

def measure_search_cost(array_type, n):
    """
    Measure search cost (total comparisons) for searching all elements in array.
    
    Parameters:
    - array_type: name of the array type ('ascending', 'descending', 'random', 'partially_shuffled')
    - n: size of the array
    
    Returns:
    - Dictionary with search cost statistics
    """
    print(f"\n{'='*70}")
    print(f"Testing Search Cost for: {array_type.upper()}")
    print(f"Array size (n): {n}")
    print(f"{'='*70}")
    
    # Generate the array
    if array_type == 'ascending':
        arr = generate_sorted_ascending(n)
    elif array_type == 'descending':
        arr = generate_sorted_descending(n)
    elif array_type == 'random':
        arr = generate_random(n)
    elif array_type == 'partially_shuffled':
        arr = generate_partially_shuffled(n)
    else:
        print(f"Unknown array type: {array_type}")
        return None
    
    # Build the tree using finger_insert
    tree = AVLTree()
    total_insert_comparisons = 0
    
    print(f"\nBuilding tree with finger_insert...")
    for val in arr:
        # finger_insert returns (node, edges, promotes)
        # We need to count comparisons during insertion
        tree.finger_insert(val, str(val))
    
    # Now search for all elements and count total comparisons using finger_search
    print(f"Searching for all {n} elements using finger_search...")
    total_search_comparisons = 0
    search_costs = []
    
    for val in arr:
        # Use finger_search - returns (node, comparisons)
        node, comparisons = tree.finger_search(val)
        total_search_comparisons += comparisons
        search_costs.append(comparisons)
    
    # Calculate statistics
    avg_search_cost = total_search_comparisons / n if n > 0 else 0
    max_search_cost = max(search_costs) if search_costs else 0
    min_search_cost = min(search_costs) if search_costs else 0
    
    # Theoretical optimal (binary search)
    import math
    theoretical_optimal = math.ceil(math.log2(n + 1)) if n > 0 else 0
    
    print(f"Total search comparisons: {total_search_comparisons}")
    print(f"Average search cost: {avg_search_cost:.2f}")
    print(f"Min search cost: {min_search_cost}")
    print(f"Max search cost: {max_search_cost}")
    print(f"Theoretical optimal (log₂ n): {theoretical_optimal}")
    
    return {
        'array_type': array_type,
        'n': n,
        'total_comparisons': total_search_comparisons,
        'avg_cost': avg_search_cost,
        'min_cost': min_search_cost,
        'max_cost': max_search_cost,
        'theoretical_optimal': theoretical_optimal
    }


# ============================================
# TEST 1: ASCENDING ORDER ARRAY
# ============================================
def test_search_ascending():
    """Test search cost for sorted ascending arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 1: SEARCH COST - ASCENDING ORDER ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 300 * (2 ** i)
        result = measure_search_cost('ascending', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Ascending Order Search Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total Comparisons':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_comparisons']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# TEST 2: DESCENDING ORDER ARRAY
# ============================================
def test_search_descending():
    """Test search cost for sorted descending arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 2: SEARCH COST - DESCENDING ORDER ARRAYS (WORST CASE)")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 300 * (2 ** i)
        result = measure_search_cost('descending', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Descending Order Search Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total Comparisons':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_comparisons']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# TEST 3: RANDOM ORDER ARRAY
# ============================================
def test_search_random():
    """Test search cost for random order arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 3: SEARCH COST - RANDOM ORDER ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 300 * (2 ** i)
        result = measure_search_cost('random', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Random Order Search Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total Comparisons':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_comparisons']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# TEST 4: PARTIALLY SHUFFLED ARRAY
# ============================================
def test_search_partially_shuffled():
    """Test search cost for partially shuffled arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 4: SEARCH COST - PARTIALLY SHUFFLED ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 300 * (2 ** i)
        result = measure_search_cost('partially_shuffled', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Partially Shuffled Search Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total Comparisons':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_comparisons']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    # Choose which test to run by uncommenting one of the lines below:
    
   # test_search_ascending()
    # test_search_descending()
    # test_search_random()
    test_search_partially_shuffled()
