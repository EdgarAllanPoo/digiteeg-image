import numpy as np
import pickle

if __name__ == '__main__':

	with open('data/digit/data.pkl', 'rb') as file:
		data = pickle.load(file, encoding='latin1')
		train_X = data['x_train']
		train_Y = data['y_train']
		test_X = data['x_test']
		test_Y = data['y_test']
		
	print(train_X.shape)