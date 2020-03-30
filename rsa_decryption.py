"""

Made by: Erlend Sanden

erlend.h.sanden@gmail.com """

import math

public_key = [29815, 100127]
private_key = [None, 100127]

n = 100127

secret_private_keys = []     #appends to private key

plain_text = [84620, 66174, 66174, 5926, 9175, 87925, 54744, 54744, 65916, 79243, 39613, 9932, 70186, 85020, 70186, 5926, 65916, 72060, 70186, 21706, 39613, 11245, 34694, 13934, 54744, 9932, 70186, 85020, 70186, 54744, 81444, 32170, 53121, 81327, 82327, 92023, 34694, 54896, 5926, 66174, 11245, 9175, 54896, 9175, 66174, 65916, 43579, 64029, 34496, 53121, 66174, 66174, 21706, 92023, 85020, 9175, 81327, 21706, 13934, 21706, 70186, 79243, 9175, 66174, 81327, 5926, 74450, 21706, 70186, 79243, 81327, 81444, 32170, 53121]
message = []

def primegenerator(n):
    primes = []


    for checkifprime in range(2, n):  # for loop from 2 to number+1
        for num in range(2, checkifprime):  # checks if the dividable by any number except itself or 1
            if checkifprime % num == 0:
                break
        else:
            primes.append(
                checkifprime)  # if iteration is not dividable by any number except itself or 1 it get's appeneded to primes list
    return primes


def modulus():


    for p in primegenerator(n):
        for q in primegenerator(p):
            if (p * q == n):
                return p, q
                break



def phi():

    modulus1 = modulus()
    p = modulus1[0]
    q = modulus1[1]

    print("p- value {}, q-value {}".format(p, q))

    phi = (p-1)*(q-1)

    return phi

    # print("phi-value is {}".format(phi))


    # for e in range(2, phi):
    #     if(phi%e != 0 and n%e != 0 and e%2 != 0):
    #         return e, phi


def d():


    e = 29815
    phi_value = phi()

    print("e value is: {} ".format(e))

    print("phi-value is: {}".format(phi_value))

    d = 0

    while(d < 100000):

        d += 1
        if ((d * e) % phi_value == 1):
            secret_private_keys.append(d)
    print(" The private keys are: {} ".format(secret_private_keys))



def decrypt_message(plain_text):
    for decrypt in plain_text:
        decrypt_message = pow(decrypt, 64327, 100127)
        message.append(decrypt_message)

    for i in message:
        print(str(chr(i)))




modulus()
phi()
d()
decrypt_message(plain_text)



