#!/usr/bin/python
#Owner :Jaideep Kekre
#_author_ = Jaideep Kekre
#_info_   = This module contains the logic for the Poller 

import os
import time
import datetime
import pickle 
import fcntl



class Poller(object):
	""" Provides logic for Poller  """
	def __init__(self,fromCallingObj_name,fromCallingObj_pickleLoc):

		super(Poller, self).__init__()               #boilerplate 
		#self.pkl=''							     #Default location of pickle module 									 
		self.timer = 2						         #Default file poller interval 
		self.tout=10						         #Default timeout for simple lock 
		self.PickleLocation=fromCallingObj_pickleLoc #Convert argument (LOCATION OF PICKLE FILE ) to instance variable 
		self.NameOFCurrentObj=fromCallingObj_name    #Convert argumet (NAME OF CALLING OBJECT) to instance variable 

		
		
		################################LOGGING###############################
		print"\n##################### LOGGING Poller Class #####################"
		print "CLASS object initialization DONE ,Following Defaults have set  "
		print "Name of  calling Object :" + self.NameOFCurrentObj
		print "Poller timer :" + str(self.timer) + " "+str(type (self.timer))
		print "Simple_Lock Timeout :" + str(self.tout) + " "+str(type (self.tout))
		print "Location of Pickle file " + str(self.PickleLocation) + " "+str(type(self.PickleLocation))
		
		print"#################################################################\n"
		#######################################################################
		pass




	def AddToPickle(self,FilePathToBeAdded):

  		#print"Contents of self :"+str(dir(self))
  		Lista = list()
  		#temp = list()
  		
  		#with simpleflock.SimpleFlock(self.PickleLocation):
  		with open(self.PickleLocation,'r+b') as PickleRead: 
  			fcntl.flock(PickleRead, fcntl.LOCK_EX )
  			print "Locked from AddToPickle read"
   				

			try : 
				Lista= pickle.load(PickleRead)
				print "Contents of Dict before adding are "
				print Lista 

				

			except EOFError : 
				Lista.append(NULL) 
				pickle.dump(Lista,PickleRead)
				print "Pickle file was  Empty , Corrected  in AddToPickle!! "
				
				pass

			fcntl.flock(PickleRead, fcntl.LOCK_UN)
			PickleRead.close()
			print "Unlocked from AddToPickle read\n"


			pass


		with open(self.PickleLocation,'wb') as PickleWrite :
			fcntl.flock(PickleWrite, fcntl.LOCK_EX )
  			print "Locked from AddToPickle write"
			#temp[FilePathToBeAdded] = "Not Processed"
			print "Contents of Dict are : "
			Lista.append(FilePathToBeAdded)
			print Lista 
			pickle.dump(Lista,PickleWrite)
			time.sleep(1)
						
			fcntl.flock(PickleWrite, fcntl.LOCK_UN)
			PickleWrite.close()
			print "Unlocked from AddToPickle write \n"

			#Sleep for 2 sec to cater for disk write issues 



	       


			
			pass
   		pass	
   		



	def LongPoll(self,path):
		
		before = [(files) for files in os.listdir (path)]
		###############################LOGGING##############################
		print "\n"
		print "########################LOGGING LongPoll Function ###############"
		print "watching path = " + path
		print "Sleep timer set to :" + str(self.timer)
		print "#############################################################"
		################################################################### 


		while 1:			
			time.sleep(self.timer) 	
			added =[]
			removed=[]		
  			after = [(files) for files in os.listdir (path)]
  			added = [files for files in after if not files in before]
  			removed = [files for files in before if not files in after]
  			if added:
  					for newfile in added :  						
  						print newfile	
  						self.AddToPickle(newfile)
  						print newfile + " HAS BEEN ADDED"		
  							#play with pickle file 

  						pass					
  						
  	            	before = list(after)
  	            	pass
  	        pass

  	
       

            	
            	
  				

  								
    			
def main():
	print("THIS IS A CLASS , BY DESIGN THIS IS NOT TO BE DIRECTLY EXECUTED!")
	print("PLEASE IMPLEMENT THIS CLASS IN A SEPERATE MODULE! CHEERS!")
	print("\nTo test this class , please uncomment the following code and set a valid path ! ")
	
#	print "obj1 = Poller()""
#	print "obj1.LongPoll('path')""
# 	print "print "DONE!"
	pass
	
 
 
if __name__ == '__main__':
 	main()
 	pass
 	
#Jaideep Kekre 