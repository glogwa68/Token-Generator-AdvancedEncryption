import hashlib
import json
import random
import string
import sys
from base64 import b64encode

import discord
import numexpr as ne
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from discord.ext import tasks

ne.set_num_threads(10)

sys.setrecursionlimit(999999)
full = str(random.randint(0, 999999999999999999))

client = discord.Client()
global tup


async def get_user_exists(tup):
    try:
        await client.fetch_user(tup)
        return True
    except:
        return False

@tasks.loop(seconds=0.0001)
async def execute():
    def encrypt(plain_text, password):
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
        return {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8')
        }
    for repeat in range(10000000000000000000000000000000000000000000000000000001):
        cnt = 0
        for i in range(1, 1001):
            password = str(random.randint(100000000000000000, 999999999999999999))
            int_pass = int(password)
            first_timestamp = (int_pass / 4194304) + 1420070400000
            normal = int(round(first_timestamp))
            string_time = str(normal)
            delta_time = string_time[:10]
            int_time = int(delta_time)
            if not (1420070400 < int_time) and (int_time < 1620070400):
                return
            sort = b64encode(str(password).encode('utf-8'))
            encoded_sort = str(sort, 'utf-8')
            # password = input("id for user: ")

            # First let us encrypt secret message
            encrypted = encrypt(full, password)
            str_enc = str(f'{encrypted}')
            rem_enc = str(str_enc).replace('cipher_text', '').replace('nonce', '').replace('tag', '').replace('salt', '').replace(':', '')
            boup = ''.join(str(rem_enc))
            pipe = str(boup).replace("'", '').replace(",", '').replace(" ", '').replace("{", '').replace("}", '')

            ALL = pipe
            One = pipe[:0]
            lenght_chipher_text = pipe[:36]
            lenght_salt = pipe[36:60]
            lenght_nonce = pipe[60:84]
            lenght_tag = pipe[84:108]

            pipo = str(pipe).replace("/", "").replace("=", "").replace("'", "")
            premier = pipo[:24]
            deuxieme = pipo[24:30]
            troisieme = pipo[30:57]

            verif = "Nz" or "Mz"

            cnt += 1
            A1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
            if A1 in lenght_chipher_text or lenght_salt or lenght_tag or lenght_nonce:
                if cnt in [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]:
                    print(f"number of itérations : {cnt}")
                    with open('stock/token{}.txt'.format(cnt), 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                        if verif in encoded_sort[:2]:
                            tup = str(password)
                            result = await get_user_exists(tup)
                            if result:
                                print(f"valid id! : {password} : {result} --> continue")
                                filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                print(f"clé: {encoded_sort}.{deuxieme}.{troisieme}")
                            else:
                                print(f"not valid id : {password} : {result} --> continue")
                                continue
                        else:
                            continue

def main():
    global client

    def get_token():
        with open("token.json", 'r') as token_file:
            data = json.load(token_file)
            return data['token']

    token = get_token()

    client = discord.Client()

    @client.event
    async def on_ready():
        print("connected")
        execute.start()

    client.run(token)

if __name__ == '__main__':
    main()

