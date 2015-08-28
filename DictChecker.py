#!/usr/bin/python
#Owner :Jaideep Kekre 
import pickle


def initPickle(PicklePath):
	print "Verifying :" + str(PicklePath)
	PickleFile = open(PicklePath, 'a')
	PickleFile = open(PicklePath, 'r')
	
	try :
		dicta= pickle.load(PickleFile)

	except EOFError : 
		print "File Empty !! "
	
	pass

def main():
	initPickle('/home/kekre/Downloads/pkl.p')
	pass

if __name__ == '__main__':
	main()
	pass












#Owner : Jaideep Kekre