import XMUT
import json
import warnings
from datetime import date,timedelta
import pandas as pd
import numpy as np
warnings.filterwarnings("ignore")
import jsonpath_ng
from jsonpath_ng import parse

def test2():
    longtitude=117.75061633921499
    latitude=24.880945705136686
    cofiguration=XMUT.MapConfiguration.Configuration()
    config=cofiguration.getConfig(latitude,longtitude)

    keplerMap=XMUT.MapGenerator.KeplerMap();
    f=open(r"./data/kepler_data/subbasin.json","r")
    data=json.load(f)
    f.close()
    keplerMap.addLayerInNoteBook(data,"subbasin",config)

def test1():
    sfp=XMUT.DataProvider.ShapeProvider()
    filelist=["rivers","outlets","raingauge","subbasin","tempgauge"]
    for filename in filelist:
        sfp.convert(r"./data/shpfile/"+filename+".shp","",r"./data/kepler_data/"+filename+".json","epsg:4326")
    
    
def test3():
    import json
    import XMUT

    longtitude=118.01177670289091
    latitude=25.440411737132468
    zoom=10.76383577825254
    configuration=XMUT.MapConfiguration.Configuration()
    sfp=XMUT.DataProvider.ShapeProvider()
    center=sfp.getCenter(r"./data/shpfile/subbasin.shp","","epsg:4326")
    center.append(zoom)
    config=configuration.getConfig(*center)
    
    

    keplerMap=XMUT.MapGenerator.KeplerMap();

    filelist=["rivers","outlets","raingauge","subbasin","tempgauge"]
    for filename in filelist:   
        f=open(r"./data/kepler_data/"+filename+".json","r")
        data=json.load(f)
        f.close()
        keplerMap.addLayerInNoteBook(data,filename,config)
        
    keplerMap.map.save_to_html(file_name=r"./data/kepler_map/map034.html")
    

#test3()

def test4():
    myswatutil=XMUT.DataProvider.Util.SWATUtil()
    
    result=myswatutil.getModelParameter("IPRINT",r"./data/model/file.cio")
    print(result)
    
#test4();


def test5():
    rp=XMUT.DataProvider.SWATRchFileProvider.RCHProvider()
    print(rp.getStartDate(r"./data/model/file.cio"))
    print(rp.getDays(r"./data/model/file.cio"))




def test6():
    sfp=XMUT.DataProvider.ShapeProvider()
    filelist=["rivers","outlets","raingauge","subbasin","tempgauge"]
    for filename in filelist:
        sfp.convert(r"./data/shpfile/"+filename+r".shp",r"./data/kepler_data/"+filename+".json",outputproject="epsg:4326")


def test7():
    rp=XMUT.DataProvider.SWATRchFileProvider.RCHProvider()
    rp.convert(r"./data/model/output.rch",r"./data/kepler_data/discharge.json",subnum=5,rivergeojson=r"./data/kepler_data/rivers.json",ciofile=r"./data/model/file.cio")


def test72():
    rp=XMUT.DataProvider.SWATRchFileProvider.RCHProvider()
    rp.convert(r"./data/model/output.rch",r"./data/kepler_data/discharge_pb.json",subnum=5,rivergeojson=r"./data/kepler_data/rivers.json",ciofile=r"./data/model/file.cio")
    zoom = 10.76383577825254
    configuration = XMUT.MapConfiguration.Configuration()
    sfp = XMUT.DataProvider.ShapeProvider()
    center = sfp.getCenter(r"./data/shpfile/subbasin.shp", "", "epsg:4326")
    center.append(zoom)
    config = configuration.getConfig(*center)

    keplerMap = XMUT.MapGenerator.KeplerMap()

    filelist = ["discharge_pb", "rivers", "subbasin"]
    for filename in filelist:
        f = open(r"./data/kepler_data/"+filename+".json", "r")
        data = json.load(f)
        f.close()
        keplerMap.addLayerInNoteBook(data, filename, config)
    keplerMap.map.save_to_html(file_name=r"./data/kepler_map/map_discharge_pd.html")

def pindex(arrLike):
    print(arrLike)

def test8():
    df=pd.DataFrame([[1,2],[4,5],[7,8]],columns=["col1","col2"])
    df.reset_index(inplace=True)
# rename
    df = df.rename(columns = {'index':'new_name'})
    print(df)


def test9():
    import json
    import XMUT

    zoom=10.76383577825254
    configuration=XMUT.MapConfiguration.Configuration()
    sfp=XMUT.DataProvider.ShapeProvider()
    center=sfp.getCenter(r"./data/shpfile/subbasin.shp","","epsg:4326")
    center.append(zoom)
    config=configuration.getConfig(*center)
    
    

    keplerMap=XMUT.MapGenerator.KeplerMap();

    filelist=["discharge","rivers","subbasin"]
    for filename in filelist:   
        f=open(r"./data/kepler_data/"+filename+".json","r")
        data=json.load(f)
        f.close()
        keplerMap.addLayerInNoteBook(data,filename,config)
    
   
    keplerMap.map.save_to_html(file_name=r"./data/kepler_map/map035.html")
    
    print(jsonpath_ng.parse('config.visState.layer[*].config.dataID').find())



def test10():
    rp=XMUT.DataProvider.SWATSubFileProvider.SUBProvider()
    rp.convert(r"./data/model/output.sub",r"./data/kepler_data/runoff_sub.json",subnum=5,subgeojson=r"./data/kepler_data/subbasin.json",ciofile=r"./data/model/file.cio")
    zoom = 10.76383577825254
    configuration = XMUT.MapConfiguration.Configuration()
    sfp = XMUT.DataProvider.ShapeProvider()
    center = sfp.getCenter(r"./data/shpfile/subbasin.shp", "", "epsg:4326")
    center.append(zoom)
    config = configuration.getConfig(*center)

    keplerMap = XMUT.MapGenerator.KeplerMap()

    filelist = ["runoff_sub", "rivers", "subbasin"]
    for filename in filelist:
        f = open(r"./data/kepler_data/"+filename+".json", "r")
        data = json.load(f)
        f.close()
        keplerMap.addLayerInNoteBook(data, filename, config)
    keplerMap.map.save_to_html(file_name=r"./data/kepler_map/map_sub_runoff.html")

#test72()

def test11():
    ciofile=r"./data/model/file.cio"
    swatUtil=XMUT.DataProvider.Util.SWATUtil()
    startDate=swatUtil.getStartDate(swatiofile=ciofile)
    configuration = XMUT.MapConfiguration.Configuration()
    print(configuration.getTSRivers("zdj",startDate))
    
#test11()


def test12():
    import json
    import XMUT
    import warnings
    warnings.filterwarnings("ignore")
    sfp=XMUT.DataProvider.ShapeProvider()
    lon_lat=sfp.getCenter("./data/shpfile/subbasins.shp","",outputproject="epsg:4326")
    zoom=10.76
    configuration=XMUT.MapConfiguration.Configuration()
    config=configuration.getBaseConfig(*lon_lat,zoom)
    keplerMap=XMUT.MapGenerator.KeplerMap()
    f=open(r"./data/kepler_data/ts_subbasins.json","r")
    data=json.load(f)
    f.close()
    
    f=open(r"./data/kepler_data/ts_rivers.json","r")
    data2=json.load(f)
    f.close()
    
    #f=open(r"./data/kepler_data/ts_raingauges.csv","r")
    data3=pd.read_csv(r"./data/kepler_data/ts_raingauges.csv")
    #f.close()
    
    ciofile=r"./data/model/file.cio"
    swatUtil=XMUT.DataProvider.Util.SWATUtil()
    startDate=swatUtil.getStartDate(swatiofile=ciofile)
    config=configuration.getConfigByType(type="ts_rivers",dataid="ts_rivers_id",startdate=startDate)
    
    keplerMap.addLayerInNoteBook(data,"ts_subbasins_id",config)   
    keplerMap.addLayerInNoteBook(data2,"ts_rivers_id",config)      
    keplerMap.addLayerInNoteBook(data3,"ts_raingauges_id",config)     
    keplerMap.map.save_to_html(file_name="./data/kepler_map/ts_all.html")
    
#test12()

def test13():
    ciofile=r"./data/model/file.cio"
    swatUtil=XMUT.DataProvider.Util.SWATUtil()
    startDate=swatUtil.getStartDate(swatiofile=ciofile)
    configuration = XMUT.MapConfiguration.Configuration()
    conf1=configuration.getConfigByType(type="ts_rivers",dataid="ts_rivers_id",startdate=startDate)
    conf2=configuration.getConfigByType(type="ts_subbasins",dataid="ts_subbasins_id",startdate=startDate)
    
    keplerMap=XMUT.MapGenerator.KeplerMap()
    f=open(r"./data/kepler_data/ts_subbasins.json","r")
    data=json.load(f)
    f.close()
    
    f=open(r"./data/kepler_data/ts_rivers.json","r")
    data2=json.load(f)
    f.close()
    
    rs=configuration.mergeConfig(src=conf1,dest=conf2)
    keplerMap.addLayer(data2,"ts_rivers_id")  
    keplerMap.addLayer(data,"ts_subbasins_id")  
    print(rs)
    keplerMap.setConfigure(rs)
    #keplerMap.addLayerInNoteBook(data,"ts_subbasins_id",conf2)   
 
    
    keplerMap.map.save_to_html(file_name="./data/kepler_map/ts_two2.html")


#test13()

def test14():
    ciofile=r"./data/model/file.cio"
    swatUtil=XMUT.DataProvider.Util.SWATUtil()
    startDate=swatUtil.getStartDate(swatiofile=ciofile)
    configuration = XMUT.MapConfiguration.Configuration()
    conf1=configuration.getConfigByType(type="ts_rivers",dataid="ts_rivers_id",startdate=startDate)
    conf2=configuration.getConfigByType(type="ts_subbasins",dataid="ts_subbasins_id",startdate=startDate)
    
    keplerMap=XMUT.MapGenerator.KeplerMap()
    f=open(r"./data/kepler_data/raingauges.json","r")
    data=json.load(f)
    f.close()
    

    data2=pd.read_csv(r"./data/kepler_data/ts_raingauges.csv")

    
    rs=configuration.mergeConfig(src=conf1,dest=conf2)
    keplerMap.addLayer(data,"raingauges_id")  
    keplerMap.addLayer(data2,"ts_raingauges_id")  
    print(rs)
    #keplerMap.setConfigure(rs)
    #keplerMap.addLayerInNoteBook(data,"ts_subbasins_id",conf2)   
 
    
    keplerMap.map.save_to_html(file_name="./raingauges-ts.html")


test14()




