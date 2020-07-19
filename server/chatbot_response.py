# things we need for NLP
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from underthesea import word_tokenize
from fuzzywuzzy import fuzz
# things we need for Tensorflow
import numpy as np
import tensorflow as tf
import keras
from tensorflow import keras
from tensorflow.keras import layers
import numpy
import random
import pickle
import json

classes = pickle.load( open( "pkl/classes.pkl", "rb" ) )

with open('data/intents.json', 'r', encoding='utf-8') as json_data:
	intents = json.load(json_data)

# with open('data/dishes_data.json', 'r', encoding='utf-8') as json_data:
#     database = json.load(json_data)

model = tf.keras.models.load_model('pkl/model.h5')
# model.summary()

vectorizer = pickle.load(open("pkl/tfidf_vectorizer.pkl", "rb"))

def classify(sentence):
	sentence = word_tokenize(sentence, format="text")
	results = model.predict(vectorizer.transform([sentence]).toarray())[0]
	results = numpy.array(results)
	idx = numpy.argsort(-results)[0]
	return classes[idx], results[idx]

context = {}
# def get_drink(sentence):
#     drinks = []
#     for values in database.values():
#         for value in values:
#             drinks.append(value['name'])

#     results = []
#     for drink in drinks:
#         ratio = fuzz.ratio(sentence.lower(), drink.lower())
#         if ratio > 50:
#             results.append((drink, ratio))
#     return results

# print(get_drink("trà sữa"))

def response(tag):
	for i in intents['intents']:
		if i['tag'] == tag:
			return random.choice(i['responses'])

if __name__ == '__main__':
	print('Begin chatting: ')
	while True:
		print('Human: ', end=''),
		x = input()
		tag, _ = classify(x)
		print('Bot: ', response(tag))

		# tag, conf = classify(x)
		# print('Bot: ', tag, conf)
