import hashlib
from cryptography.fernet import Fernet
from secrets import compare_digest


master_password=input("Enter the master password : ")
a=hashlib.new("md5",master_password.encode()).hexdigest()
def ckeck(a):
    return (compare_digest(a,'58b4eb8271e10c17b510bdc91bfb3743'))
       
def add():
    name=input("Account name : ")
    pwd=input("Password : ")
    with open(r"C:\Users\KB\OneDrive - Frontera Consulting\Documents\apassword.txt",'a') as f:
        key=Fernet.generate_key()
        fernet = Fernet(key)
        pwd= fernet.encrypt(pwd.encode())



        f.write(name+"|"+pwd +"|"+key\n")
def view():
    
    with open(r"C:\Users\KB\OneDrive - Frontera Consulting\Documents\apassword.txt",'r') as f:
        for line in f.readlines():
            user,passw,key=line.split("|")
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
