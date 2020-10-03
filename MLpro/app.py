import numpy as np
from flask import Flask,request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/submit',methods = ['POST'])
def submit_data():
    return render_template('result.html') 
      

      

if __name__ == '__main__':
    app.run(debug=True)
