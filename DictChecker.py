#!/usr/bin/python
#Owner :Jaideep Kekre 
#_info_   = This Module performs basic checks on the pickle file  the poller 

import pickle
import sys
import time 
import fcntl


def initPickle(PicklePath):

    
    #Creates file if file does not exist 

	try :
		PickleFile = open(PicklePath, 'rb+')
		fcntl.flock(PickleFile, fcntl.LOCK_EX )
		print "Locked from initPickle"
		dicta = list()

	except IOError , OSError :
		print " FATAL ERROR Could not open file AW!  \n Please Create a file as  " + PicklePath
		#PickleFile.close()
		sys.exit(0)
		#exits the prog as file could not be opened 

	
	


	try :
		dicta= pickle.load(PickleFile)
		

	except EOFError : 
		dicta.append("NULL") 
		print "Pickle file was  Empty, Corrected in initPickle!! "
		pickle.dump(dicta, PickleFile)
		print dicta 

		time.sleep(1)
		

	fcntl.flock(PickleFile, fcntl.LOCK_UN)
	print "Unlocked from initPickle "
	PickleFile.close()

	
	

    #Write to pickle 




	pass



def main():
	initPickle('/home/admin/Downloads/pkl.p')
	print("THIS IS A CLASS , BY DESIGN THIS IS NOT TO BE DIRECTLY EXECUTED!")
	print("PLEASE IMPLEMENT THIS CLASS IN A SEPERATE MODULE! CHEERS!")
	pass

if __name__ == '__main__':
	main()
	pass












#Owner : Jaideep Kekre