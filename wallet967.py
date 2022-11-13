import os
import secrets
import secp256k1 as ice

counter=0
cBTC=0
uBTC=0
address="12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr"

print("Search private key..."+"\n")

while (cBTC or uBTC) != address:
    key=int(secrets.token_hex(32),16) #random HEX (private key)
    cBTC=ice.privatekey_to_address(0,True,key) #compress address
    uBTC=ice.privatekey_to_address(0,False,key) #uncompress address
    counter+=1
    #print (hex(key).split('x')[-1])
    #print (cBTC + "\n" + uBTC)
    if counter % 10000 == 0:
    	print(f"Counter: {counter} HEX's")
    if (cBTC or uBTC) == address:
        found=hex(key).split('x')[-1]
        print ("FOUND!!!"+"\n"+found)
        with open("winner.txt","a") as file:
            file.write(str(found)+"\n")
            break
