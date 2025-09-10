from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

# import the pickle files
model = pickle.load(open('models/ridge.pkl','rb'))
scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route("/predict", methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        temp = float(request.form.get('temperature'))
        rh = float(request.form.get('rh'))
        ws = float(request.form.get('ws'))
        rain = float(request.form.get('rain'))
        ffmc = float(request.form.get('ffmc'))
        dmc = float(request.form.get('dmc'))
        isi = float(request.form.get('isi'))
        cls_val = request.form.get('classes')
        if cls_val=='fire':
            classes = 1
        else:
            classes = 0
        reg_val = request.form.get('region')
        if reg_val=='north':
            region = 1
        elif reg_val=='south':
            region = 2
        elif reg_val=='east':
            region = 3
        elif reg_val=='west':
            region = 4
        else:
            region = 0

        new_X = scaler.transform([[temp,rh,ws,rain,ffmc,dmc,isi,classes,region]])
        res = model.predict(new_X)

        return render_template('home.html', result=res)

    else:
        return render_template('home.html')


@app.route("/")
def welcome():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)