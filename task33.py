from flask import Flask,request,render_template
from pymongo import MongoClient

app = Flask("task33")
client = MongoClient("mongodb://127.0.0.1:27017")

@app.route('/task33')
def task33():
	return render_template("index.html")

@app.route('/mgdata', methods=['POST'])
def mgdata():
	if request.method == 'POST':
		var = request.form.get('x')
		data= [ { "learner_name": var } ]
		client[arth][learner].insert(data)
	return var

app.run(debug=True)
		
		