#! usr/bin/env python
file=raw_input("Enter the file name:")
print("*"*60)
def l_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    largestword = len(max(words, key=len))
    for word in words:
	 if len(word) == largestword:
         	return word
print("Largest word in the file : "+l_word(file+'.txt'))
