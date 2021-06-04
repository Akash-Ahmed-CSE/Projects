from flask import Flask, render_template, flash, request
from get_model import *

#initializing the model
MODEL_PATH = "../models/logistic_reg1.sav"
model = LoadModel(MODEL_PATH)


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

#Define home route
@app.route("/")
def index():
    return render_template("index.html")

#Define diagnosis route
@app.route("/diagnosis", methods=['POST'])
def diagnosis():

############################################################
    male = request.form['male']
    age = request.form['age']
    education = request.form['education']
    currentSmoker = request.form['currentSmoker']
    cigsPerDay = request.form['cigsPerDay']
    BPMeds = request.form['BPMeds']
    prevalentStroke = request.form['prevalentStroke']
    prevalentHyp = request.form['prevalentHyp']
    diabetes = request.form['diabetes']
    totChol = request.form['totChol']
    sysBP = request.form['sysBP']
    diaBP = request.form['diaBP']
    BMI = request.form['BMI']
    heartRate = request.form['heartRate']
    glucose = request.form['glucose']


#############################################################

    #Pcc = request.form['ZZZZZZZZZZZZZZZZZZ']

    #Predict on the given parameters
    prediction = model.predict_class(male, age, education, currentSmoker, cigsPerDay, BPMeds, prevalentStroke, prevalentHyp, diabetes, totChol, sysBP, diaBP, BMI, heartRate,glucose)
    print(prediction)
    #Route for result
    if int(prediction[0]) == 1:
        return render_template("positive.html", result="true")
    elif int(prediction[0]) == 0:
        return render_template("negetive.html", result="true")
        
if __name__ == "__main__":
    app.run()