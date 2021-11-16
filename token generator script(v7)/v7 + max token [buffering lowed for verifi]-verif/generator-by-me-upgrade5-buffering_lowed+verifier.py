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
import struct
import numpy as np
from datetime import date, datetime
from pprint import pprint
from random import randint
from flask import Flask, request, render_template
from bs4 import BeautifulSoup
from math import *
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

 


	
parser = argparse.ArgumentParser(description='number of minutes to retry.')
parser.add_argument("retry", help="number of minutes to retry.")
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

BUFF = 2*10
count = 0
num = args.retry
N = int(num)
numberf = 0
a = "OK"
#sys.stdout = io.TextIOWrapper(io.BufferedWriter(sys.stdout.buffer, BUFF))
# Only run if the user types in "start"
global fingo
# Loop until we reach time minutes running

while(1):
	while(1):
		while(int(count)<int(N)):
			def generate():
				#print(a)
				global count
				global N
				global numberf
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
				with open("millieux-max.txt", "r", encoding='utf-8', buffering=BUFF) as milieux: 
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
						integer_val = 5
						mono = str(fing)
						key = str('b'+mono).encode()
						time1_ = str(t1)
						time2_ = str(t2)
						def encrypt(plain_text, password):
							# generate a random salt
							salt = key
							# use the Scrypt KDF to get a private key from the password
							private_key = hashlib.scrypt(
							password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
							# create cipher config
							cipher_config = AES.new(private_key, AES.MODE_GCM)
							# return a dictionary with the encrypted text
							cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
							return {
							'tag': base64.b64encode(tag).decode('utf-8').replace("/", "").replace("=", ""),
							'cipher_text': base64.b64encode(cipher_text).decode('utf-8').replace("/", "").replace("=", ""),
							'salt': base64.b64encode(salt).decode('utf-8').replace("/", "").replace("=", ""),
							'nonce': base64.b64encode(cipher_config.nonce).decode('utf-8').replace("/", "").replace("=", "")
							}
						#def main():
						#	password = o
						#	print(a)
						#	encrypted = encrypt(fingo, password)
						#	print(a)
						#	print(encrypted)
						password = mono
						fing_string = str(fing)
						encrypted = encrypt(fing_string, password)
						bup = str(encrypted),
						bop = str(bup)
						boup = ''.join(filter(str.isalnum, bop)) 
						#pipe = str(boup).replace('b','.',1).replace('ciphertext','.-',1).replace('nonce','.-',1)
						pipe = str(boup).replace('b','',1).replace('ciphertext','.',1).replace('nonce','.',1).replace('tag','',1).replace('salt','',1)
						pipu = base64.b64encode(hashlib.sha1(hashlib.sha1(hashlib.sha1(base64.b64encode(pipe.encode('utf-16'))).digest()).digest()).digest())
						pop = str(pipu).replace('b','',1).replace("/", "").replace("=", "").replace("'", "")
						#print(pop)
						if len(pop)==27:
							pipo = pop
							with open('Generated Tokens Avancé Buff.txt','a',newline='\n', encoding='utf-8', buffering=BUFF) as filehandle:
							#with open('Generated Tokens Avancé Buff.txt','w',newline='\n', encoding='utf-8') as filehandle:
								for listitem in randomlist:
									TOKEN = str('%s' % listitem+"."+fingo_+"."+pipo+'\n')	
									filehandle.write(TOKEN)
									print('%s' % listitem+"."+fingo_+"."+pipo)
									numberf+=1
									count+=1
						else :
							return
						generate()
					else :
						return
				else :
					return
				generate()
			generate()



	
#ex id : 238769695031951360
#id to to to 100000000000000000 > 999999999999999999