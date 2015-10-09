#!usr/bin/python 
#_info_   = This module is used to define logic to consume the contents of the pickle 

import pickle
import fcntl
import time 
import sys

class DictConsumer(object):

	"""Provides logic for Consumption of dict"""	 
	def __init__(self,fromCallingObj_PickleLocation):
		super(DictConsumer, self).__init__()
		self.PickleLocation  = fromCallingObj_PickleLocation
		self.SleepTime =10
		pass


	def  consumer(self):
		while 1:
			time.sleep(self.SleepTime)
			with open(self.PickleLocation,'rb+') as pkl_file : 
				
				mydict=list()				
				mydict = pickle.load(pkl_file)

				fcntl.flock(pkl_file, fcntl.LOCK_EX )
  				print "Locked from  consumer"
  				time.sleep(1)
				print "consuming" + str (mydict)
				if mydict[-1]=="NULL":
					print "List is empty! May the Force Be with You !"

				else :
					LastElement = mydict.pop()
					print("Last Added :" + LastElement)
					print ("New List is:" + str(mydict) )
					#Buildbot calling goes here
					pickle.dump(mydict, pkl_file)

				

				#
				fcntl.flock(pkl_file, fcntl.LOCK_UN)
				print "Unlocked from Consumer\n"	
			pass

		pass

def main():
	obj = DictConsumer('/home/kekre/Downloads/pkl.p')
	obj.consumer()
	pass

if __name__ == '__main__':
	main()
	



