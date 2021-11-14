from pprint import pprint
from random import choice
import sys
import random
import requests
import urllib.request, random
import urllib.request
import string
import os
import os, random
from datetime import date
import datetime
import base64
import linecache
import fileinput
import time

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
	print("0")
		
	with open("millieux-max.txt", "r", encoding='UTF-8') as milieux: 
			allText = milieux.read() 
			m_words = list(map(str, allText.split()))
	print("1")		
	
	fing = str(random.choice(m_words))
	fing_ = base64.b64encode(fing.encode('utf-16'))
	fing__ = str(fing_,'utf-8')
	fing_sort = fing__.replace("/", "").replace("=", "")

	rdom_txt = random.choice(os.listdir("divisation"))
	big_brother = str("divisation/"+rdom_txt)
	#print(big_brother)

	randomlist2 = []
	for i2 in range(1):
		n2 = random.randint(1,1000000)
		o2 = int(n2)
	print("2")
	#print(o2)
	#print("divisation/"+rdom_txt)
	
	BIG = open(big_brother, "r", buffering=999999999).read(o2)
	time.sleep(1)
	words = BIG.readline(o2)
	print(words)
	print("3")
	
	#print("5 seconds left last generation for liberate buffer..")
	#time.sleep(5)
	#print(EndText)

	#with open(big_brother, 'r') as mots: 
	#	pit = mots.readlines()[20]
	#	print(pit)
		#words = list(map(str, pit.split()))	
		
	mot = str(random.choice(words))
	mot_ = base64.b64encode(mot.encode('utf-16'))
	mot__ = str(mot_,'utf-8')
	mot_sort = mot__.replace("/", "").replace("=", "")
	
	with open('MAXXED-tokens.txt','r') as fr:
			copy = fr.read()
	p = copy.find('\r\n') + 2
	print("4")
	
	with open('MAXXED-tokens.txt', 'w',newline='\n') as filehandle:
		filehandle.write(copy[0:p])
		for listitem in randomlist:
			filehandle.write('%s' % listitem+"."+fing_sort+"."+mot_sort+"\n")
		filehandle.write(copy[p:])
	print(randomlist, fing_sort, mot_sort)
	print("5 seconds left last generation for liberate buffer..")
	count+=1
	

	
#ex id : 238769695031951360
#id to to to 100000000000000000 > 999999999999999999