# -*- coding: utf-8 -*-
"""
Applying unit-tests on module pic_handler.py , using
python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import os, sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
from libs.pic_handler import Pic_Handler

class Test_pic_handler(unittest.TestCase):

    def setUp(self):
        self.__url = ["http://bilder.bild.de/fotos/lachsack-36229038/Bild/1.bild.jpg"]
        self.__save_path = "test_files"
        self.__pic = Pic_Handler(self.__url,self.__save_path)
        
        
    def test_pic_save(self):
        '''
        Method to test if the Save_Pic class returns 1
        '''
        self.assertEqual( self.__pic.pic_save(), 1)
        
    def test_pic_info(self):
        '''
        Method to test if the Save_Pic class returns the right information.
        '''
        pic_info =  self.__pic.pic_info()
        
        self.assertNotIn("/", pic_info[0][0])
        self.assertNotIn(":", pic_info[0][0])
        self.assertIn("http://", pic_info[0][1])
        self.assertEqual(type (pic_info[0][2]), str)


if __name__ == '__main__':
    unittest.main(exit=False)