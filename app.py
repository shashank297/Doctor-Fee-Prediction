from flask import Flask,render_template,request
import pickle
import numpy as np

modal=pickle.load(open('pipe.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/predict',methods=['post'])

def predict_fee():
   DP_Score= int(request.form.get('DP Score'))
   NPV_Value=int(request.form.get('NPV Value'))
   City=request.form.get('City')
   Years_of_Experience=int(request.form.get('Years of Experience'))
   Speciality=request.form.get('Speciality')
   Degree_no=int(request.form.get('Degree_no'))
   Degree_1=request.form.get('Degree_1')

   result=round(modal.predict(np.array([DP_Score,NPV_Value,City,Years_of_Experience,Speciality,Degree_no,Degree_1]).reshape(1,7))[0])

   return render_template('index.html',result=result)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)