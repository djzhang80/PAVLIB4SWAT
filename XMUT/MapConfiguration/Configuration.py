import json
from jsonpath_ng.ext import parse
import os
from datetime import datetime, timedelta
class Configuration:
    
    def getBaseConfig(self,longitude:float,latitude:float,zoom:float) -> dict:
        return {
            'version': 'v1',
            'config': {
                'mapState': {
                    'latitude': latitude,
                    'longitude': longitude,
                    'zoom': zoom,
                    "bearing": 1.7306903622693106,
                    "dragRotate": True,
                    "pitch": 50.27522937918078,
                    "isSplit": False
                },
                "mapStyle": {
                    "styleType": "satellite"
                }
            }
        }
        
    def getConfigByType(self,type="ts_rivers",dataid=None,startdate=None)->dict:
        #print(TS_rivers.config)
        match type:
            case "scenarios":
                from .scenarios import config
            case "ts_trip_discharges":
                from .TS_trip_discharges import config
            case "ts_rivers":
                from .TS_rivers import config
            case "ts_subbasins":
                from .TS_subbasins import config
            case "rivers":
                from .rivers import config
            case "subbasins":
                from .subbasins import config
            case "outlets":
                from .outlets import config
            case "raingauges":
                from .raingauges import config
            case "tempgauges":
                from .tempgauges import config
            case "ts_raingauges":
                from .TS_raingauges import config
            case _:
                pass
        

        if dataid!=None:
            #old_dataid=parse(r'$.config.visState.layers[0].config.dataId').find(config)[0].value
            expression=parse(r'$.config.visState.layers[*].config.dataId')
            expression.update(config,dataid)
            expression=parse(r'$.config.visState.filters[*].dataId')
            expression.update(config,[dataid])
            #config["config"]["visState"]["interactionConfig"]["tooltip"]["fieldsToShow"][dataid]=config["config"]["visState"]["interactionConfig"]["tooltip"]["fieldsToShow"].pop(old_dataid)

        if startdate!=None:
            expression=parse(r'$.config.visState.filters[*].value')
            enddate=startdate+timedelta(days=1)
            #print(int(datetime.fromisoformat(startdate.isoformat()).timestamp()*1000))
            expression.update(config,[int(datetime.fromisoformat(startdate.isoformat()).timestamp()*1000),int(datetime.fromisoformat(enddate.isoformat()).timestamp()*1000)])
        
        return config
    
    
    def mergeConfig(self,src:dict,dest:dict,layer=True,filter=True):
        
        if layer:
            dest["config"]["visState"]["layers"]=dest["config"]["visState"]["layers"]+src["config"]["visState"]["layers"]
            
        if filter:
            dest["config"]["visState"]["filters"]=dest["config"]["visState"]["filters"]+src["config"]["visState"]["filters"]

        return dest    
    
    def setBaseConfig(self,src:dict,dest:dict):
        
        dest["config"]["mapState"]=src["config"]["mapState"]    
        dest["config"]["mapStyle"]=src["config"]["mapStyle"]

        return dest    

                
                
            
