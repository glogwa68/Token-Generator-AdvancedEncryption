import random
import requests
import urllib.request, random
import urllib.request
import string
import os
import datetime
import base64
import hashlib
import argparse
import time
from datetime import date
from pprint import pprint
from random import randint


parser = argparse.ArgumentParser(description='number of retry.')
parser.add_argument("retry", help="number of retry.")
args = parser.parse_args()
print(args.retry)

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

N = args.retry
count = 0

while(int(count)<int(N)):
	def generate():
		name = randint(100000000, 9999999999)
		count=+1
		randomlist = []
		for i in range(1):
			n = random.randint(100000000000000000,999999999999999999)
			o = str(n)
			sort_ = base64.b64encode(o.encode('utf-8'))
			sort__ = str(sort_,'utf-8')
			randomlist.append(sort__)
		
		with open("millieux-max.txt", "r", encoding='utf-8') as milieux: 
			allText = milieux.read() 
			m_words = list(map(str, allText.split()))	
		
		fing = str(random.choice(m_words))
		fing_ = base64.b64encode(fing.encode('utf-16'))
		fing__ = str(fing_,'utf-8')
		fing_sort = fing__.replace("/", "").replace("=", "")
		fingo = str(fing_sort)
		if len(fingo)==6:
			fingo_ = fingo
		else :
			count=-1 
			return 
 
 
		#randomlist2 = []
		#for i2 in range(1):
		#	n2 = random.randint(1000000000,1636629227)
		#	o2 = str(n2)
		#	o3 = base64.b64encode(o2.encode('utf-8'))
		#	o4 = str(o3,'utf-8')
		#	o5 = o4.replace("/", "").replace("=", "")

		is_file = random.choice(os.listdir("end_word")) 
	
		export = str("end_word/"+is_file)

		with open(export, "r", encoding='utf-8') as mots: 
			allText = mots.read() 
			words = list(map(str, allText.split()))	
		
		#wording = hashlib.sha1(base64.b64encode(words.encode('utf-8'))
		#select_word = str(words)
		select_word = ''.join(filter(str.isalnum, words)) 
		bip = base64.b64encode(hashlib.sha1(base64.b64encode(select_word.encode('utf-16'))).digest())
		bop = str(bip)
		boup = ''.join(filter(str.isalnum, bop)) 
		pipe = str(boup).replace('b','',1)
		pop = str(pipe)
		if len(pop)==27:
			pipo = pop
			with open(f'token_files/Generated{name}.txt', 'w+',newline='\n') as filehandle:
				for listitem in randomlist:
					filehandle.write('%s' % listitem+"."+fingo_+"."+pipo+'\n')
					print('%s' % listitem+"."+fingo_+"."+pipo)
		else :
			return
	generate()



	
#ex id : 238769695031951360
#id to to to 100000000000000000 > 999999999999999999