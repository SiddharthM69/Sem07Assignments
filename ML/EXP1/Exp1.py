# Select appropriate dataset and perform following data preprocessing steps: 
# Imputation 
# Anomaly detection 
# Standardization 
# Normalization 
# Encoding 
import pandas as pd

class Preprocessing:
    def __init__(self,path) -> None:
        self.file=pd.read_csv(path)
        self.util=Utilities()
    
    def Imputation(self):
        FuelBeforeImpute=self.file['FuelEconomy']
        toFill=[el for el in FuelBeforeImpute.isnull()]
        fuelSum=0
        fuelCount=0
        for i in range(0,len(toFill)):
            if(toFill[i]==False and self.util.isfloat(FuelBeforeImpute[i])):
                fuelSum+=float(FuelBeforeImpute[i])
                fuelCount+=1
        avgFuelEco=fuelSum/fuelCount
        avgFuelEco=round(avgFuelEco,2)
        for i in range(0,len(toFill)):
            if(toFill[i]==True or not self.util.isfloat(FuelBeforeImpute[i])):
                self.file['FuelEconomy'][i]=avgFuelEco
        print(self.file)
        self.file.to_csv('travel-time-after-impute.csv')
    
    def AnomalyDetection():
        pass
    def Normalization():
        pass
    def Encoding():
        pass


class Utilities:
    def isfloat(a,num):
        try:
            float(num)
            return True
        except ValueError:
            return False


#---------------------------------Execution Space--------------------------------------------------------------
obj=Preprocessing('./travel-times.csv')
obj.Imputation()


    