import os
import sys
import unittest

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from medianOfTwoSortedArrays4 import Solution

class TestSolutionClass(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def testFindMedianSortedArrays1(self):
        self.assertEqual(self.s.findMedianSortedArrays([1, 3], [2]), 2.0)

    def testFindMedianSortedArrays2(self):
        self.assertEqual(self.s.findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def testFindMedianSortedArrays3(self):
        self.assertEqual(self.s.findMedianSortedArrays([], [2, 3]), 2.5)

    def testFindMedianSortedArrays4(self):
        self.assertEqual(self.s.findMedianSortedArrays([1,2], [-1,3]), 1.5)

    def testFindMedianSortedArrays5(self):
        self.assertEqual(self.s.findMedianSortedArrays([1], [2,3]), 2)

    def testFindMedianSortedArrays6(self):
        self.assertEqual(self.s.findMedianSortedArrays([1,2,4], [3]), 2.5)

    def testFindMedianSortedArrays7(self):
        self.assertEqual(self.s.findMedianSortedArrays([5], [1,2,3,4,6]), 3.5)

        
    

if __name__ == '__main__':
    unittest.main()
