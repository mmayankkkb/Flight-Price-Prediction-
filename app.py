from flask import Flask,request,jsonify,url_for,render_template
import pickle
import numpy as np
from data_preprocess import process 
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route(rule='/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature_inp=[i for i in request.form.values()]
    
    final_feature=[process(feature_inp)]
    prediction=model.predict(final_feature)
    output=round(prediction[0],2)

    return render_template('index.html',Prediction_text='Flight Price Should be Rs :{}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
