# -*- coding: utf-8 -*-
"""
Applying unit-tests on module database_abs_factory , using
python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import os, sys
sys.path.insert(0, os.path.abspath(".."))

import unittest
import sqlite3
from abstract_factory import database_abs_factory


class Test_database_abs_factory(unittest.TestCase):

    def setUp(self):
        self.__path = "test_files/unittest_database_abs_factory_test_db.db"
        self.__db_abs_factory = database_abs_factory.database_factory()
        self.__db_factory =  self.__db_abs_factory.db_abs_fac('sqlite',
                                                              self.__path)
        self.__db_prod = self.__db_factory.process_sql()
                                 
        
    def test_create_db(self):
        '''
        Unit-test to check if a database and an images table are created.
        '''
        
        self.__db_prod.create_db()
        db_file = os.path.isfile(self.__path)
        self.assertIs((db_file),True)
    
        return
        

    def test_populate_db(self):
                       
        '''
        Unit-test to check if inserted data is in the databes table.
        '''       
        info_list = ["image_name",  "image_url","image_local_path"]
        self.__db_prod.populate_db([info_list])

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