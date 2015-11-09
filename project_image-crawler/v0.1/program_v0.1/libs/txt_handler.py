# -*- coding: utf-8 -*-
"""
Module with  class methods to process input .txt-Files, 
using python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import os


    
class Txt_Container:
    '''
    Class with methods 
    -to retrieve lines in a .txt-File.
    -to retrieve the file's name.
    -to retrieve the file's type.
    -to retrieve the file's size. 
    
    Class Object(s):
    
    path = Local path of the file.
    '''
    def __init__(self, path):
        self.__path = path
        
    def get_lines_txt(self):
        '''
        Method to bundle  each line of a .txt-File in a list.
    
        Function parameter(s): 
        path = Local path of the file.
        
        Function return(s):
        lines_container = list with each line of a .txt-File.
        '''    
        lines_container = []
        plaintext = open(self.__path, "r")
        for line in plaintext:
            lines_container.append(line.strip("\n"))
        plaintext.close()
        return lines_container
        
    def get_name(self):
        '''
        Method to retrieve the file's name.
        
        Method return(s):
        name = Name of file.
        '''
        split = self.__path.split("/")
        name = split[-1]
        return name
        
    def get_type(self):
        '''
        Method to retrieve the file's type.
        
        Method return(s):
        type_ = type of file.
        '''        
        split = self.__path.split(".")
        ending = split[-1]
        type_ = "."+ending+"-File"
        return type_
    
    def get_size(self):
        '''
        Method to retrieve the file's size.
        
        Method return(s):
        size_info = size of file.
        '''        
        size_info = os.stat(self.__path).st_size
        return size_info