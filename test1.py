"""
Balancing cost analysis for AVL Finger Tree insertion.
Tests balancing operations (PROMOTE) cost during insertion for different array types.
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

def measure_balancing_cost(array_type, n):
    """
    Measure balancing cost (total PROMOTE operations) during insertion.
    
    Parameters:
    - array_type: name of the array type ('ascending', 'descending', 'random', 'partially_shuffled')
    - n: size of the array
    
    Returns:
    - Dictionary with balancing cost statistics
    """
    print(f"\n{'='*70}")
    print(f"Testing Balancing Cost for: {array_type.upper()}")
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
    
    # Build the tree using finger_insert and count PROMOTE operations
    tree = AVLTree()
    total_promotes = 0
    promote_costs = []
    
    print(f"\nInserting {n} elements...")
    for val in arr:
        # finger_insert returns (node, edges, promotes)
        node, edges, promotes = tree.finger_insert(val, str(val))
        total_promotes += promotes
        promote_costs.append(promotes)
    
    # Calculate statistics
    avg_promote_cost = total_promotes / n if n > 0 else 0
    max_promote_cost = max(promote_costs) if promote_costs else 0
    min_promote_cost = min(promote_costs) if promote_costs else 0
    
    # Theoretical analysis
    import math
    theoretical_logn = n * math.log2(n + 1) if n > 0 else 0
    
    print(f"Total PROMOTE operations: {total_promotes}")
    print(f"Average PROMOTE per insertion: {avg_promote_cost:.2f}")
    print(f"Min PROMOTE in single insertion: {min_promote_cost}")
    print(f"Max PROMOTE in single insertion: {max_promote_cost}")
    print(f"Theoretical n*log(n): {theoretical_logn:.0f}")
    
    return {
        'array_type': array_type,
        'n': n,
        'total_promotes': total_promotes,
        'avg_cost': avg_promote_cost,
        'min_cost': min_promote_cost,
        'max_cost': max_promote_cost,
        'theoretical_nlogn': theoretical_logn
    }


# ============================================
# TEST 1: ASCENDING ORDER ARRAY
# ============================================
def test_balancing_ascending():
    """Test balancing cost for sorted ascending arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 1: BALANCING COST - ASCENDING ORDER ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 111 * (2 ** i)
        result = measure_balancing_cost('ascending', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Ascending Order Balancing Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total PROMOTE':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_promotes']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# TEST 2: DESCENDING ORDER ARRAY
# ============================================
def test_balancing_descending():
    """Test balancing cost for sorted descending arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 2: BALANCING COST - DESCENDING ORDER ARRAYS (WORST CASE)")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 111 * (2 ** i)
        result = measure_balancing_cost('descending', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Descending Order Balancing Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total PROMOTE':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_promotes']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# TEST 3: RANDOM ORDER ARRAY
# ============================================
def test_balancing_random():
    """Test balancing cost for random order arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 3: BALANCING COST - RANDOM ORDER ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 111 * (2 ** i)
        result = measure_balancing_cost('random', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Random Order Balancing Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total PROMOTE':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_promotes']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# TEST 4: PARTIALLY SHUFFLED ARRAY
# ============================================
def test_balancing_partially_shuffled():
    """Test balancing cost for partially shuffled arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 4: BALANCING COST - PARTIALLY SHUFFLED ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 11):
        n = 111 * (2 ** i)
        result = measure_balancing_cost('partially_shuffled', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Partially Shuffled Balancing Cost:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Total PROMOTE':<20} {'Avg Cost':<15} {'Max Cost':<15}")
    print(f"{'-'*70}")
    for r in results:
        i = int(r['n'] / 300).bit_length() - 1
        print(f"{i:<5} {r['n']:<10} {r['total_promotes']:<20} {r['avg_cost']:<15.2f} {r['max_cost']:<15}")

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    # Choose which test to run by uncommenting one of the lines below:
    
    test_balancing_ascending()
    # test_balancing_descending()
    # test_balancing_random()
    # test_balancing_partially_shuffled()
