from flask import Flask,render_template,request
import numpy as np
from joblib import load,dump

model = load('Healthcare.joblib')

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def new():
    return render_template('new.html')

@app.route('/predict', methods=['POST','GET'] )
def predict():
    data1=float(request.form['a'])
    data2=float(request.form['b'])
    data3=float(request.form['c'])
    data4=float(request.form['d'])
    data5=float(request.form['e'])
    data6=float(request.form['f'])
    data7=float(request.form['g'])
    data8=float(request.form['h'])
    data9=float(request.form['i'])
    data10=float(request.form['j'])
    features=np.array([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10])
    pred = model.predict([features])