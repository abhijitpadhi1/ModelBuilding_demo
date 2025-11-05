from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__, static_folder='public', static_url_path='')
app = application

# import the pickle files
model = pickle.load(open('models/ridge.pkl','rb'))
scaler = pickle.load(open('models/scaler.pkl','rb'))

@app.route("/predict", methods=['POST'])
def predict():
    data = request.json
    temp = float(data.get('temperature'))
    rh = float(data.get('rh'))
    ws = float(data.get('ws'))
    rain = float(data.get('rain'))
    ffmc = float(data.get('ffmc'))
    dmc = float(data.get('dmc'))
    isi = float(data.get('isi'))
    cls_val = data.get('classes')
    if cls_val=='fire':
        classes = 1
    else:
        classes = 0
    reg_val = data.get('region')
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

    return jsonify({'prediction': res[0]})


@app.route("/")
def welcome():
    return render_template('home.html')

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
