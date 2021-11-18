# AES 256 encryption/decryption using pycryptodome library
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
from discord import HTTPException, NotFound
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
    password = str(random.randint(100000000000000000, 999999999999999999))
    int_pass = int(password)
    first_timestamp = (int_pass / 4194304) + 1420070400000
    normal = int(round(first_timestamp))
    string_time = str(normal)
    delta_time = string_time[:10]
    int_time = int(delta_time)
    if not (1520070400 < int_time) and (int_time < 1620070400):
        return
    sort = b64encode(str(password).encode('utf-8'))
    encoded_sort = str(sort, 'utf-8')
    # password = input("id for user: ")

    # First let us encrypt secret message
    encrypted = encrypt(full, password)
    str_enc = str(f'{encrypted}')
    rem_enc = str(str_enc).replace('cipher_text', '').replace('nonce', '').replace('tag', '').replace('salt',
                                                                                                      '').replace(
        ':', '')
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

    if "N" or "M" in One:
        A1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
        if A1 in lenght_chipher_text or lenght_salt or lenght_tag:
            A2 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
            if A2 in lenght_chipher_text or lenght_salt:
                A3 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                if A3 in lenght_tag:
                    A4 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                    if A4 in lenght_tag:
                        A5 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                        if A5 in ALL:
                            A6 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                            if A6 in lenght_chipher_text:
                                A7 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                if A7 in lenght_chipher_text:
                                    A8 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                    if A8 in lenght_chipher_text or lenght_nonce or lenght_tag:
                                        A9 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                        if A9 in lenght_chipher_text or lenght_salt or lenght_tag:
                                            A10 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                            if A10 in lenght_chipher_text:
                                                A11 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                if A11 in lenght_chipher_text or lenght_salt:
                                                    A12 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                    if A12 in lenght_salt:
                                                        A13 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                        if A13 in lenght_nonce or lenght_tag:
                                                            A14 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                            if A14 in lenght_chipher_text or lenght_nonce:
                                                                A15 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                if A15 in lenght_salt or lenght_tag:
                                                                    A16 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                    if A16 in ALL:
                                                                        tup = str(password)
                                                                        result = await get_user_exists(tup)
                                                                        print(f"cherching id: {tup}")
                                                                        if result:
                                                                            print(result)
                                                                            with open("user.txt", "a") as file:
                                                                                file.write("{}\n".format(tup))
                                                                            with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                print(f"ok1: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                        A17 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                        if A17 in lenght_nonce:
                                                                            tup = str(password)
                                                                            result = await get_user_exists(tup)
                                                                            print(f"cherching id: {tup}")
                                                                            if result:
                                                                                print(result)
                                                                                with open("user.txt", "a") as file:
                                                                                    file.write("{}\n".format(tup))
                                                                                with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                    filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                    print(f"ok2: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                            A18 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                            if A18 in lenght_chipher_text:
                                                                                tup = str(password)
                                                                                result = await get_user_exists(tup)
                                                                                print(f"cherching id: {tup}")
                                                                                if result:
                                                                                    print(result)
                                                                                    with open("user.txt", "a") as file:
                                                                                        file.write("{}\n".format(tup))
                                                                                    with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                        filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                        print(f"ok3: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                A19 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                if A19 in lenght_nonce:
                                                                                    tup = str(password)
                                                                                    result = await get_user_exists(tup)
                                                                                    print(f"cherching id: {tup}")
                                                                                    if result:
                                                                                        print(result)
                                                                                        with open("user.txt", "a") as file:
                                                                                            file.write("{}\n".format(tup))
                                                                                        with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                            filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                            print(f"ok4: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                    A20 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                    if A20 in lenght_nonce:
                                                                                        tup = str(password)
                                                                                        result = await get_user_exists(tup)
                                                                                        print(f"cherching id: {tup}")
                                                                                        if result:
                                                                                            print(result)
                                                                                            with open("user.txt", "a") as file:
                                                                                                file.write("{}\n".format(tup))
                                                                                            with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                print(f"ok5: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                        A21 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                        if A21 in lenght_salt or lenght_tag:
                                                                                            tup = str(password)
                                                                                            result = await get_user_exists(tup)
                                                                                            print(f"cherching id: {tup}")
                                                                                            if result:
                                                                                                print(result)
                                                                                                with open("user.txt", "a") as file:
                                                                                                    file.write("{}\n".format(tup))
                                                                                                with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                    filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                    print(f"ok6: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                            A22 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                            if A22 in lenght_tag:
                                                                                                tup = str(password)
                                                                                                result = await get_user_exists(tup)
                                                                                                print(f"cherching id: {tup}")
                                                                                                if result:
                                                                                                    print(result)
                                                                                                    with open("user.txt", "a") as file:
                                                                                                        file.write("{}\n".format(tup))
                                                                                                    with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                        filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                        print(f"ok7: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                                A23 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                if A23 in lenght_chipher_text or lenght_nonce:
                                                                                                    tup = str(password)
                                                                                                    result = await get_user_exists(tup)
                                                                                                    print(f"cherching id: {tup}")
                                                                                                    if result:
                                                                                                        print(result)
                                                                                                        with open("user.txt", "a") as file:
                                                                                                            file.write("{}\n".format(tup))
                                                                                                        with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                            filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                            print(f"ok8: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                                    A24 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                    if A24 in lenght_nonce:
                                                                                                        tup = str(password)
                                                                                                        result = await get_user_exists(tup)
                                                                                                        print(f"cherching id: {tup}")
                                                                                                        if result:
                                                                                                            print(result)
                                                                                                            with open("user.txt", "a") as file:
                                                                                                                file.write("{}\n".format(tup))
                                                                                                            with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                                filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                                print(f"ok9: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                                        A25 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                        if A25 in ALL:
                                                                                                            tup = str(password)
                                                                                                            result = await get_user_exists(tup)
                                                                                                            print(f"cherching id: {tup}")
                                                                                                            if result:
                                                                                                                print(result)
                                                                                                                with open("user.txt", "a") as file:
                                                                                                                    file.write("{}\n".format(tup))
                                                                                                                with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                                    filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                                    print(f"ok10: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                                            A26 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                            if A26 in lenght_chipher_text:
                                                                                                                A27 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                                if A27 in lenght_salt:
                                                                                                                    A28 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                                    if A28 in lenght_chipher_text or lenght_salt or lenght_tag:
                                                                                                                        A29 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                                        if A29 in lenght_salt:
                                                                                                                            A30 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(1))
                                                                                                                            if A30 in lenght_chipher_text or lenght_tag:
                                                                                                                                tup = str(password)
                                                                                                                                result = await get_user_exists(tup)
                                                                                                                                print(f"cherching id: {tup}")
                                                                                                                                if result:
                                                                                                                                    print(result)
                                                                                                                                    with open("user.txt", "a") as file:
                                                                                                                                        file.write("{}\n".format(tup))
                                                                                                                                    with open('tokens.txt', 'a', newline='\n', encoding='utf-8', buffering=2 ** 10) as filehandle:
                                                                                                                                        filehandle.write(f"{encoded_sort}.{deuxieme}.{troisieme}" + '\n')
                                                                                                                                        print(f"GOD: {encoded_sort}.{deuxieme}.{troisieme}")
                                                                                                                            else:

                                                                                                                                return
                                                                                                                        else:

                                                                                                                            return
                                                                                                                    else:

                                                                                                                        return
                                                                                                                else:

                                                                                                                    return
                                                                                                            else:

                                                                                                                return
                                                                                                        else:

                                                                                                            return
                                                                                                    else:

                                                                                                        return
                                                                                                else:

                                                                                                    return
                                                                                            else:

                                                                                                return
                                                                                        else:

                                                                                            return
                                                                                    else:

                                                                                        return
                                                                                else:

                                                                                    return
                                                                            else:

                                                                                return
                                                                        else:

                                                                            return
                                                                    else:

                                                                        return
                                                                else:

                                                                    return
                                                            else:

                                                                return
                                                        else:

                                                            return
                                                    else:

                                                        return
                                                else:

                                                    return
                                            else:

                                                return
                                        else:

                                            return
                                    else:

                                        return
                                else:

                                    return
                            else:

                                return
                        else:

                            return
                    else:

                        return
                else:

                    return
            else:

                return
        else:

            return
    else:

        return

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
