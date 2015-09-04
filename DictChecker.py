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
	print("THIS IS A CLASS , BY DESIGN THIS IS NOT TO BE DIRECTLY EXECUTED!")
	print("PLEASE IMPLEMENT THIS CLASS IN A SEPERATE MODULE! CHEERS!")
	pass

if __name__ == '__main__':
	main()
	pass












#Owner : Jaideep Kekre