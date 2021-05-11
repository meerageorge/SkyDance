import sys
import os

def FindPalindrome(string: str) -> bool:

    length = len(string)

    mid = length/2
    i = 0
    # While not the end of the string
    while i <= mid:
        if string[i] != string[(length-1)-i]:
            return False
        i += 1
    return True


# Main Code
if __name__ == "__main__":

	try:
		fileName = sys.argv[1]
		try:
		    with open(fileName, mode='r') as file:
			    # read all lines at once
			    try:
			    	string = file.read()
			    	# close the file
			    	file.close()
			    	print (FindPalindrome(string))
			    except Exception:
			    	print ("Out of Memory")

		except FileNotFoundError as error:
			print (error)
	
	except IndexError as error:
		print (error)
		print ("Please pass the path to the file containing the sequence.")