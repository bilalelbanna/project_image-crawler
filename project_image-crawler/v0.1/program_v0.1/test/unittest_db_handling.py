# -*- coding: utf-8 -*-
"""
Applying unit-tests on module db_handling.py , using
python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import os, sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
import sqlite3
from libs.db_handling import DB_Handling

class Test_db_handling(unittest.TestCase):
    '''
    Class with methods to apply unit-tests on.    
    '''
    def setUp(self):
        self.__path = "test_files/unittest_db_handling_test_db.db"
        self.__database =  DB_Handling(self.__path)
                                 
        
    def test_create_db(self):
        '''
        Unit-test to check if a database and an images table are created.
        '''
        
        self.__database.create_db()
        db_file = os.path.isfile(self.__path)
        self.assertIs((db_file),True)
    
        return
        

    def test_populate_db(self):
        '''
        Unit-test to check if inserted data is in the databes table.
        '''       
        
        info_list = ["image_name",  "image_url","image_local_path"]
        self.__database.populate_db([info_list])

        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM images") 
        res = cursor.fetchone() 
        self.assertIs(res[0],1)
        for i in range(1,4,1):
            self.assertEqual(res[i],info_list[i-1])
        

        return connection.close()
        
        
    

if __name__ == '__main__':
    unittest.main(exit=False)