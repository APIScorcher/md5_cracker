import hashlib
import time

counter = 1
print("-----" * 6)
time.sleep(1)
hash = input("Input your MD5 Hash: ")
wordlist = input("Input location of wordlist: ")

try:
	wordlist = open(wordlist, 'r')
except:
	print("Wordlist not found.")
	quit()
	
for password in wordlist:
	hash_obj = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
	print("-----" * 6)
	print("Trying password %d, %s" % (counter,password))
	counter += 1
	
	if hash_obj == hash:
		print("Password Found: %s" % (password))
		print("-----" * 6)
		time.sleep(10)
		break
else:
		print("Password couldn't be cracked.")
		
		