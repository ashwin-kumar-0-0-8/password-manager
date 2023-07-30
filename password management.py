import hashlib #used for hashing the master password and later used for comparing
from cryptography.fernet import Fernet #encryption and decryption processes to ensure the security and reliability of your cryptographic
from secrets import compare_digest """used to securely compare two strings in constant time, which is crucial in cryptographic 
                                    applications to avoid potential timing attacks"""


master_password=input("Enter the master password : ")
a=hashlib.new("md5",master_password.encode()).hexdigest()
def ckeck(a):
    return (compare_digest(a,'58b4eb8271e10c17b510bdc91bfb3743'))
       
def add():
    name=input("Account name : ")
    pwd=input("Password : ")
    # where the user id and password is stored
    with open(r"C:\Users\KB\OneDrive - Frontera Consulting\Documents\apassword.txt",'a') as f: 
        key=Fernet.generate_key()
        fernet = Fernet(key)
        pwd= fernet.encrypt(pwd.encode())
        f.write(name+"|"+pwd +"|"+str(key)\n")
def view():
    
    with open(r"C:\Users\KB\OneDrive - Frontera Consulting\Documents\apassword.txt",'r') as f:
        for line in f.readlines():
            user,passw,key=line.split("|")
            fernet = Fernet(key)
            passw = fernet.decrypt(passw).decode()
            passw2=passw.rstrip()
            print("User : ",user,"  ,Password : ", passw2)
while(True):
    exit1=ckeck(a)
    if(exit1):
        print("invalid password")
        break
        
    mode=input("Enter the mode view or add password , to quite PRESS q: ").lower()
    
    if mode=='q':
        break
    elif mode=='view':
       view()
    elif mode=='add':

        add()
    else:
        print("invalid mode")

            
else:
    print("worng password")
