from .DataProviderInterface import ProviderInterface
import shapefile
from pyproj import Proj, transform,CRS
import json

class ShapeProvider(ProviderInterface):
    
    def convert(self,inputfile:str,outputfile:str,**kvargs):
        """This method convert from shp to geojson"""
        shpf = shapefile.Reader(inputfile)
        outputproject=kvargs["outputproject"]
        
        if "inputproject" in kvargs:
            inputproject=kvargs["inputproject"]
        else:
            inputproject=None
            
        if inputproject is None or inputproject.isspace() or len(inputproject)==0:
            with open(inputfile.replace(".shp",".prj")) as f:
                wkt=f.read()
                input_projection = CRS.from_wkt(wkt)  
        else:
            input_projection = Proj(init=inputproject)

        output_projection = Proj(init=outputproject)

        geojson=shpf.__geo_interface__
        for j in range(0,len(geojson["features"])):
            if(isinstance(geojson["features"][j]["geometry"]["coordinates"],tuple)):
                geojson["features"][j]["geometry"]["coordinates"]=self.convertProjection(geojson["features"][j]["geometry"]["coordinates"],input_projection, output_projection)
            else:
                self.convertProjection(geojson["features"][j]["geometry"]["coordinates"],input_projection, output_projection)   

        for i in range(0,len(geojson["bbox"]),2):
            x, y = geojson["bbox"][i], geojson["bbox"][i+1]
            # tranform the coord
            new_x, new_y = transform(input_projection, output_projection, x, y)
            geojson["bbox"][i]=new_x
            geojson["bbox"][i+1]=new_y

        with open(outputfile, "w") as f2:
            json.dump(geojson,f2)
    
    def getBoundary(self,inputfile:str,inputproject:str,outputproject:str):
        shpf = shapefile.Reader(inputfile)
        if inputproject is None or inputproject.isspace() or len(inputproject)==0:
            with open(inputfile.replace(".shp",".prj")) as f:
                wkt=f.read()
                input_projection = CRS.from_wkt(wkt)  
        else:
            input_projection = Proj(init=inputproject)
        output_projection = Proj(init=outputproject)
        geojson=shpf.__geo_interface__
        output_boundary=[]
        for i in range(0,len(geojson["bbox"]),2):
            x, y = geojson["bbox"][i], geojson["bbox"][i+1]
            # tranform the coord
            new_x, new_y = transform(input_projection, output_projection, x, y)
            output_boundary.append(new_x)
            output_boundary.append(new_y)
        return output_boundary
        
    def getCenter(self,inputfile:str,inputproject:str,outputproject:str):
        boundary=self.getBoundary(inputfile,inputproject,outputproject)
        return [(boundary[0]+boundary[2])/2,(boundary[1]+boundary[3])/2]
    
    def convertProjection(self,coords,input_projection, output_projection):
        if(isinstance(coords,list)|isinstance(coords,tuple)):
            if(isinstance(coords[0],list)):
                for i in range(0,len(coords)):
                        child=coords[i]
                        self.convertProjection(child,input_projection, output_projection) 
            elif(isinstance(coords[0],tuple)):
                for i in range(0,len(coords)):
                        child=coords[i]
                        coords[i]=self.convertProjection(child,input_projection, output_projection) 
            else:
                x, y = coords[0], coords[1]
                # tranform the coord
                new_x, new_y = transform(input_projection, output_projection, x, y)
                if(isinstance(coords,list)):
                    coords=[new_x, new_y]
                elif(isinstance(coords,tuple)):
                    coords=new_x,new_y
                return coords

