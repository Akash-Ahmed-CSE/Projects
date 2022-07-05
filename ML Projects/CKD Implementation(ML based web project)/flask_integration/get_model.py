import pickle
import pandas as pd

class LoadModel:
    #Loading the model
    def __init__(self,MODEL_PATH):
        self.loaded_model = pickle.load(open(MODEL_PATH, 'rb'))

    def predict_class(self, Age,Bp,Sg,Al,Su,Rbc,Pc,Pcc,Ba,Bgr,Bu,Sc,Sod,Pot,Hemo,Pcv,Wbcc,Rbcc,Htn,Dm,Cad,Appet,pe,Ane):
        # initialize list of lists 
        data = [[Age,Bp,Sg,Al,Su,Rbc,Pc,Pcc,Ba,Bgr,Bu,Sc,Sod,Pot,Hemo,Pcv,Wbcc,Rbcc,Htn,Dm,Cad,Appet,pe,Ane]]
        
        # Create the pandas DataFrame 
        df = pd.DataFrame(data, columns = ['Age', 'Bp', 'Sg', 'Al', 'Su', 'Rbc', 'Pc', 'Pcc', 'Ba','Bgr', 'Bu', 'Sc', 'Sod', 'Pot', 'Hemo', 'Pcv', 'Wbcc', 'Rbcc', 'Htn', 'Dm', 'Cad', 'Appet', 'pe', 'Ane'])
        new_pred = self.loaded_model.predict(df)
        return new_pred
#48,50,1.02,4,0,1,1,0,0,121,18,1.2,137.53,4.63,11.3,44,6000,4.71,1,1,0,1,0,0 -> for 1
#82,60,1.025,0,0,1,1,0,0,137,17,0.4,147,4.7,14.3,34,6700,5.9,0,1,0,1,0,0 -> for 0

#Test LoadMode
if __name__ == '__main__':
    MODEL_PATH = "../models/XGBClassifier.sav"
    model = LoadModel(MODEL_PATH)
    predicted_class = model.predict_class(48,50,1.02,4,0,1,1,0,0,121,18,1.2,137.53,4.63,11.3,44,6000,4.71,1,1,0,1,0,0)
    print(predicted_class)


