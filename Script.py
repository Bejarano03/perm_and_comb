import math
import unittest

def permutations(n, r):
    return math.factorial(n) // math.factorial( n - r)

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def main():
    print("Permutation and Combination Calculator")
    try:
        n = int(input("Enter the total number of items (n): "))
        r = int(input("Enter the number of items to choose/arrange (r): "))
        if n < 0 or r < 0 or r > n:
            print("Please ensure that n and r are non-negative and n >=r.")
            return
        p = permutations(n, r)
        c = combinations(n, r)
        print(f"\nPermutations P({n}, {r}) = {p}")
        print(f"Combinations C({n}, {r}) = {c}")
    except ValueError:
        print("Please enter valid integers for n and r.")

class TestPermComb(unittest.TestCase):
    # Normal cases
    def test_perm_normal_1(self):
        self.assertEqual(permutations(5, 2), 20)
        self.assertEqual(combinations(5, 2), 10)

    def test_perm_normal_2(self):
        self.assertEqual(permutations(6, 3), 120)
        self.assertEqual(combinations(6, 3), 20)

    def test_perm_normal_3(self):
        self.assertEqual(permutations(10, 0), 1)
        self.assertEqual(combinations(10, 0), 1)

    # Edge cases
    def test_perm_edge_n_equals_r(self):
        self.assertEqual(permutations(4, 4), 24)
        self.assertEqual(combinations(4, 4), 1)

    def test_perm_edge_r_greater_than_n(self):
        with self.assertRaises(ValueError):
            permutations(3, 5)
        with self.assertRaises(ValueError):
            combinations(3, 5)

    def test_perm_edge_negative_input(self):
        with self.assertRaises(ValueError):
            permutations(-5, 2)
        with self.assertRaises(ValueError):
            combinations(5, -2)

if __name__ == "__main__":
    main()
    #unittest.main()