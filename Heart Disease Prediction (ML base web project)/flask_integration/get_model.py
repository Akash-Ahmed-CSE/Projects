import pickle
import pandas as pd

class LoadModel:
    #Loading the model
    def __init__(self,MODEL_PATH):
        self.loaded_model = pickle.load(open(MODEL_PATH, 'rb'))

    def predict_class(self, male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate,glucose):
        # initialize list of lists 
        data = [[male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate,glucose]]
        
        # Create the pandas DataFrame 
        df = pd.DataFrame(data, columns = ['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds', 'prevalentStroke', 'prevalentHyp', 'diabetes','totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate','glucose'])
        new_pred = self.loaded_model.predict(df)
        return new_pred

#Test LoadMode
if __name__ == '__main__':
    MODEL_PATH = "../models/logistic_reg.sav"
    model = LoadModel(MODEL_PATH)
    predicted_class = model.predict_class(1,39,4,0,0,0,0,0,0,195,106,70,26.97,80,77)
    print(predicted_class)


