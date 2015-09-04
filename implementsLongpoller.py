#Owner: Jaideep Kekre		
from definesLongPoller import Poller 
from DictChecker import initPickle
#####################################################
#To customize this poller add oe edit varaibles in this section only 
# main() must remain untouched for better reusability 
PollThisLocation = '/home/kekre/Downloads'
PickleLocation   = '/home/kekre/Downloads/pkl.p'
NameOfObject     = 'SERVER POLLER'
#####################################################
def PollerCreator():
	print "Initializing PollerCreator() & Creating Poller Object "
	polling_obj=Poller(NameOfObject,PickleLocation)
	polling_obj.timer=5
	###########################LOGGING################################
	print "\nLOGGING implementsLongpoller.py PollerCreator()"
	print "PATH OF PICKLE FILE  : " + PickleLocation
	print "POLLING INTERVAL     : " + str(polling_obj.timer)
	print "POLLING THIS LOCATION: " +  PollThisLocation
	print "\n"
	##################################################################
	initPickle(PickleLocation)
	polling_obj.LongPoll(PollThisLocation)
	pass

def main():
	PollerCreator()



if __name__ == '__main__' :
	main()
	pass

#This process can be indivisually DAEMONIZED or be controlled by Supervisor 
#This implements the Poller class and is aimed at polling the server 
#Owner : Jaideep Kekre 