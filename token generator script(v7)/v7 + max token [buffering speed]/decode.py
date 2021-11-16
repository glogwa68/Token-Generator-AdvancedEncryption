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


a = "zoo"
# decode the dictionary entries from base64
tag = base64.b64decode("NzA3ODAyMTg2MjkyMTgzOTE1")
cipher_text = base64.b64decode("HgA")
salt = base64.b64decode("41A")
nonce = base64.b64decode("HiZ8fDgkf9Mrg4Zd4HoU840ERBc")
# generate the private key from the password and salt
private_key = hashlib.scrypt(
password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
# create the cipher config
cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
# decrypt the cipher text
decrypted = cipher.decrypt_and_verify(cipher_text, tag)
print(decrypted)
