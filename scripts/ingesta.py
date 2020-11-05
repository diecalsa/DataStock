#!/usr/bin/python3

import pandas as pd
import sys
import fileinput
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

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

df = pd.DataFrame({'text':text, 'location':location, 'tags':tags}, index = [0])

df.to_csv(sys.stdout, index=False)

#sys.stdout = {'text':text}


