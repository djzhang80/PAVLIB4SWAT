from .DataProviderInterface import ProviderInterface
from datetime import datetime, date, timedelta
from . import Util
import pandas as pd
import json
import copy

class RCHTripLayerProvider(ProviderInterface):
    def get_token(self,index:int,line:str)->str:
        return line.split()[index]
    

    def convert(self, inputfile: str, outputfile: str, **kvargs):    
        if "subnum" in kvargs:
            sub_number=kvargs["subnum"]
        else:
            sub_number=5
        
        if "rivergeojson" in kvargs:
            rivergeojson=kvargs["rivergeojson"]
        else:
            rivergeojson="rivers.json"
            
        if "ciofile" in kvargs:
            ciofile=kvargs["ciofile"]
        else:
            ciofile="file.cio"
            
        if "dividen" in kvargs:
            dividen=kvargs["dividen"]
        else:
            dividen=10
        
        f1=open(inputfile)
        lines=f1.readlines()
        lines=lines[9:]

        desired_list_of_tuple=[(int(self.get_token(1,line)),float(self.get_token(5,line))) for line in lines]

        df=pd.DataFrame(data=desired_list_of_tuple,columns=["rch_no","discharge"])
        df.reset_index(inplace=True)
        df.rename(columns={"index":"date"},inplace=True)
        
        swatUtil=Util.SWATUtil()
        startDate=swatUtil.getStartDate(swatiofile=ciofile)
        df["date"]=df["date"].apply(lambda x:timedelta(days=divmod(x,sub_number)[0])+startDate)

        endDate=df["date"].max()
        f1.close()
        f=open(rivergeojson)
        data=json.load(f)
        discharge=copy.deepcopy(data)

        discharge["features"]=[]
        dt_obj=datetime.now()
        ms=int(dt_obj.timestamp() * 1000)

        for d1 in pd.date_range(startDate,endDate):
            #print(d1.timestamp())
            for feature in data["features"]:
                #del feature["properties"]
                rch=feature["properties"]["Subbasin"]
                dis=df.loc[(df["rch_no"]==rch) &  (df["date"]==d1.to_pydatetime().date()),"discharge"] 
                point_number=len(feature["geometry"]["coordinates"])
                particle_number=int(dis/dividen)+1
                #print(point_number)
                for k in range(0,particle_number):
                    item=copy.deepcopy(feature)
                    del item["properties"]
                    for i in range(0,point_number):
                        point=item["geometry"]["coordinates"][i]
                        point.append(0)
                        point.append(d1.timestamp()*1000+int(86400/(point_number+particle_number))*(i+k))
                    discharge["features"].append(item)
        f.close()
        
        with open(outputfile,"w") as f:
            json.dump(discharge,f) 



