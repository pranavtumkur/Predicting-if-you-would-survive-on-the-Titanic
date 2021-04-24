import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    if final_features[0][6]==1:
        final_features[0][6]=1
        final_features=[np.array(np.append(final_features[0],0))]
    elif final_features[0][6]==2:
        final_features[0][6]=0
        final_features=[np.array(np.append(final_features[0],1))]
    else:
        final_features[0][6]=0
        final_features=[np.array(np.append(final_features[0],0))]
    print(final_features)
    
    prediction = model.predict(final_features)
    if prediction==0:
        output="You are dead!"
    else:
        output="You will survive!"

    return render_template('index.html', prediction_text='If you were on the Titanic- {}'.format(output))


if __name__ == "__main__":
    app.run(debug=False)
