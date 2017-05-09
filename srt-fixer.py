import sys
import re
import argparse



regex = r'([0-9][0-9]):([0-9][0-9]):([0-9][0-9]),([0-9][0-9][0-9]) --> ([0-9][0-9]):([0-9][0-9]):([0-9][0-9]),([0-9][0-9][0-9])'
rexp = re.compile(regex)

parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()



with open(args.fname,'r+',newline='') as ifp:	
	for line in ifp:
		
		
		m = rexp.search(line)	
		
		
		if m is not None:
			
			LeftHour = int(m.group(1))			#	 Μεταβλητές στις οποίες αποθηκεύει 
			LeftMin = int(m.group(2)) 			#	 τις τιμες που βρίσκει στο input
			LeftSec	= int(m.group(3))	
			LeftMs = int(m.group(4))
			
			RightHour = int(m.group(5))
			RightMin = int(m.group(6)) 
			RightSec= int(m.group(7))
			RightMs = int(m.group(8))
	
		#------------------------------------------------------------------------
			
			NewLeftHour = LeftHour				#	 Μεταβλητές στις οποίες αποθηκεύει 
			LeftMin = int(m.group(2)) 			#	 τις τιμες που θα μπουν στο output
			NewLeftMin = LeftMin
			NewLeftSec = LeftSec + int(args.offset)
			NewLeftMs = LeftMs 
			
			NewRightHour = RightHour
			NewRightMin = RightMin 
			NewRightSec = RightSec + int(args.offset)
			NewRightMs = RightMs
			
		#------------------------------------------------------------------------

			ms = args.offset - int(args.offset) 		#	Mόνο τo δεκαδικό μέρος του offset
			NewLeftMs = int(LeftMs + (ms*1000))		
			NewRightMs = int(RightMs + (ms*1000))

			if NewLeftMs > 999:
				NewLeftMs = NewLeftMs -1000
				NewLeftSec = NewLeftSec + 1
			if NewRightMs > 999:
				NewRightMs = NewRightMs -1000
				NewRightSec = NewRightSec + 1

		#------------------------------------------------------------------------
						
			NewLeftHour = str(NewLeftHour).zfill(2)  	#	Μετατροπή των μεταβλητών σε string
			NewLeftMin = str(NewLeftMin).zfill(2)	
			NewLeftSec = str(NewLeftSec).zfill(2)
			NewLeftMs = str(NewLeftMs).zfill(2) 
			
			NewRightHour = str(NewRightHour).zfill(2)
			NewRightMin = str(NewRightMin).zfill(2) 
			NewRightSec = str(NewRightSec).zfill(2)
			NewRightMs = str(NewRightMs).zfill(3)
			
			ps = "%s:%s:%s,%s --> %s:%s:%s,%s\n"%(NewLeftHour, NewLeftMin, NewLeftSec, NewLeftMs, NewRightHour, NewRightMin, NewRightSec, NewRightMs)
			sys.stdout.write(ps)			
		else:
			sys.stdout.write(line)

		
ifp.close() 

		
		
		
