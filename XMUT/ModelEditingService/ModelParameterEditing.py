import subprocess
import os
import shutil
class ModelParameterEditing:
        
    def __init__(self):
        self._properties = {}

    @property
    def parameters(self):
        return self._properties

    @parameters.setter
    def parameters(self, value):
        if not isinstance(value, dict):
            raise ValueError("Input must be a dictionary")
        self._properties = value
        
    def addCalibrationParameter(self,key:str,value:str):
        self.parameters[key]=value
        
    def saveToModelIn(self,path:str):
        f1=open(path+"model.in", 'w')
        for key in self.parameters:
            f1.write(key+" "+self.parameters[key])
            f1.write("\n")
        f1.close()
        
    def invokeModel(self,path:str,bakoutput:str):

        if not os.path.isfile(path+"model.in"):
            print(f"The file "+path+"model.in does not exist.")
            return
        
          
        result=subprocess.run([path+"Swat_Edit.exe"])
        if result.returncode == 0:
            print("Command executed successfully")
            print("Output:", result.stdout)
        else:
            print("Command failed")
            print("Error:", result.stderr)
            
        rs=subprocess.run([path+"swat2009.exe"],cwd=path, capture_output=True, text=True)
        #print(path+"run.bat")
        if rs.returncode == 0:
            print("Command executed successfully")
            print("Output:", rs.stdout)
        else:
            print("Command failed")
            print("Error:", rs.stderr)   
            
        try:
        # Copy the contents of the file to the backup file
            shutil.copy2(path+"output.rch", bakoutput)
            print(f"Backup created successfully: {bakoutput}")
        except Exception as e:
            print(f"An error occurred while creating the backup: {e}")
