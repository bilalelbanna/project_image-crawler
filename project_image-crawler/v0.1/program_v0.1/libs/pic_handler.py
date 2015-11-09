# -*- coding: utf-8 -*-
"""
Module with class methods to process input URLs of images, 
using python's standard libraries.
To properly use the module, Python 2.7 or higher is required.

Author: Bilal El Banna
Date: 06 November 2015
"""
import urllib
import urllib2
import os

class Pic_Handler:
    '''
    Class with methods 
    -to retrieve the image's information.
    -to bundle the image URLs in a container.
    -to save the Image locally. 
    
    Class Objects:
    
    url =  URL from which the image shall be retrieved
    (empty Default-Parameter).
    
    save_path = Local save path of the image. 
    (Default-Parameter is the root directory).
    
    url_container = list with image URLs. 
    (Default-Parameter is an empty list).
    '''
    
    def __init__ (self,urls,save_path):
        self.__urls = urls
        self.__save_path = save_path
        
    def pic_info(self):
        '''
        Method retrieve the image's information and check if URL could be 
        retrieved.
        
        Following inforamtion are retrieved:
        - Name of the image
        - URL of the image
        - Local save path of the image
        
        Method return(s):
        new_name = Name of the image
        self.__url = URL of the image
        self.__save_path = Local save path of the image
        '''
        info_list = []
        for url in self.__urls:
            
            new_name = ""
            for chars in url:
                if chars != "/" and chars != ":":
                    new_name =  new_name+chars
            try:
                urllib2.urlopen(urllib2.Request(url))
                info_list.append([new_name,url,self.__save_path])
            except:
                info_list.append([new_name,"link corrupted","can't be saved"])
        return info_list

    def pic_save(self):
        '''
        Method to save the image locally.
        
        Method return(s):
        return 1 for later testing
        '''
                
        init_info = Pic_Handler(self.__urls,self.__save_path)
        pic_info_list = init_info.pic_info()

        for pic_info_list_element in  pic_info_list:
            if pic_info_list_element[1] == "link corrupted":
                continue
            else:
                
#                try:
                complete_path_name = os.path.join(pic_info_list_element[2],
                                                  pic_info_list_element[0])
                
                urllib.urlretrieve(pic_info_list_element[1],
                                   complete_path_name)
#                except:
#                    pass
        return 1
        