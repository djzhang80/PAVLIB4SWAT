import math
from datetime import datetime, date, timedelta
class SWATUtil:
    def getModelParameter(self,prameter:str,parameterfile:str)->int|str|float|None:
        with open(parameterfile,"r") as f:
            for line in f.readlines():
                if(line.find(prameter)!=-1):
                   return line.partition("|")[0].strip()
               
    def getStartDate(self, swatiofile: str) -> date:
        skip_year = int(self.getModelParameter("NYSKIP", swatiofile))
        sim_year = int(self.getModelParameter("NBYR", swatiofile))
        start_year = int(self.getModelParameter("IYR", swatiofile))
        start_day = int(self.getModelParameter("IDAF", swatiofile))
        end_day = int(self.getModelParameter("IDAL", swatiofile))
        day = date(start_year+skip_year, 1, 1)+timedelta(days=start_day-1)
        return day

    def getDays(self, swatiofile: str) -> int:
        skip_year = int(self.getModelParameter("NYSKIP", swatiofile))
        sim_year = int(self.getModelParameter("NBYR", swatiofile))
        start_year = int(self.getModelParameter("IYR", swatiofile))
        start_day = int(self.getModelParameter("IDAF", swatiofile))
        end_day = int(self.getModelParameter("IDAL", swatiofile))
        day = date(start_year+skip_year, 1, 1)+timedelta(days=start_day-1)
        endday = date(start_year+sim_year-1, 1, 1)+timedelta(days=end_day)
        return (endday-day).days
    
    def jdtodatestd (self,jdate):
        fmt = '%Y%j'
        datestd = datetime.strptime(jdate, fmt).date()
        return(datestd)