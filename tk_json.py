# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 21:43:54 2021

@author: talha
"""


import json


class Tk_Json():
    def __init__(self, config_file_name, json_format):
        self._config_file_name = config_file_name
        self._json_format = json_format # nasıl yazmak istiyorsan

    def read_file(self):
        try:
            
            with open(self._config_file_name, "r") as read_file:
                return json.load(read_file)
        except Exception as ex:
            print(ex)
            return self._json_format

    def read_config(self, key):
        try:
            with open(self._config_file_name, "r") as read_file:
                data = json.load(read_file)
                return data[key]
        except Exception as ex:
            return None

    def write_config(self, key, val):
        data = self.read_file()
        data[key] = val
        with open(self._config_file_name, "w") as write_file:
            json.dump(data, write_file)
            
            
if __name__ == '__main__':
    js = Tk_Json("example.json",{"IP": "", "Port": 0}) #initial ayarları
    
    #Config
    js.write_config("IP", "host")
    js.write_config("Port",155)
    
    #Read all config
    print(js.read_file())
    
    #Read spesific key
    print(js.read_config("Port"))
    

