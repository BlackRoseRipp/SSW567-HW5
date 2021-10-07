# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

# Original Testcases
class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classify_triangle(5,5,9),'Isosceles','5,5,9 should not be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classify_triangle(3,4,6),'Scalene','3,4,5 should be scalene')

    def testScaleneTriangleB(self):
        self.assertEqual(classify_triangle(6,4,3),'Scalene','6,4,3 should not be scalene')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(3,4,3),'Isosceles','3,4,3 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classify_triangle(3,3,5),'Isosceles','3,3,5 should be isosceles')

    def testInvalidA(self):
        self.assertEqual(classify_triangle(3,0,5),'InvalidInput','A side cannot be 0 or less')

    def testInvalidB(self):
        self.assertEqual(classify_triangle(150,150,201),'InvalidInput','A side cannot be greater than 200')

    def testInvalidC(self):
        self.assertEqual(classify_triangle("150",{},140),'InvalidInput','A side cannot be greater than 200')

    def testNotTriangle(self):
        self.assertEqual(classify_triangle(5,11,5),'NotATriangle','A side cannot be greater than 200')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

