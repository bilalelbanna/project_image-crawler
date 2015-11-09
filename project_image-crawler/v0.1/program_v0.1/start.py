# -*- coding: utf-8 -*-
"""
Starting image crawler v0.1
Author: Bilal El Banna
Date: 06 November 2015
"""

##############################Imports#########################################
import os, sys
sys.path.insert(0, os.path.abspath(".."))

from libs.pic_handler import Pic_Handler
from configuration import config
from abstract_factory import plaintext_abs_factory
from abstract_factory import database_abs_factory
import time

##############################Main############################################

def main():
    print ("Start of process...")
    
    #configuration parameters
    start = time.time()
    txt_path = config.conf["txt_path"]
    save_path = config.conf["save_path"]
    database_path = config.conf["database_path"]
    db_type = config.conf["db_type"]
    
    #use plaintext abstract factory
    txt_abs_factory = plaintext_abs_factory.plaintext_factory()
    txt_factory = txt_abs_factory.get_plaintext(txt_path)
    txt_prod = txt_factory.get_txt()
    URLs = txt_prod.get_lines()
    #use images abstract factory
    init_pics = Pic_Handler(URLs,save_path)
    pics_info = init_pics.pic_info()
    init_pics.pic_save()
    #use database abstract factory
    db_abs_factory = database_abs_factory.database_factory()
    db_factory = db_abs_factory.db_abs_fac(db_type,database_path)
    db_prod = db_factory.process_sql()
    db_prod.create_db()
    db_prod.populate_db(pics_info)
    
    print ("End of process" )
    end = time.time()
    print ("Process time: ", str(round(end-start,2)),"sec")
    raw_input("Press enter to exit.")       
        
if __name__ == "__main__":
    main()
    
##############################End of Script###################################