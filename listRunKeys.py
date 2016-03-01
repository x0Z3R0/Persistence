from _winreg import *

print r"*** Reading from SOFTWARE\Microsoft\Windows\CurrentVersion\Run ***"
aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run") 
for i in range(1024):                                           
    try:
        n,v,t = EnumValue(aKey,i)
        print n, v
    except EnvironmentError:                                               
        print "You have",i," tasks starting at logon..."
        break          
CloseKey(aKey) 