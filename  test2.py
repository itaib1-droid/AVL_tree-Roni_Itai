"""
Generator for test data for AVL Finger Tree insertion sort analysis.
Creates 4 different array types for each size n = i * 300 * 2, where i = 1, 2, ..., 5
"""

import random
import json
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




def count_inversions(arr):
    """
    Count the number of inversions in array.
    An inversion is a pair (i, j) where i < j but arr[i] > arr[j]
    Time complexity: O(n^2) for simplicity, but acceptable for this use case
    """
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                count += 1
    return count

def test_inversion_count(array_type, n):
    """
    Test inversion count for a specific array type
    
    Parameters:
    - array_type: name of the array type ('ascending', 'descending', 'random', 'partially_shuffled')
    - n: size of the array
    """
    print(f"\n{'='*70}")
    print(f"Testing Inversions for: {array_type.upper()}")
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
    
    # Count inversions
    inversions = count_inversions(arr)
    
    # Show some statistics
    max_possible_inversions = n * (n - 1) // 2
    inversion_ratio = (inversions / max_possible_inversions) * 100 if max_possible_inversions > 0 else 0
    
    print(f"Number of inversions (I): {inversions}")
    print(f"Max possible inversions: {max_possible_inversions}")
    print(f"Inversion ratio: {inversion_ratio:.2f}%")
    
    return {
        'array_type': array_type,
        'n': n,
        'inversions': inversions,
        'max_possible': max_possible_inversions,
        'inversion_ratio': inversion_ratio
    }



# Template for testing each array type separately
# Uncomment and run the array type you want to test

# ============================================
# TEST 1: ASCENDING ORDER ARRAY
# ============================================
def test_ascending():
    """Test inversion count for sorted ascending arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 1: ASCENDING ORDER ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 6):
        n = 300 * (2 ** i)
        result = test_inversion_count('ascending', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Ascending Order:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Inversions (I)':<20} {'I/Max (%)':<15}")
    print(f"{'-'*70}")
    for r in results:
        print(f"{r['n']//600:<5} {r['n']:<10} {r['inversions']:<20} {r['inversion_ratio']:<15.2f}")

# ============================================
# TEST 2: DESCENDING ORDER ARRAY
# ============================================
def test_descending():
    """Test inversion count for sorted descending arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 2: DESCENDING ORDER ARRAYS (WORST CASE)")
    print("#"*70)
    
    results = []
    for i in range(1, 6):
        n = 300 * (2 ** i)
        result = test_inversion_count('descending', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Descending Order:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Inversions (I)':<20} {'I/Max (%)':<15}")
    print(f"{'-'*70}")
    for r in results:
        print(f"{r['n']//600:<5} {r['n']:<10} {r['inversions']:<20} {r['inversion_ratio']:<15.2f}")

# ============================================
# TEST 3: RANDOM ORDER ARRAY
# ============================================
def test_random():
    """Test inversion count for random order arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 3: RANDOM ORDER ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 6):
        n = 300 * (2 ** i)
        result = test_inversion_count('random', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Random Order:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Inversions (I)':<20} {'I/Max (%)':<15}")
    print(f"{'-'*70}")
    for r in results:
        print(f"{r['n']//600:<5} {r['n']:<10} {r['inversions']:<20} {r['inversion_ratio']:<15.2f}")

# ============================================
# TEST 4: PARTIALLY SHUFFLED ARRAY
# ============================================
def test_partially_shuffled():
    """Test inversion count for partially shuffled arrays"""
    print("\n\n" + "#"*70)
    print("# TEST 4: PARTIALLY SHUFFLED ARRAYS")
    print("#"*70)
    
    results = []
    for i in range(1, 6):
        n = 300 * (2 ** i)
        result = test_inversion_count('partially_shuffled', n)
        results.append(result)
    
    # Summary table
    print(f"\n{'='*70}")
    print("Summary Table - Partially Shuffled:")
    print(f"{'='*70}")
    print(f"{'i':<5} {'n':<10} {'Inversions (I)':<20} {'I/Max (%)':<15}")
    print(f"{'-'*70}")
    for r in results:
        print(f"{r['n']//600:<5} {r['n']:<10} {r['inversions']:<20} {r['inversion_ratio']:<15.2f}")

# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    # Choose which test to run by uncommenting one of the lines below:
    
    # test_ascending()
    # test_descending()
    # test_random()
    test_partially_shuffled()