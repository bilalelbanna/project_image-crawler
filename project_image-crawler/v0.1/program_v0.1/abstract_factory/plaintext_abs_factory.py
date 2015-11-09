# -*- coding: utf-8 -*-
"""
Abstract factory to detect and process plaintext files, applying specified 
routines on each data type after detection, using python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""

import os, sys
sys.path.insert(0, os.path.abspath(".."))

from abc import ABCMeta 
from libs.txt_handler import Txt_Container

#Abstract Factory
class plaintext_factory(object):
    '''
    Abstract factory for handling plaintext files and further processing.
    
     Supported type(s):
     - .txt-Files
    '''    
    
    @staticmethod
    def get_plaintext(path):
        type_ = Txt_Container(path).get_type()
        if type_ == '.txt-File':
            return txt_factory(path)
        raise TypeError('File format not compatible')
        
    


#Factory
class txt_factory(object):
    '''
    Factory which handles .txt-Files
    '''
    
    def __init__(self,path):
        self.__path = path
        
    def get_txt(self):
        return txt_processing(self.__path);


    
# Product Interface
class type_(object):
    __metaclass__ = ABCMeta
    def process(self):
        pass
        
        
# Products
class txt_processing(object):
    '''
    Products of "plaintext_factory", using the txt_handler class in libs.
    '''
    
    def __init__(self, path):
        self.__path = path  
        self.__init_text = Txt_Container(self.__path)
        
    def get_lines(self):
        lines = self.__init_text.get_lines_txt()
        return lines
        
    def get_name(self):
        name = self.__init_text.get_name()
        return name
        
    def get_size(self):
        size = self.__init_text.get_size()
        return size 
        
