The decrypted message:
https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Attacks_against_plain_RSA

First I made a primenumber generator, and then a nested for loop to find two prime numbers (p, q)
which together is equal to the public key (n). After that you can find the phi-value = (p-1)(q-1). 
The e-value was already known, but it could have been found by simple math. Thing thing was to find out the 
d-value (private key). The d-value was found by using a while loop and a simple if-statement D-value is equal 
to (d*e)%phi == 1. 

After the d-value was found, the message could be decrpyted by a foor loop, and using 
the formula pow(d, private key, public key) inside the loop. 

