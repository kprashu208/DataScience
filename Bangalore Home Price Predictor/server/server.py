from flask import Flask, request, jsonify
import util


app = Flask(__name__)

@app.route('/')
def index():
	return "Open app.html on the 'client/app.html' path."

@app.route('/get_location_names')
def get_location_names():
	response = jsonify({
		'locations' : util.get_location_names()
		})

	response.headers.add('Access-Control-Allow-Origin', '*')

	return response



@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
	total_sqft = float(str(request.form["total_sqft"]))
	location = str(request.form['location'])
	bath = int(request.form['bath'])
	balcony = int(str(request.form['balcony']))
	bhk = int(str(request.form['bhk']))
	
	response = jsonify({
		'estimated_price' : util.get_estimated_price(location, total_sqft, bath, balcony, bhk)
		})

	response.headers.add('Access-Control-Allow-Origin', '*')

	return response


if __name__ == '__main__':
	app.run(debug=True)
