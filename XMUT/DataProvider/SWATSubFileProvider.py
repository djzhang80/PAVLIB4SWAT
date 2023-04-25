from .DataProviderInterface import ProviderInterface
from datetime import datetime, date, timedelta
from . import Util
import pandas as pd
import json
import copy


class SUBProvider(ProviderInterface):
    
    def retrieve_feature(self,index:int,subs:dict)->dict|None:
        for feature in subs["features"]:
            if feature["properties"]["Subbasin"]==index:
                return feature
    
    def convert(self, inputfile: str, outputfile: str, **kvargs):
        if "subnum" in kvargs:
            sub_number = kvargs["subnum"]
        else:
            sub_number = 5

        if "subgeojson" in kvargs:
            subgeojson = kvargs["subgeojson"]
        else:
            subgeojson = "subbasin.json"

        if "ciofile" in kvargs:
            ciofile = kvargs["ciofile"]
        else:
            ciofile = "file.cio"

        f1 = open(inputfile)
        lines = f1.readlines()
        lines = lines[9:]

        desired_list_of_tuple=[(int(line[7:11]),int(line[20:24]),float(line[35:45]),float(line[45:55]),float(line[55:65]),float(line[65:75]),float(line[75:85]),float(line[85:95]),float(line[95:105]),float(line[105:115]),float(line[115:125])) for line in lines]
        #print(lines[0])
        #print(desired_list_of_tuple[0])

        df=pd.DataFrame(data=desired_list_of_tuple,columns=["sub_no","date","PRECIPmm","SNOMELTmm","PETmm","ETmm","SWmm","PERCmm","SURQmm","GW_Qmm","WYLDmm"])

        #print(df.iloc[0:3].to_dict("records"))
        
        swatUtil=Util.SWATUtil()
        startDate=swatUtil.getStartDate(swatiofile=ciofile)
        df["date"]=df["date"].apply(lambda x:timedelta(days=x)+startDate)
        df["date"]=df["date"].apply(lambda x:int(datetime.fromisoformat(x.isoformat()).timestamp()*1000))

        f2=open(subgeojson)
        subs=json.load(f2)
        f2.close()

        sub_discharges=copy.deepcopy(subs)

        sub_discharges["features"]=[]


        records=df.to_dict("records")

        for record in records:
            ft=copy.deepcopy(self.retrieve_feature(record["sub_no"],subs))
            del ft["properties"]
            ft["properties"]=record
            
            sub_discharges["features"].append(ft)

        with open(outputfile, "w") as f:
            json.dump(sub_discharges, f)

