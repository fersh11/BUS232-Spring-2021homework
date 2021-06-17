import pyAesCrypt

buffersize = 100 *1024
fileName = input("What's your file name: ")
password = input("password:  ")
cipher = fileName+'.enc'
print("Encrypting {} ...".format(fileName))
pyAesCrypt.encryptFile(fileName,cipher,password,buffersize)
print("{} Encrypted succesful".format(fileName))
