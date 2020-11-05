#!/usr/bin/python3

import pandas as pd
import sys
import fileinput
import random
from ludwig.api import LudwigModel
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

model_dir = '/home/diego/ELK/Files/results/experiment_run/model'

text = ''
tags = ''
output = {}
lats = [39.46975, 52.52437, 51.5085]
longs = [-0.37739, 13.41053, -0.12574]

n = random.randint(0,2)

lon = longs[n]
lat = lats[n]

location = "{},{}".format(lat,lon)

for line in fileinput.input():
	text = text + ' ' + line.rstrip()

tokens = word_tokenize(text.lower())
words = [word for word in tokens if word.isalpha()]
words = [word for word in words if word not in stopwords.words('english')]

for word in words:
	tags = tags + ' ' + word

ludwig_model = LudwigModel.load(model_dir)

df = pd.DataFrame({'text':text, 'location':location, 'tags':tags}, index = [0])

prediction = ludwig_model.predict(data_df = df)

df['class'] = prediction['class_predictions']

df.to_csv(sys.stdout, index = False)


