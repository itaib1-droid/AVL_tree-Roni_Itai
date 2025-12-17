"""
Generator for test data for AVL Finger Tree insertion sort analysis.
Creates 4 different array types for each size n = i * 300 * 2, where i = 1, 2, ..., 10
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





for i in range(1, 11):
    n = 300 *  2 ** i # 300 * 2^i
    print(f"Generating data for i={i}, n={n}...")
    arr = generate_sorted_ascending(n)

    T = AVLTree()
    balancing = 0
    for num in arr:
        balancing += T.finger_insert(num, "0")[2]

    print(f"Total balancing operations for ascending array of size {n}: {balancing}")


        












'''
def generate_all_test_data():
    """Generate all test data for all sizes and trials"""
    
    test_data = {}
    
    # For each i from 1 to 10
    for i in range(1, 11):
        n = 300 *  2 ** i # 300 * 2^i
        print(f"Generating data for i={i}, n={n}...")
        
        test_data[n] = {}
        
        # Trial 1: Ascending
        test_data[n]["ascending"] = generate_sorted_ascending(n)
        print(f"  ✓ Ascending sorted array (trial 1)")
        
        # Trial 2: Descending
        test_data[n]["descending"] = generate_sorted_descending(n)
        print(f"  ✓ Descending sorted array (trial 2)")
        
        # Trial 3: Random
        test_data[n]["random"] = generate_random(n)
        print(f"  ✓ Random array (trial 3)")
        
        # Trial 4: Partially shuffled
        test_data[n]["partially_shuffled"] = generate_partially_shuffled(n)
        print(f"  ✓ Partially shuffled array (trial 4)")
    
    return test_data

def save_test_data(test_data, filename="test_data.json"):
    """Save test data to JSON file"""
    print(f"\nSaving test data to {filename}...")
    with open(filename, 'w') as f:
        json.dump(test_data, f)
    print(f"✓ Test data saved successfully!")

def load_test_data(filename="test_data.json"):
    """Load test data from JSON file"""
    print(f"Loading test data from {filename}...")
    with open(filename, 'r') as f:
        test_data = json.load(f)
    print(f"✓ Test data loaded successfully!")
    return test_data

def get_array_info():
    """Print information about generated arrays"""
    print("\n" + "=" * 70)
    print("TEST DATA ARRAY INFORMATION")
    print("=" * 70)
    print("\nArray sizes (n = i * 300 * 2):")
    print("-" * 70)
    
    for i in range(1, 11):
        n = i * 300 * 2
        print(f"  i={i:2d}: n={n:5d} elements")
    
    print("\n" + "=" * 70)
    print("TRIAL TYPES:")
    print("=" * 70)
    print("  Trial 1: Ascending sorted (small to large)")
    print("  Trial 2: Descending sorted (large to small)")
    print("  Trial 3: Random order")
    print("  Trial 4: Partially shuffled (50% chance to swap adjacent pairs)")
    print("\n" + "=" * 70)

if __name__ == "__main__":
    # Set random seed for reproducibility (optional)
    # random.seed(42)
    
    # Print array information
    get_array_info()
    
    # Generate all test data
    print("\n" + "=" * 70)
    print("GENERATING TEST DATA")
    print("=" * 70 + "\n")
    test_data = generate_all_test_data()
    
    # Save to file
    print("\n" + "=" * 70)
    save_test_data(test_data)
    
    # Print summary
    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total arrays generated: {len(test_data)} sizes × 4 trials = {len(test_data) * 4} arrays")
    total_elements = sum(n * 4 for n in test_data.keys())
    print(f"Total elements across all arrays: {total_elements:,}")
    print("=" * 70 + "\n")

'''