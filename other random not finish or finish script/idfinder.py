import random
import base64 
import argparse

parser = argparse.ArgumentParser(description='number of retry.')
parser.add_argument("retry", help="number of retry.")
args = parser.parse_args()

N = args.retry
count = 0

while(int(count)<int(N)):
	with open("dick.txt", "r") as milieux: 
		allText = milieux.read() 
		words = list(map(str, allText.split()))	
		motus = str(random.choice(words))
		motus_ = motus[:24]
		bite = str(base64.b64decode(motus_), "utf-8")
		dickos = str(bite)
		print(dickos)
	count+=1
