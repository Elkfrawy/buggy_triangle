# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(3,5,4),'Right','3,5,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isosceles', '3, 3, 5 should be isosceles')

    def testIsoscelesTriangles2(self):
        self.assertEqual(classifyTriangle(3, 5, 3), 'Isosceles', '3, 5, 3 should be isosceles')

    def testIsoscelesTriangles3(self):
        self.assertEqual(classifyTriangle(5, 3, 3), 'Isosceles', '5, 3, 3 should be isosceles')

    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4, 7, 10), 'Scalene', '4, 7, 10 should be scalene')

    def testNotTriangles(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1, 2, 3 should not be a triangle')

    def testNotTriangles2(self):
        self.assertEqual(classifyTriangle(1, 2, 5), 'NotATriangle', '1, 2, 5 should not be a triangle')

    def testNotTriangles3(self):
        self.assertEqual(classifyTriangle(5, 1, 2), 'NotATriangle', '5, 1, 2 should not be a triangle')

    def testNotTriangles4(self):
        self.assertEqual(classifyTriangle(1, 5, 2), 'NotATriangle', '1, 5, 2 should not be a triangle')

    def testInvalidInput_tooLongSide(self):
        self.assertEqual(classifyTriangle(250, 130, 150), 'InvalidInput', '250 should be invalid input')

    def testInvalidInput_tooLongSide2(self):
        self.assertEqual(classifyTriangle(130, 250, 150), 'InvalidInput', '250 should be invalid input')

    def testInvalidInput_tooLongSide3(self):
        self.assertEqual(classifyTriangle(130, 150, 250), 'InvalidInput', '250 should be invalid input')

    def testInvalidInput_negativeSide(self):
        self.assertEqual(classifyTriangle(-5, 1, 5), 'InvalidInput', '-5 should be invalid input')

    def testInvalidInput_negativeSide2(self):
        self.assertEqual(classifyTriangle(1, -5, 5), 'InvalidInput', '-5 should be invalid input')

    def testInvalidInput_negativeSide3(self):
        self.assertEqual(classifyTriangle(5, 1, -5), 'InvalidInput', '-5 should be invalid input')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

