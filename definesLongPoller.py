#!/usr/bin/python
#Owner :Jaideep Kekre
import os
import time
import simpleflock
import datetime
import pickle 


class Poller(object):
	"""docstring for ClassName"""
	def __init__(self,name,pkl):

		super(Poller, self).__init__()      #boilerplate 
		#self.pkl=''							#Default location of pickle module 									 
		self.timer = 2						#Default file poller interval 
		self.tout=10						#Default timeout for simple lock 
		self.w=12

		
		
		################################LOGGING###############################
		print"\n##################### LOGGING Poller Class #####################"
		print "CLASS object initialization DONE ,Following Defaults have set  "
		print "Name of  calling Object :" + name
		print "Poller timer :" + str(self.timer) + " "+str(type (self.timer))
		print "Simple_Lock Timeout :" + str(self.tout) + " "+str(type (self.tout))
		print "Location of Pickle file " + str(pkl) + " "+str(type(pkl))
		
		print"#################################################################\n"
		#######################################################################
		pass

	def AddToPickle(self,FilePathToBeAdded):
  		with simpleflock.SimpleFlock(pkl):
   			pkl_file = open(pkl, 'rb')
			mydict = pickle.load(pkl_file)
			print (mydict)
			
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
  						print newfile + "HAS BEEN ADDED"		
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