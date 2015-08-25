#!/usr/bin/python
import os
import time

class Poller(ob):
	"""docstring for ClassName"""
	def __init__(self):
		super(Poller, self).__init__()
		self.timer = 10
		


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
            	before = after  
  				

  								
    			
def main():
	obj1 = Poller()
 	obj1.LongPoll('/home/kekre/Downloads')
 	print "DONE!"
 
 
if __name__ == '__main__':
 	main()
