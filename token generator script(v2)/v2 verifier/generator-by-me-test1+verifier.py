import random
import requests
import urllib.request, random
import urllib.request
import string
import os
import datetime
import base64
import hashlib
from datetime import date
from pprint import pprint

#class bcolors:
#    OK = '\033[92m' #GREEN
#    WARNING = '\033[93m' #YELLOW
#    FAIL = '\033[91m' #RED
#    RESET = '\033[0m' #RESET COLOR


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
		
	with open("millieux-max.txt", "r", encoding='utf-8') as milieux: 
		allText = milieux.read() 
		m_words = list(map(str, allText.split()))	
	
	fing = str(random.choice(m_words))
	fing_ = base64.b64encode(fing.encode('utf-16'))
	fing__ = str(fing_,'utf-8')
	fing_sort = fing__.replace("/", "").replace("=", "")
 
 
	#randomlist2 = []
	#for i2 in range(1):
	#	n2 = random.randint(1000000000,1636629227)
	#	o2 = str(n2)
	#	o3 = base64.b64encode(o2.encode('utf-8'))
	#	o4 = str(o3,'utf-8')
	#	o5 = o4.replace("/", "").replace("=", "")
	
	with open("mots.txt", "r", encoding='utf-8') as mots: 
		allText = mots.read() 
		e_words = list(map(str, allText.split()))
		o2 = str(random.choice(e_words))
		o3 = base64.b64encode(o2.encode('utf-8'))
		o4 = str(o3,'utf-8')
		o5 = o4.replace("/", "").replace("=", "")
	with open('temp/temp.txt', 'w',newline='\n') as temp_write:
		temp_write.write(o5)

	command = str("py sha1.py --string "+o5+" >>temp/sha-code.txt")
	texting = os.system(command)	
	
	with open("temp/sha-code.txt") as sha1_code :
		allShaText = sha1_code.read()
		
	resort = str(allShaText)

	ab = base64.b64encode(resort.encode('utf-8'))
	ab2 = str(ab,'utf-8').replace("/", "").replace("=", "")
	
	to_bin = str(resort)
	to_bin2 = str(ab2)
    #type = to_hex.hex()

	def text_to_binary(text):
		return ' '.join(format(ord(x), 'b') for x in text)
	binary = str(text_to_binary(to_bin))
	binary += str(text_to_binary(to_bin2))

	multi_binary = str(binary).replace(" ", "")
	
	command2 = str("py sha1.py --string "+multi_binary+" >>temp/sha-code-binary.txt")
	texting2 = os.system(command2)	

	with open("temp/sha-code-binary.txt") as sha1_code_b :
		allShaBinText = sha1_code_b.read()
		
	bin_b64 = base64.b64encode(allShaBinText.encode('utf-8'))
	bin_b64_ = str(bin_b64,'utf-8')
	bin_b64__ = bin_b64_.replace("/", "").replace("=", "")
	biz = str(bin_b64__)

	f1 = open('temp/temp.txt', 'r+')
	f1.truncate(0) # need '0' when using r+	
	f1.close()
	f2 = open('temp/sha-code.txt', 'r+')
	f2.truncate(0) # need '0' when using r+
	f2.close()
	f3 = open('temp/sha-code-binary.txt', 'r+')
	f3.truncate(0) # need '0' when using r+
	f3.close()

	with open('Generated Tokens.txt', 'w',newline='\n') as filehandle:
		for listitem in randomlist:
			filehandle.write('%s' % listitem+"."+fing_sort+"."+biz[0:27]+'\n')
			#print(bcolors.WARNING +'%s' % listitem+"."+fing_sort[0:7]+"."+biz[0:27]+" generated!"+ bcolors.RESET)
			#print('%s' % listitem+"."+fing_sort+"."+biz[0:27])
		
	command3 = str("py verify.py")
	texting3 = os.system(command3)
		
	clear = open('Generated Tokens.txt', 'r+')
	clear.truncate(0) # need '0' when using r+
	clear.close()
	print(count)
	count+=1



	
#ex id : 238769695031951360
#id to to to 100000000000000000 > 999999999999999999