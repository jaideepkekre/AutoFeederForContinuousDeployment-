from LongPollerTOFeeder import Poller 

def main():
	polling_obj=Poller()
	polling_obj.timer=5
	polling_obj.LongPoll('/home/kekre/Downloads')
	pass



if __name__ == '__main__' :
	main()
	pass

#This process can be indivisually DAEMONIZED or be controlled by Supervisor 
#This implements the Poller class and is aimed at polling the server 