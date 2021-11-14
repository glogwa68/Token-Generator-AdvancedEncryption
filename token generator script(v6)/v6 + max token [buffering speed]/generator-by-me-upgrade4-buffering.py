import random
import requests
import urllib.request, random
import urllib.request
import string
import os
import sys
import datetime
import base64
import hashlib
import argparse
import time
import io
from datetime import date, datetime
from pprint import pprint
from random import randint
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from math import *


parser = argparse.ArgumentParser(description='number of retry.')
parser.add_argument("retry", help="number of retry.")
args = parser.parse_args()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#BUFF=2**10
N = args.retry
count = 0
numberf = 0
#sys.stdout = io.TextIOWrapper(io.BufferedWriter(sys.stdout.buffer, 2**10))

while(int(count)<int(N)):
	def generate():
		global numberf
		count=+1
		randomlist = []
		for i in range(1):
			num = random.randint(100000000000000000,999999999999999999)
			o = str(num)
			sort_ = base64.b64encode(o.encode('utf-8'))
			sort__ = str(sort_,'utf-8')
			timestamp = time.time()
			id = num
			id_calc = (id / 4194304) + 1420070400000
			timstamp_string = id_calc
			t1 = int(round(timestamp))
			t2 = int(round(timstamp_string))
			if len(sort__)==24:
				sorting = sort__
				randomlist.append(sorting)
			else :
				return 
		with open("millieux-max.txt", "r", encoding='utf-8', buffering=2**10) as milieux: 
		#with open("millieux-max.txt", "r", encoding='utf-8') as milieux: 
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
			return
		if (t1 >= 1420070400):
			if (1420070400 <= t2):
				time1_ = str(t1)
				time2_ = str(t2)
				bip = base64.b64encode(hashlib.sha1(base64.b64encode(time2_.encode('utf-16'))).digest())
				bop = str(bip)
				boup = ''.join(filter(str.isalnum, bop)) 
				pipe = str(boup).replace('b','',1)
				pop = str(pipe)
				if len(pop)==27:
					pipo = pop
					with open('Generated Tokens Avancé Buff.txt','r', encoding='utf-8', buffering=2**10) as fr:
					#with open('Generated Tokens Avancé Buff.txt','r', encoding='utf-8') as fr:
						copy = fr.read()
					p = copy.find('\r\n') + 2
					with open('Generated Tokens Avancé Buff.txt','w',newline='\n', encoding='utf-8', buffering=2**10) as filehandle:
					#with open('Generated Tokens Avancé Buff.txt','w',newline='\n', encoding='utf-8') as filehandle:
						filehandle.write(copy[0:p])
						for listitem in randomlist:
							filehandle.write('%s' % listitem+"."+fingo_+"."+pipo+'\n')
							print('%s' % listitem+"."+fingo_+"."+pipo)
						filehandle.write(copy[p:])
						file_size = os.path.getsize('Generated Tokens Avancé Buff.txt') 
					if file_size >= 1000000:
						with open('Generated Tokens Avancé Buff.txt','r', encoding='utf-8', buffering=2**10) as fr:
						#with open('Generated Tokens Avancé Buff.txt','r', encoding='utf-8') as fr:
							copy = fr.read()
						with open(f'token_gen/gen_{numberf}.txt', 'w') as saveFile:
							saveFile.write(copy)
						clear = open('Generated Tokens Avancé Buff.txt', 'r+', encoding='utf-8', buffering=2**10)
						clear.truncate(0) # need '0' when using r+
						clear.close()
						numberf+=1
					else :
						return
				else :
					return
			else :
				return
		else :
			return
	generate()



	
#ex id : 238769695031951360
#id to to to 100000000000000000 > 999999999999999999