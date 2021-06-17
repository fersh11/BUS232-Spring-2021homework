import pyAesCrypt

buffersize = 100 *1024
fileName = input("What's your file name: ")
password = input("password:  ")
cipher = "new-"+fileName[:len(fileName)-4:]
print("Decrypting {} ...".format(fileName))
try:
    pyAesCrypt.decryptFile(fileName,cipher,password,buffersize)
    print("{} Decrypted succesful".format(fileName))
except Exception as e:
    print("incorrect password :(")
