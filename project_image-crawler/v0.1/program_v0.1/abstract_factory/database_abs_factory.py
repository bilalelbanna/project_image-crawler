# -*- coding: utf-8 -*-
"""
Abstract factory to create and apply specialized routines on databases, 
after type input and database path, by using python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""

import os, sys
sys.path.insert(0, os.path.abspath(".."))

from abc import ABCMeta 
from libs.db_handling import DB_Handling

#Abstract Factory
class database_factory(object):
    '''
    Abstract factory for detecting database format and further processing.
    
     Supported type(s):
    - sqlite
    '''       
    
    @staticmethod
    def db_abs_fac(type_db,path):
        if type_db == 'sqlite':
            return db_sql_factory(path)
        raise TypeError('Database format not supported')
        
    


#Factory
class db_sql_factory(object):
    '''
    Factory which handles sqlite databases.
    '''
    def __init__(self,path):
        self.__path = path
        
    def process_sql(self):
        return sql_processing(self.__path);


    
# Product Interface
class type_(object):
    __metaclass__ = ABCMeta
    def process(self):
        pass
        
        
# Products
class sql_processing(object):
    '''
    Products of "db_sql_factory", using the db_handling class in libs.
    '''
    
    def __init__(self, path):
        self.__path = path  
        self.__init_db = DB_Handling(self.__path)
        
    def create_db(self):
        self.__init_db.create_db()
        return
        
    def populate_db(self, info_list):
        self.__init_db.populate_db(info_list)
        
