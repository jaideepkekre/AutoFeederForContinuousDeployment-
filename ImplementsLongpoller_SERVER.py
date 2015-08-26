from LongPollerTOFeeder import Poller 

def main():
	polling_obj=Poller()
	polling_obj.LongPoll('/home/kekre/Downloads')


if __name__ == '__main__' :
	main()

#This process can be indivisually DAEMONIZED or be controlled by Supervisor 
#This implements the Poller class and is aimed at polling the server 