# -*- coding: utf-8 -*-
"""
Configuration File

@author: Bilal El Banna
Date: 06 November 2015
"""
import os

conf = dict(txt_path = os.getcwd()+r'/data/links_plaintext.txt',
             save_path = os.getcwd()+r'/storage',
             database_path = os.getcwd()+r'/database/image.db',
             db_type = 'sqlite')
    
