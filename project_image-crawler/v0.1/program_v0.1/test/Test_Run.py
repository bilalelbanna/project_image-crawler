# -*- coding: utf-8 -*-
"""
Run unit-tests in Folder /test/
@author: Bilal El Banna
Date: 06 November 2015
"""
import os, sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
import glob

def main():



   test_files = glob.glob('unittest_*.py')
   modules = [str[0:len(str)-3] for str in test_files]
   suites = [unittest.defaultTestLoader.loadTestsFromName(str) for str
              in modules]
   testSuite = unittest.TestSuite(suites)
   text_runner = unittest.TextTestRunner().run(testSuite)
   
   raw_input("Press Enter to exit Unit-test." )


            
        
if __name__ == "__main__":
    main()