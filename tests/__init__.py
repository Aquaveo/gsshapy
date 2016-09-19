'''
********************************************************************************
* Name: Tests
* Author: Nathan Swain
* Created On: August 13, 2013
* Copyright: (c) Brigham Young University 2013
* License: BSD 2-Clause
********************************************************************************
'''
import unittest
from read_tests import TestReadMethods
from write_tests import TestWriteMethods
from hrrr_tests import TestHRRRtoGSSHA

def all_tests():
    # Retrieve tests
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestReadMethods)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestWriteMethods)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(TestHRRRtoGSSHA)
    return unittest.TestSuite([suite1, suite2, suite3])

def run_all_tests(verbosity=2):
    # Retrieve tests
    alltests = all_tests()
    
    # Execute all tests
    unittest.TextTestRunner(verbosity=verbosity).run(alltests) 


if __name__  == '__main__':
    run_all_tests(verbosity=2)