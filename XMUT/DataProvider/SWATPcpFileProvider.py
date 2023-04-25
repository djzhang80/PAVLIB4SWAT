from .DataProviderInterface import ProviderInterface
from datetime import datetime
from . import Util
import pandas as pd

class PCPProvider(ProviderInterface):
    def get_token(self,index:int,line:str)->str:
        return line.split()[index]
    

    def convert(self, inputfile: str, outputfile: str, **kvargs):    
        f1=open(inputfile)
        lines=f1.readlines()
        lines_of_points=lines[1:4]
        charactor_count=len(lines_of_points[0])
        pcp_points=[]
        swatUtil=Util.SWATUtil()
        for line in lines[4:]:
            date=swatUtil.jdtodatestd(line[0:7])
            i=7
            while i+5<charactor_count:
                latitude=float(lines_of_points[0][i:i+5])
                longitude=float(lines_of_points[1][i:i+5])
                elevation=float(lines_of_points[2][i:i+5])
                value=float(line[i:i+5])
                pcp_points.append([latitude,longitude,elevation,int(datetime.fromisoformat(date.isoformat()).timestamp()*1000),value])
                i=i+5
        #print(len(pcp_points))

        pcp_data=pd.DataFrame(data=pcp_points,columns=["lat","lon","ele","date1","value"])
        pcp_data.to_csv(outputfile)



