from flask import Flask,request,jsonify,url_for,render_template
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route(rule='/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    feature_inp=[int(i) for i in request.form.values()]
    final_feature=[np.array(feature_inp)]
    prediction=model.predict(final_feature)
    output=round(prediction[0],2)

    return render_template('index.html',Prediction_text='Flight Price Should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
