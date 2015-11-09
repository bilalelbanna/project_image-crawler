# -*- coding: utf-8 -*-
"""
Applying unit-tests on module plaintext_abs_factory.py , using
python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import os, sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
from abstract_factory import plaintext_abs_factory


class Test_Txt_Container(unittest.TestCase):

    def setUp(self):
        self.__path = "test_files/test_txt.txt"
        self.__txt_abs_factory = plaintext_abs_factory.plaintext_factory()
        self.__txt_factory = self.__txt_abs_factory.get_plaintext(self.__path)
        self.__txt_prod = self.__txt_factory.get_txt()
        
    def test_get_lines_txt(self):
        '''
        unit-test to check if a list type and the refrence are returned.
        '''
        get_lines = self.__txt_prod.get_lines()
        refrence = "http://bilder.bild.de/fotos/lachsack-36229038/Bild/1.bild.jpg"
        self.assertEqual(type (get_lines), list)
        self.assertEqual(get_lines[0], refrence)
        
        
    def test_get_size(self):
        '''
        unit-test to check if the file size was correctly retrieved.
        '''
        file_size = self.__txt_prod.get_size()
        self.assertEqual(file_size, 61)
        
    def test_get_name(self):
        '''
        unit-test to check if the file name was correctly retrieved.
        '''
        file_name = self.__txt_prod.get_name()
        self.assertEqual(file_name, "test_txt.txt")
    
        


if __name__ == '__main__':
    unittest.main(exit=False)