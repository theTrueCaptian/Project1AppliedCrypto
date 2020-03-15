from __future__ import division
from random import shuffle

#Global Variable: Frequencies of letters in the English Language
LETTER_FREQUENCIES	= [ 
	('a', 8.167), ('b',	1.492),	('c',	2.782), ('d',	4.253),	('e',	12.702),	('f',	2.228),	
	('g',	2.015),	('h', 6.094), ('i',	6.966),	('j',	0.153),	('k',	0.772), ('l',	4.025),	
	('m',	2.406),	('n',	6.749),	('o',	7.507),	('p',	1.929),	('q',	0.095),('r',	5.987),	
	('s',	6.327),	('t',	9.056),('u',	2.758),('v',	0.978),	('w',	2.361),('x',	0.150),	
	('y',	1.974),('z',	0.074)]
#Global Variable: Distribution Matrix for the English Language
#Source = http://keithbriggs.info/documents/english_latin.pdf
distribution_matrix_english_language =[ 
	#a b c d e f g h i j k l m n o p q r s t u v w x y z 
	[0.005, 0.037, 0.048, 0.054, 0.013, 0.013, 0.024, 0.020, 0.075, 0.000, 0.028, 0.158, 0.056, 0.440, 0.002, 0.018, 0.000, 0.146, 0.128, 0.204, 0.019, 0.050, 0.014, 0.001, 0.056, 0.003], 
	[0.019, 0.002, 0.000, 0.000, 0.121, 0.000, 0.000, 0.000, 0.014, 0.001, 0.000, 0.026, 0.000, 0.001, 0.028, 0.000, 0.000, 0.028, 0.005, 0.002, 0.041, 0.000, 0.000, 0.000, 0.024, 0.000], 
	[0.060, 0.000, 0.010, 0.000, 0.068, 0.000, 0.000, 0.086, 0.025, 0.000, 0.019, 0.015, 0.000, 0.000, 0.080, 0.000, 0.001, 0.014, 0.000, 0.031, 0.014, 0.000, 0.000, 0.000, 0.003, 0.000], 
	[0.035, 0.000, 0.000, 0.004, 0.087, 0.001, 0.006, 0.000, 0.051, 0.000, 0.000, 0.005, 0.003, 0.006, 0.039, 0.000, 0.000, 0.019, 0.023, 0.000, 0.011, 0.002, 0.003, 0.000, 0.006, 0.000], 
	[0.121, 0.006, 0.048, 0.157, 0.074, 0.026, 0.014, 0.011, 0.043, 0.001, 0.004, 0.084, 0.062, 0.200, 0.021, 0.024, 0.003, 0.305, 0.166, 0.080, 0.002, 0.043, 0.015, 0.015, 0.049, 0.002], 
	[0.028, 0.000, 0.000, 0.000, 0.036, 0.022, 0.000, 0.000, 0.033, 0.000, 0.000, 0.011, 0.000, 0.000, 0.097, 0.000, 0.000, 0.031, 0.001, 0.016, 0.011, 0.000, 0.000, 0.000, 0.001, 0.000], 
	[0.030, 0.000, 0.000, 0.002, 0.043, 0.000, 0.003, 0.050, 0.020, 0.000, 0.000, 0.008, 0.002, 0.004, 0.048, 0.000, 0.000, 0.024, 0.014, 0.002, 0.006, 0.000, 0.000, 0.000, 0.003, 0.000], 
	[0.249, 0.001, 0.000, 0.000, 0.710, 0.001, 0.000, 0.000, 0.184, 0.000, 0.000, 0.001, 0.001, 0.001, 0.106, 0.000, 0.000, 0.017, 0.002, 0.036, 0.016, 0.000, 0.000, 0.000, 0.024, 0.000], 
	[0.022, 0.007, 0.061, 0.059, 0.055, 0.035, 0.038, 0.000, 0.000, 0.001, 0.008, 0.077, 0.064, 0.332, 0.052, 0.009, 0.001, 0.051, 0.164, 0.167, 0.001, 0.034, 0.000, 0.003, 0.000, 0.002], 
	[0.005, 0.000, 0.000, 0.000, 0.016, 0.000, 0.000, 0.000, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000, 0.010, 0.000, 0.000, 0.000, 0.000, 0.000, 0.011, 0.000, 0.000, 0.000, 0.000, 0.000], 
	[0.001, 0.000, 0.000, 0.000, 0.050, 0.000, 0.000, 0.000, 0.027, 0.000, 0.000, 0.001, 0.000, 0.013, 0.002, 0.000, 0.000, 0.000, 0.006, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000], 
	[0.063, 0.000, 0.001, 0.056, 0.119, 0.009, 0.000, 0.000, 0.064, 0.000, 0.004, 0.141, 0.002, 0.000, 0.082, 0.002, 0.000, 0.001, 0.020, 0.019, 0.007, 0.007, 0.002, 0.000, 0.047, 0.000], 
	[0.080, 0.012, 0.001, 0.000, 0.127, 0.001, 0.000, 0.000, 0.037, 0.000, 0.000, 0.000, 0.011, 0.001, 0.051, 0.015, 0.000, 0.003, 0.011, 0.000, 0.013, 0.000, 0.000, 0.000, 0.025, 0.000], 
	[0.034, 0.001, 0.041, 0.354, 0.107, 0.004, 0.145, 0.004, 0.031, 0.001, 0.008, 0.006, 0.000, 0.009, 0.087, 0.000, 0.001, 0.000, 0.056, 0.139, 0.008, 0.002, 0.001, 0.000, 0.016, 0.000], 
	[0.010, 0.010, 0.011, 0.045, 0.006, 0.216, 0.008, 0.003, 0.013, 0.001, 0.015, 0.039, 0.081, 0.192, 0.037, 0.025, 0.000, 0.208, 0.039, 0.074, 0.194, 0.024, 0.060, 0.001, 0.004, 0.001], 
	[0.032, 0.000, 0.000, 0.000, 0.059, 0.000, 0.000, 0.015, 0.014, 0.000, 0.000, 0.033, 0.000, 0.000, 0.037, 0.013, 0.000, 0.045, 0.005, 0.013, 0.011, 0.000, 0.000, 0.000, 0.001, 0.000], 
	[0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.011, 0.000, 0.000, 0.000, 0.000, 0.000], 
	[0.073, 0.002, 0.009, 0.066, 0.259, 0.004, 0.009, 0.001, 0.092, 0.000, 0.011, 0.009, 0.015, 0.027, 0.089, 0.004, 0.000, 0.012, 0.049, 0.044, 0.021, 0.011, 0.001, 0.000, 0.028, 0.000], 
	[0.078, 0.001, 0.012, 0.001, 0.154, 0.001, 0.001, 0.098, 0.048, 0.000, 0.004, 0.009, 0.006, 0.003, 0.069, 0.030, 0.001, 0.010, 0.047, 0.134, 0.029, 0.000, 0.008, 0.000, 0.004, 0.000], 
	[0.052, 0.000, 0.004, 0.000, 0.119, 0.001, 0.000, 0.858, 0.092, 0.000, 0.000, 0.014, 0.001, 0.002, 0.178, 0.000, 0.000, 0.041, 0.037, 0.022, 0.022, 0.000, 0.013, 0.000, 0.023, 0.000], 
	[0.010, 0.010, 0.019, 0.014, 0.010, 0.002, 0.022, 0.000, 0.011, 0.000, 0.001, 0.044, 0.011, 0.086, 0.001, 0.033, 0.000, 0.072, 0.073, 0.075, 0.000, 0.000, 0.000, 0.000, 0.000, 0.001], 
	[0.018, 0.000, 0.000, 0.000, 0.142, 0.000, 0.000, 0.000, 0.029, 0.000, 0.000, 0.000, 0.000, 0.000, 0.007, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000], 
	[0.072, 0.000, 0.000, 0.000, 0.070, 0.000, 0.000, 0.084, 0.084, 0.000, 0.000, 0.003, 0.000, 0.016, 0.039, 0.000, 0.000, 0.005, 0.004, 0.000, 0.000, 0.000, 0.000, 0.000, 0.001, 0.000], 
	[0.002, 0.000, 0.002, 0.000, 0.002, 0.000, 0.000, 0.000, 0.002, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.003, 0.000, 0.000, 0.000, 0.005, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000], 
	[0.001, 0.002, 0.000, 0.000, 0.035, 0.000, 0.000, 0.000, 0.009, 0.000, 0.000, 0.002, 0.001, 0.001, 0.034, 0.004, 0.000, 0.002, 0.013, 0.001, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000], 
	[0.003, 0.000, 0.000, 0.000, 0.005, 0.000, 0.000, 0.000, 0.003, 0.000, 0.000, 0.000, 0.000, 0.000, 0.001, 0.000, 0.000, 0.001, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.000, 0.001]]
#Global Variable: Distribution Matric for the ciphertext. This will be constructed only once
#DistributionMatrixCipherText[][]

'''
**********************************************************************************
									Smart Swap 
**********************************************************************************
'''
'''
cipher_symbol is the list of unique ciphertext symbols, i.e. [0,1,2]. 
	The first call to swap must have the cipher symbols ranked in the order of its frequencies 
	in the ciphertext. 
frequency is the list of frequencies of each cipher_symbol. ith cipher symbol has frequency[i].
candidate_plaintext_letters is the list of candiate alphabet letters for the cipher_symbol

A call to the smartswap() will two swap elements in the solution i.e. candidate_plaintext_letters.
The choice between which two elements will be swapped will be changed progressively over "rounds".
In the first round, all the adjacent elements will be selected for swapping.
In the second round, the adjacent elements with a distance of two will be selected for swapping.
In the last round, candidate_plaintext_letters[0] with candidate_plaintext_letters[n]

returns: a swapped candidate_plaintext_letters array
'''
global currSwapI
global distance

currSwapI = 0
distance = 1
def smartswap(cipher_symbol, frequency, candidate_plaintext_letters):
	#Indicate we are using global swap variables
	global currSwapI
	global distance

	#Check if the arrays have valid lengths
	if len(cipher_symbol) != len(frequency) and len(cipher_symbol) != len(candidate_plaintext_letters):
		return None

	#Check if the swap will make a difference, i.e. the frequencies aren't nearly the same
	#Otherwise, ith element with j+1 element
	currSwapJ = currSwapI + distance
	#print str(candidate_plaintext_letters[currSwapI]) + " =? " + str(candidate_plaintext_letters[currSwapJ])
	#while isLetterMatchCipher(): 					#candidate_plaintext_letters[currSwapI] == candidate_plaintext_letters[currSwapJ]:
	#	currSwapJ = currSwapJ + 1
		#If the end is reach, swap no more
	#	if currSwapJ == len(cipher_symbol):
	#		return candidate_plaintext_letters

	#Swap given current variables
	temp = candidate_plaintext_letters[currSwapI]
	candidate_plaintext_letters[currSwapI] = candidate_plaintext_letters[currSwapJ]
	candidate_plaintext_letters[currSwapJ] = temp

	#Set the swaps variables to the next iteration
	currSwapI = currSwapI + 1
	currSwapJ = currSwapI + distance
	if currSwapJ == len(cipher_symbol):
		#If the j moves beyond the last element, change the distance
		#Reset currSwapI to 0 and reset currSwapJ
		distance = distance + 1
		currSwapI = 0
		currSwapJ = currSwapI + distance
		
	return candidate_plaintext_letters

'''
**********************************************************************************
									Digram 
**********************************************************************************
'''
'''
ciphertext is a string of symbols separated by , or space
unique_symbols is a list of unique cipher symbols that the matrix will follow i.e. [0, 1, 2, ...]
Returns an N x N matrix of a bigram for the ciphertext
'''
def create_digram_frequency(ciphertext, unique_symbols):
	arr_cipher = ciphertext.split(',')
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	#unique_arr_cipher = sorted(set(arr_cipher))
	#print ', '.join(unique_arr_cipher)

	#Form the matrix
	matrix = [[0]*len(unique_symbols) for _ in range(len(unique_symbols))]
	for i in range(len(arr_cipher)-1):
		char1 = arr_cipher[i]
		char2 = arr_cipher[i + 1]
		#get indices for the matrix
		ind1 = unique_symbols.index(char1)
		ind2 = unique_symbols.index(char2)
		matrix[ind1][ind2] = matrix[ind1][ind2] + 1 

	for i in range(len(matrix)): 
		for j in range(len(matrix[i])): 
			matrix[i][j] = matrix[i][j] /  len(ciphertext)
	return matrix

'''
**********************************************************************************
									inner hill climb 
**********************************************************************************
'''
'''
Return the letter given the symbol
'''
def get_symbol(putative_key, symbol):
	letter = None
	for x in putative_key:
		for cand_symbol in x[1]:
			if str(cand_symbol) == str(symbol):
				letter = x[0]
				return letter
	return letter
'''
ciphertext is a string of symbols separated by , or space
putative_key is an array of (cipher symbol, plaintext letter) i.e. [('I', [0]), ('L', [1]), ('E', [2])]

returns putative plaintext i.e. 'ISTSHETS'
'''
def get_putative_plaintext(ciphertext, putative_key):
	arr_cipher = ciphertext.split(',')
	plaintext = ''
	for i, symbol in enumerate(arr_cipher):
		#Find letter in putativekey given a symbol
		letter = get_symbol(putative_key, symbol)
		#letter = [x for x in putative_key if str(x[0])==str(symbol)][0][1]
		plaintext = plaintext + str(letter)
		if i<len(arr_cipher)-1:
			plaintext = plaintext + ','
	return plaintext
'''
Calculate the score of the digram and the expected matrices
'''
def getScore(digram_putative_plaintext, expected):
	#Check if the matrices are both the same size
	if len(digram_putative_plaintext) != len(expected) and len(digram_putative_plaintext[0]) != len(expected[0]):
		return None
	#See page 10 (formula) and 18 (justification) from http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf
	score = 0
	for i in range(len(digram_putative_plaintext)):
		for j in range(len(digram_putative_plaintext[i])):
			score = score + abs(digram_putative_plaintext[i][j]-expected[i][j])
	return score
'''
digram_putative_plaintext is the 26 by 26 array
n = 103, which is the number of cipher symbols total
'''
def inner_hill_climb(digram_putative_plaintext, n):
	#innerScore = d(Dc , E)
	innerScore = getScore(digram_putative_plaintext, distribution_matrix_english_language)
	print "Inner Score: "+str(innerScore)

	return innerScore
'''
**********************************************************************************
									random 
**********************************************************************************
'''

'''
symbol_cipher i.e. [0, 1, 2, ...
constraints: for each letter, list of symbols
return a list of constraints random symbols for each letter i.e. 
	('a', [40, 30, 81, 44, 3, 80, 69, 4, 97, 70])
	('b', [47]) 
	etc
'''
def rand(symbol_cipher, constraints):
	shuffle(symbol_cipher)
	print ', '.join(map(lambda x: str(x), symbol_cipher))
	ctr =0
	for i, letter in enumerate(constraints):
		for j, symbols in enumerate(letter[1]):
			constraints[i][1][j] = symbol_cipher[ctr]
			ctr = ctr + 1
	return constraints

'''
ciphertext i.e. '24,6,64'. Be sure that this is word for word
'''

def outer(ciphertext):
	#distribution of the symbols to each letter
	#Current mappings of letters to symbols
	constraints = [
		('a', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
		('b', [0]), 
		('c', [0, 0]), 
		('d', [0, 0, 0, 0]), 
		('e', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
		('f', [0, 0]), 
		('g', [0]), 
		('h', [0, 0, 0, 0, 0]), 
		('i', [0, 0, 0, 0, 0, 0, 0]), 
		('j', [0]), 
		('k', [0]), 
		('l', [0, 0, 0, 0]), 
		('m', [0, 0]), 
		('n', [0, 0, 0, 0, 0, 0, 0]), 
		('o', [0, 0, 0, 0, 0, 0, 0, 0]), 
		('p', [0]), 
		('q', [0]), 
		('r', [0, 0, 0, 0, 0, 0]), 
		('s', [0, 0, 0, 0, 0, 0]), 
		('t', [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
		('u', [0, 0]), 
		('v', [0]), 
		('w', [0, 0]), 
		('x', [0]), 
		('y', [0]), 
		('z', [0])
	]
	alphabets = [x[0] for x in constraints ]
	symbol_cipher = [x for x in range(103) ]


	key = None
	bestInitKey = None
	bestKey = None

	#parse ciphertext to determine Dc, the ciphertext_digram, N by N
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	unique_arr_cipher = sorted(set(ciphertext.split(',')))	
	ciphertext_digram = create_digram_frequency(ciphertext, unique_arr_cipher) #n by n, n = number of unique cipher symbols
	n = 103	#len(unique_arr_cipher)

	print ', '.join(unique_arr_cipher)
	print '\n'.join(''.join(str(row)) for row in ciphertext_digram)

	R = 100
	bestInitScore = 100000
	for r in range( R-1):
		#randomly initialize K = (k1, k2, . . . , kn) satisfying constraints na, nb, . . . , nz
		K = rand(symbol_cipher, constraints)
		print 'Random constraints i.e. the putative key:'
		print '\n'.join(''.join(str(row)) for row in K)

		#Generate the putative plaintext based on the constraints
		putative_plaintext = get_putative_plaintext(ciphertext, K)
		print "putative_plaintext = " + putative_plaintext
		#DP = digram matrix from DC and K
		digram_putative_plaintext = create_digram_frequency(putative_plaintext, alphabets)
		
		print 'Digram plaintext: '
		print '\n'.join(''.join(str(row)) for row in digram_putative_plaintext)
		
		initScore = inner_hill_climb(digram_putative_plaintext, n )
		print "Score: "+str(initScore)

		if initScore < bestInitScore:
			bestInitScore = initScore
			bestInitKey = K
		
	return bestInitScore

	'''
	#na to nz constraints initialize
	bestScore = randomInitialKey(letters)
	bestKey = bestKeyInit

	for i in range(25-1):
		for j in range(26-i-1):
	'''

#def initial_key():
'''
	The initial putative key is constructed using an educated guess, where the frequencies of the
	ciphertext symbols matches the frequency of a particular plaintext letter.
'''