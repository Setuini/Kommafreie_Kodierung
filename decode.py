def decode(number):
	result = []
	comments = 1
	while(len(number) > 0):
		#first number has 3 bit length
		n = 3
		while 1:
			try:

				#print "n: "+str(n);

				#first n bits in decimal
				next_len = int(number[:n], 2)
				#cut of first n bits
				number = number[n:]
				n = next_len

				#print "rest: "+str(number);

				#check the first bit of the rest, if it is 0 the end of the number before was 0
				#therefore interpret it as number
				if number[0] == '0':
					#print "parsed number: " + str(n)
					#cut of the 0
					number = number[1:]
					result.append(n)
					break
			except:
			    return "Invalid encoding"

	return result



def main():
	numbers = ['10010111111110000','100101111111100001010101000']
	for n in numbers:
		print "Decoding: "+str(n)
		print decode(n)
		print

main()