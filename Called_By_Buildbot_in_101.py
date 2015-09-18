import shutil 
import subprocess
import fcntl

NASControlFilePath = '/mnt/Server/QA/Automation_Data/AutoFiringData/CurrentServer.txt'
CopyDestination='/home/web/vaultize/'
#CopyDestination='/home/kekre/Scratch/'
LookHere = '/mnt/Server/Vaultize_build/Server/Release_15.1.maint/'
#LookHere = '/home/kekre/Scratch/test/'
print "variables set"

def fileReadCopy():
	server=open(NASControlFilePath,'r')
	fcntl.flock(server, fcntl.LOCK_EX )
	x=server.read()
	fcntl.flock(server, fcntl.LOCK_UN )
	server.close()
	x=x.strip()	
	#x= x[0:-2]
	print "Attempting to install Server :" + x
	dest = CopyDestination + x 
	src = LookHere + x 
	print src
	shutil.copyfile(src,dest)

	pass
def callScript():
	subprocess.call(['./ServerInstall.sh'])


def main():
	fileReadCopy()

	pass


if __name__ == '__main__':
	main()




    
    #Creates file if file does not exist 

	




