import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bath, balcony, bhk):
	try:
		loc_index = __data_columns.index(location.lower())
	except:
		loc_index = -1

	x = np.zeros(len(__data_columns))

	x[0] = sqft
	x[1] = bath
	x[2] = balcony
	x[3] = bhk

	if loc_index >=0:
		x[loc_index] = 1

	return round(__model.predict([x])[0], 2)


def get_location_names():
	load_saved_data()
	return __locations


def load_saved_data():
	print("Loading saved data.........START\n")
	global __data_columns
	global __locations
	global __model

	with open("./data/columns.json", 'r') as f:
		__data_columns = json.load(f)['data_columns']
		__locations = __data_columns[4:]

	with open("./data/Bangalore_House_Prices_Model.pickle", 'rb') as f:
		__model = pickle.load(f)

	
	print("Loading saved data.........DONE\n")


if __name__ == '__main__':
	
	print(get_location_names())
	print(get_estimated_price('1st Phase JP Nagar',1000, 3, 2, 3))
	print(get_estimated_price('1st Phase JP Nagar',1000, 2, 2, 2))
	print(get_estimated_price('Kalhalli',1000, 3, 2, 3))
	print(get_estimated_price('Ejipura',1000, 2, 2, 2))