
'''
Created by Rajeev varma
import libraries to be used in the code
'''
import svgwrite # A Python library to create SVG Drawings
import codecs #This module defines base classes for standard Python codecs (encoders and decoders) and provides access to the internal Python codec registry which manages the codec and error handling lookup process
import sys #This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. It is always available.

'''
function that returns the width of the rectangle to be generated
'''
def findWidth(lines):
	count = 0
	for value in lines:
		ts = int(value.split()[0])# ts is the current time-stamp
		if ts in range(start, end+1):
			count += 1
	return 500/count#return the width of the rectangle

#read the input text file from the desktop and store each line as elements of a list
if __name__ == "__main__":
	
	try:
		sys.argv[1]
		sys.argv[2]
		sys.argv[3]
	except:
		print "Enter start and end timestamps"
		sys.exit()
	else:
		start = int(sys.argv[1])
		end = int(sys.argv[2])
		filename = sys.argv[3]
	f=codecs.open(filename,"r",encoding='utf-8') #Open an encoded file using the given mode and return a wrapped version providing transparent encoding/decoding. The default file mode is 'r' meaning to open the file in read mode.
	rfile = f.read()
	
	lines = rfile.splitlines()
	
	for value in lines:
		
		if value.split()[0]== str(start):
			start_index = lines.index(value)
		if value.split()[0]== str(end):
			end_index = lines.index(value)

	l2 = lines[start_index:end_index+1]
	#print l2
	#start_index = lines.index(start)
	#end_index = lines.index(end)
	#l2 = lines[start_index:nd_index]
	#print l2
	x_value = 0#initial x coordniate value

	width = findWidth(lines)
	dwg = svgwrite.Drawing('output.svg')

	for value in l2:
		ts = int(value.split()[0])
		state = value.split()[1]
		#for value in xrange(start)

		if state == 'True':
			dwg.add(dwg.rect((x_value, 0), (width, 50), fill='green'))
			x_value += width
		elif state == 'False':
			
			dwg.add(dwg.rect((x_value, 0), (width, 50), fill='red'))
				
			x_value += width

dwg.save()
