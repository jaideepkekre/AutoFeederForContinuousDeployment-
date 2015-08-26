#!/usr/bin/python
import os
import time

class Poller(object):
	"""docstring for ClassName"""
	def __init__(self):
		super(Poller, self).__init__()
		self.timer = 2
		


	def LongPoll(self,path):
		#path_to_watch = 'C:\\logs\\admin-PC\\deepesh\\Test_vaultize\\1.01\\1.01'
		#path_to_watch=str(path)
		
		before = [(f) for f in os.listdir (path)]
		print "watching path = " + path
		#print before 
		print "Sleep timer set to :" + str(self.timer)
		 	
		while 1:			
			time.sleep(self.timer) 	
			added =[]
			removed=[]		
  			after = [(f) for f in os.listdir (path)]
  			added = [f for f in after if not f in before]
  			removed = [f for f in before if not f in after]
  			if added:
  					for f in added :  						
  						print f + "HAS BEEN ADDED" 						
  						

  	            	before = list(after)
            	
            	
  				

  								
    			
def main():
	print("THIS IS A CLASS , BY DESIGN THIS IS NOT TO BE DIRECTLY EXECUTED!")
	print("PLEASE IMPLEMENT THIS CLASS IN A SEPERATE MODULE! CHEERS!")
	print("\nTo test this class , please uncomment the following code and set a valid path ! ")
	
#	obj1 = Poller()
#	obj1.LongPoll('path')
# 	print "DONE!"
 
 
if __name__ == '__main__':
 	main()
