from .DataProviderInterface import ProviderInterface
from datetime import datetime, date, timedelta
from . import Util
import pandas as pd
import json
import copy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

class RCHScenarioProvider(ProviderInterface):
    def get_token(self,index:int,line:str)->str:
        return line.split()[index]
    

    def convert(self, inputfile: str, outputfile: str, **kvargs):    
        if "subnum" in kvargs:
            sub_number=kvargs["subnum"]
        else:
            sub_number=5
        
        if "outlets" in kvargs:
            outlets=kvargs["outlets"]
        else:
            outlets="outlets.json"
            
        if "ciofile" in kvargs:
            ciofile=kvargs["ciofile"]
        else:
            ciofile="file.cio"
            
        if "inputfile2" in kvargs:
            inputfile2=kvargs["inputfile2"]
        else:
            inputfile2=inputfile
            
        if "label1" in kvargs:
            label1=kvargs["label1"]
        else:
            label1="scenario1"
            
        if "label2" in kvargs:
            label2=kvargs["label2"]
        else:
            label2="scenario2"          
            
        
        #read scenario one
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
        f1.close()
        
        #read scenario two
        f1=open(inputfile2)
        lines=f1.readlines()
        lines=lines[9:]

        desired_list_of_tuple=[(int(self.get_token(1,line)),float(self.get_token(5,line))) for line in lines]
        df2=pd.DataFrame(data=desired_list_of_tuple,columns=["rch_no","discharge"])
        df2.reset_index(inplace=True)
        df2.rename(columns={"index":"date"},inplace=True)
        startDate=swatUtil.getStartDate(swatiofile=ciofile)
        df2["date"]=df2["date"].apply(lambda x:timedelta(days=divmod(x,sub_number)[0])+startDate)
        f1.close()
        
        
        merged_df = pd.merge(df, df2, on=('date','rch_no'))
        date_format = "%m%d"
        
        for rch in range(1,sub_number+1):
            #print(rch)
            fig=plt.figure()
            plt.figure(figsize=(3,2))
            plt.subplots_adjust(left=0.15, bottom=0.3, right=0.95, top=0.95)
            plt.plot(merged_df.loc[df['rch_no']==rch]['date'], merged_df.loc[df['rch_no']==rch]['discharge_x'], label=label1)
            plt.plot(merged_df.loc[df['rch_no']==rch]['date'], merged_df.loc[df['rch_no']==rch]['discharge_y'], label=label2)

        # Add labels and title

            plt.xlabel('Date')
            plt.ylabel('Discharge (cms)')
            #plt.title('Line Plot with Two DataFrames')
            plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=20))  # Adjust the interval as needed
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(date_format))
            plt.xticks(rotation=20)
            # Rotate the date labels for better readability (optional)
            #plt.gcf().autofmt_xdate()
            plt.legend(fontsize='8')  # Show legend
            plt.savefig("./plot_rch_"+str(rch)+".jpg")
            plt.close()
        
        f=open(outlets)
        data=json.load(f)
        features_collection=copy.deepcopy(data)
        features_collection["features"]=[]
        for feature in data["features"]:
                #del feature["properties"]
                item=copy.deepcopy(feature)
                rch=feature["properties"]["Subbasin"]
                item["properties"]["<img>scenario"]="./plot_rch_"+str(rch)+".jpg"
                features_collection["features"].append(item)
                
        f.close()
        
        with open(outputfile,"w") as f:
            json.dump(features_collection,f) 
        
        
        
        
        




