import json
import copy
from datetime import datetime
from keplergl import KeplerGl
import pandas as pd

class KeplerMap:
    
    map=KeplerGl()
    
    def renderToHtml(self):
        return self.map
    
    def addLayer(self,data:dict,layerid:str):
        self.map.add_data(data,layerid)

    def setConfigure(self,config):
        if config!=None:
            self.map.config=config
    
    def save(self,filename):
        self.map.save_to_html(file_name=filename)