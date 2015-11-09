# -*- coding: utf-8 -*-
"""
Module with class methods to create an SQLite database and to populate a database, using
python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import sqlite3
import datetime


class DB_Handling:
    '''
    Class with methods to create and populate image.db.
    
    Class Objects:
    
    path = save path of "image.db"
    
    '''
    def __init__(self, path):
        self.__path = path
    
    def create_db(self):
        '''
        Method to connect to "image.db" and to create the "images" TABLE. 
        If "images" Table does not exist, "images" Table will be created.
        '''
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
#        cursor.execute("DROP TABLE IF EXISTS images;")
        cursor.execute("""CREATE TABLE IF NOT EXISTS images ( 
        image_number INTEGER PRIMARY KEY, 
        image_name TEXT, 
        image_url TEXT, 
        image_local_path TEXT,
        date_stored DATE);""")
        connection.commit()
        
        
        
#        sql_command = """
#        CREATE TABLE images ( 
#        image_number INTEGER PRIMARY KEY, 
#        image_name TEXT, 
#        image_url TEXT, 
#        image_local_path TEXT,
#        date_stored DATE);"""
#        cursor.execute(sql_command)
        
        return connection.close()
        
    def populate_db(self,info_list):
        '''
        Method to connect to "image.db" and to populate the "images" TABLE
        with following information:
        
        - Image's Name
        - Image's URL
        - Image's local save path
        - image's retrievement date    
        
        Method's parameter(s):
        
        info_list = list with the following image information:
        
        -infolist[0]: imge_name = Name of the image.
        
        -info_list[1]: image_url = URL from which the image is retrieved. 
        
        -info_list[2]: image_local_path = Local save path of the image.   
        '''
        connection = sqlite3.connect(self.__path)
        cursor = connection.cursor()
        
        
        format_str = """INSERT INTO images (image_number,
        image_name, image_url, image_local_path,  date_stored)
        VALUES (NULL, "{name}", "{url}",  "{local}","{date}");"""                                     
        
        for info in info_list:
            
            sql_command = format_str.format(name= info[0], 
                                            url = info[1],
                                            local = info[2], 
                                            date = datetime.datetime.now())
            cursor.execute(sql_command)
            connection.commit()
        
        return connection.close()