from flask import Flask, render_template, flash, request
from get_model import *

#initializing the model
MODEL_PATH = "../models/XGBClassifier.sav"
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
    Age = request.form['Age']
    Bp = request.form['Bp']
    Sg = request.form['Sg']
    Al = request.form['Al']
    Su = request.form['Su']
    Rbc = request.form['Rbc']
    Pc = request.form['Pc']
    Pcc = request.form['Pcc']
    Ba = request.form['Ba']
    Bgr = request.form['Bgr']
    Bu = request.form['Bu']
    Sc = request.form['Sc']
    Sod = request.form['Sod']
    Pot = request.form['Pot']
    Hemo = request.form['Hemo']
    Pcv = request.form['Pcv']
    Wbcc = request.form['Wbcc']
    Rbcc = request.form['Rbcc']
    Htn = request.form['Htn']
    Dm = request.form['Dm']
    Cad = request.form['Cad']
    Appet = request.form['Appet']
    pe = request.form['pe']
    Ane = request.form['Ane']


    #Pcc = request.form['ZZZZZZZZZZZZZZZZZZ']

    #Predict on the given parameters
    prediction = model.predict_class(Age,Bp,Sg,Al,Su,Rbc,Pc,Pcc,Ba,Bgr,Bu,Sc,Sod,Pot,Hemo,Pcv,Wbcc,Rbcc,Htn,Dm,Cad,Appet,pe,Ane)
    print(prediction)
    #Route for result
    if int(prediction[0]) == 1:
        return render_template("positive.html", result="true")
    elif int(prediction[0]) == 0:
        return render_template("negetive.html", result="true")
        
if __name__ == "__main__":
    app.run()