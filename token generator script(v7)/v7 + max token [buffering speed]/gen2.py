import random
import base64
import hashlib
import argparse
import time
from math import *
from Cryptodome.Cipher import AES

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

def main():
    parser = argparse.ArgumentParser(description='number of minutes to retry.')
    parser.add_argument("retry", help="number of minutes to retry.")
    args = parser.parse_args()
    count = 0
    retry = int(args.retry)
    while(count < retry):
        randomlist = []
        num = random.randint(100000000000000000,999999999999999999)
        sort = base64.b64encode(str(num).encode('utf-8'))
        encoded_sort = str(sort,'utf-8')
        current_timestamp = time.time()
        first_timestamp = (num / 4194304) + 1420070400000
        max_timestamp = int(round(current_timestamp))
        min_timestamp = int(round(first_timestamp))
        if len(encoded_sort) != 24:
            return
        randomlist.append(encoded_sort)
        with open("caracteres.txt", "r", encoding='utf-8', buffering=2**10) as caracteres_file: 
            allText = caracteres_file.read()
            words = allText.split()
            word = random.choice(words)	
            fingerprint = str(base64.b64encode(word.encode('utf-16')), 'utf-8').replace("/", "").replace("=", "")
        if len(fingerprint)!=6:
            return
        if (max_timestamp < 1420070400) or (1420070400 > min_timestamp):
            return
        key = str('b'+word).encode()
        def encrypt(password):
            salt = key
            private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
            cipher_config = AES.new(private_key, AES.MODE_GCM)
            cipher_text, tag = cipher_config.encrypt_and_digest(bytes(password, 'utf-8'))
            return {
            'tag': base64.b64encode(tag).decode('utf-8').replace("/", "").replace("=", ""),
            'cipher_text': base64.b64encode(cipher_text).decode('utf-8').replace("/", "").replace("=", ""),
            'salt': base64.b64encode(salt).decode('utf-8').replace("/", "").replace("=", ""),
            'nonce': base64.b64encode(cipher_config.nonce).decode('utf-8').replace("/", "").replace("=", "")
            }
        encrypted = str(encrypt(word))
        boup = ''.join(filter(str.isalnum, encrypted)) 
        pipe = str(boup).replace('b','',1).replace('ciphertext','.',1).replace('nonce','.',1).replace('tag','',1).replace('salt','',1)
        pipu = base64.b64encode(hashlib.sha1(hashlib.sha1(hashlib.sha1(base64.b64encode(pipe.encode('utf-16'))).digest()).digest()).digest())
        pop = str(pipu).replace('b','',1).replace("/", "").replace("=", "").replace("'", "")
        if len(pop)!=27:
            return
        with open('tokens.txt','a',newline='\n', encoding='utf-8', buffering=2**10) as filehandle:
            for listitem in randomlist:
                filehandle.write('%s' % listitem+"."+fingerprint+"."+pop+'\n')
        count+=1

if __name__ == "__main__":
    main()