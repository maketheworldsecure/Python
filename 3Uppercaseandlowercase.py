#! usr/bin/env python
print("Print Number of Upper and Lower case character")
print("*"*60)
string=raw_input("Enter string:")
print("*"*60)
countupper=0
countlower=0
for i in string:
      if(i.isupper()):
            countupper=countupper+1
      elif(i.islower()):
            countlower=countlower+1
print("The number of uppercase characters is:")
print(countupper)
print("The number of lowercase characters is:")
print(countlower)
print("*"*60)
if(i.find('Malware')):
            print("please dont search for malwares it may harm you device")
