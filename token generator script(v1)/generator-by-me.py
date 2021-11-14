from pprint import pprint
import random
import requests
import urllib.request, random
import urllib.request
import string
import os
from datetime import date
import datetime
import base64

N = input("How many tokens loop?: ")
count = 0
while(int(count)<int(N)):
	randomlist = []
	for i in range(1):
		n = random.randint(100000000000000000,999999999999999999)
		o = str(n)
		sort_ = base64.b64encode(o.encode('utf-8'))
		sort__ = str(sort_,'utf-8')
		randomlist.append(sort__)
		
	with open("milieux.txt", "r", encoding='utf-8') as milieux: 
		allText = milieux.read() 
		m_words = list(map(str, allText.split()))	
	
	fing = str(random.choice(m_words))
	fing_ = base64.b64encode(fing.encode('utf-16'))
	fing__ = str(fing_,'utf-8')
	fing_sort = fing__.replace("/", "").replace("=", "")
 

	with open("mots.txt", "r", encoding='utf-8') as mots: 
		allText = mots.read() 
		words = list(map(str, allText.split()))	
		
	mot = str(random.choice(words))
	mot_ = base64.b64encode(mot.encode('utf-16'))
	mot__ = str(mot_,'utf-8')
	mot_sort = mot__.replace("/", "").replace("=", "")

	
	with open('Generated Tokens.txt','r') as fr:
		copy = fr.read()
	p = copy.find('\r\n') + 2

	with open('Generated Tokens.txt', 'w',newline='\n') as filehandle:
		filehandle.write(copy[0:p])
		for listitem in randomlist:
			filehandle.write('%s' % listitem+"."+fing_sort+"."+mot_sort+"\n")
		filehandle.write(copy[p:])
	print(randomlist, fing_sort, mot_sort)
	count+=1



	
#ex id : 238769695031951360
#id to to to 100000000000000000 > 999999999999999999