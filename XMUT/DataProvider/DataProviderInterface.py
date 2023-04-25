import abc

class ProviderInterface(abc.ABC):
    
    @abc.abstractclassmethod
    def convert(self,inputfile:str,outputfile:str,**kvargs):
        pass
    
