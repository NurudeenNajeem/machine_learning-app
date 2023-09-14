from flask import Flask,render_template,request
import numpy as np
import pickle
from datetime import datetime,time

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[50]]))



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['GET','POST'])
def predict():
    try :
        curent_day = datetime.today().strftime('%A')
       

        int_features = [float(x) for x in request.form.values()]
        features =[np.array(int_features)]
        prediction = model.predict(features)
        output = round(prediction[0], 2)
        print(output)
        return render_template('index.html', prediction =f'Total revenue generated is ${output}')
    except:
        return render_template('index.html', prediction ='Try to input numbers')

if (__name__)=='__main__' :
    app.run(debug=True)