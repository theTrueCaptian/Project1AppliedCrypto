from __future__ import division
from random import shuffle
import sys

IS_PRINT_SCORES = True#False
#K = [('I', 0), ('L', 1), ('S', 2), ('K', 3), ('T', 4), ('T', 7), ('E', 5), ('E', 9), ('R', 6), ('H', 8)]
K = None
bestInitKey = None
bestKey = None

global R

R = 10	

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


'''
**********************************************************************************
									Digram Creation
**********************************************************************************
'''
'''
ciphertext is a string of symbols separated by , or space
unique_symbols is a list of unique cipher symbols that the matrix will follow i.e. [0, 1, 2, ...]
Returns an N x N matrix of a bigram for the ciphertext
'''
def create_digram_frequency(ciphertext, unique_symbols):
	arr_cipher = (ciphertext.strip().replace(' ', ', ,')).split(',')
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	#unique_arr_cipher = sorted(set(arr_cipher))

	#BUG!!!! Digram calculated wrong!!
	#Form the matrix
	matrix = [[0]*len(unique_symbols) for _ in range(len(unique_symbols))]
	for i in range(len(arr_cipher)-1):
		char1 = arr_cipher[i]
		char2 = arr_cipher[i + 1]
		if ' ' not in [char1, char2]: 
			#get indices for the matrix
			ind1 = unique_symbols.index(char1)
			ind2 = unique_symbols.index(char2)
			matrix[ind1][ind2] = matrix[ind1][ind2] + 1 

	for i in range(len(matrix)): 
		for j in range(len(matrix[i])): 
			matrix[i][j] = matrix[i][j] /  len(ciphertext)
	return matrix

'''
Uses a previously calculated digram and just updates certian rows and columns that were involved in some swap
previously_calculated_digram is the digram to update based on swapI and swapJ
unique_symbols is a list of unique cipher symbols that the previously_calculated_digram matrix will follow i.e. [0, 1, 2, ...]
swapI and swapJ are the keys that were involved in the swap i.e. if E and S were swapped, then we only consider those.
	e.g. ('E', 2), ('S', 0)
putative_plaintext i.e. 'I,E,T,E,H,S,T,E,E,I,T,S,E,H,E,S,S,H,R,L,I,T,S,K,I,E,K,E,H,S,T,H,I,E,E,I,L,I,T,R,H,R,L,I,T,R,T,T,H,E,S,I,T'
return the updated digram
'''
def efficient_digram_frequency(previously_calculated_digram, swapI, swapJ, ciphertext, unique_symbols):
	#arr_cipher = filter(lambda x:x==swapI[0] or x==swapJ[0], (ciphertext.strip().replace(' ', ',')).split(','))
	arr_cipher = (ciphertext.strip().replace(' ', ', ,')).split(',')
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	#unique_arr_cipher = sorted(set(arr_cipher))
	#print str(arr_cipher)
	#updated = previously_calculated_digram
	#updated[]
	#Form the matrix
	need_update = [swapI[0], swapJ[0]]

	matrix = previously_calculated_digram#[[0]*len(unique_symbols) for _ in range(len(unique_symbols))]
	#Set what needs to be updated to zero
	for i in range(len(arr_cipher)-1):
		char1 = arr_cipher[i]
		char2 = arr_cipher[i + 1]
		if (char1 in need_update or char2 in need_update) and (' ' not in [char1, char2]):
			#get indices for the matrix
			ind1 = unique_symbols.index(char1)
			ind2 = unique_symbols.index(char2)
			matrix[ind1][ind2] = 0
	
	#Recalculate
	for i in range(len(arr_cipher)-1):
		char1 = arr_cipher[i]
		char2 = arr_cipher[i + 1]
		if (char1 in need_update or char2 in need_update) and (' ' not in [char1, char2]):
			#get indices for the matrix
			ind1 = unique_symbols.index(char1)
			ind2 = unique_symbols.index(char2)
			matrix[ind1][ind2] = matrix[ind1][ind2] + 1 
	'''
	for i in range(len(matrix)): 
		for j in range(len(matrix[i])): 
			matrix[i][j] = matrix[i][j] /  len(ciphertext)
	'''
	return matrix

'''
**********************************************************************************
									inner hill climb 
**********************************************************************************
'''
'''
Swap item at r and c in inarr
'''
def swap(inarr, r, c):
	temp = inarr[r]
	inarr[r] = inarr[c]
	inarr[c] = temp
	return inarr

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
putative_key is an array of (cipher symbol, plaintext letter) i.e. [('I', 0), ('L', 1), ('E', 2)]
	Note key must be flatten before calling function e.g. flatten(key)

returns putative plaintext i.e. 'I,S, T,S,H, E,T,S'
'''
def get_putative_plaintext(ciphertext, putative_key):
	cipherwords = ciphertext.strip().split(' ')
	plaintext = ''

	for word in cipherwords:
		arr_cipher = word.split(',')
		for i, symbol in enumerate(arr_cipher):
			#if symbol!=' ':
			#Find letter in putativekey given a symbol
			#letter = get_symbol(putative_key, symbol)
			letter = [x for x in putative_key if str(x[1])==str(symbol)][0][0]
			plaintext = plaintext + str(letter)
			if i<len(arr_cipher)-1:
				plaintext = plaintext + ','
			#else:
		plaintext = plaintext + ' '
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
digram_putative_plaintext is the 26 by 26 array i.e. Dp
n = 103, which is the number of cipher symbols total
ciphertext is the cipher text
alphabets is the alphabets i.e. [a, b, c,...]

See page 27 http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf for pseudo

return score
'''
def inner_hill_climb( digram_putative_plaintext, n, ciphertext, alphabets):
	global K 
	global bestInitKey 
	global bestKey 

	#innerScore = d(Dc , E)
	innerScore = getScore(digram_putative_plaintext, distribution_matrix_english_language)
	#print "Inner Score: "+str(innerScore)

	for i in range(0, n-1-1):
		for j in range(0, n-i-1):
			Kprime = list(K)	#e.g. [('q', 26), ('r', 87), ('r', 87), ('r', 3)]

			if Kprime[j][0]!=Kprime[j+1][0]:
				#swap(K'j, K'j+1)
				#print str(j)+', '+str(j+1)
				swap(Kprime, j, j+1)

				#New digram i.e. digram matrix for Kprime using DP and DC
				putative_plaintext_prime = get_putative_plaintext(ciphertext, Kprime)
				#Dprime = create_digram_frequency(putative_plaintext_prime, alphabets)
				Dprime = efficient_digram_frequency(digram_putative_plaintext, Kprime[j], Kprime[j+1], putative_plaintext_prime, alphabets)

				#print 'Dprime, Digram plaintext: '
				#print '\n'.join(''.join(str(row)) for row in Dprime)
				
				#if d(D', E) < innerScore 
				if getScore(Dprime, distribution_matrix_english_language)<innerScore:
					#innerScore = d(D', E)
					innerScore = getScore(Dprime, distribution_matrix_english_language)

					K = Kprime
					digram_putative_plaintext = Dprime



	return innerScore
'''
**********************************************************************************
									Random 
**********************************************************************************
'''

'''
symbol_cipher i.e. [0, 1, 2, ...
constraints: for each letter, its key distribution i.e. [('a', 8), ('b', 1), ...]
return a list of keys of random symbols for each letter i.e. 
	('a', [40, 30, 81, 44, 3, 80, 69, 4, 97, 70])
	('b', [47]) 
	etc
'''
def rand(symbol_cipher, constraints):
	shuffle(symbol_cipher)
	#if DEBUG_OUTER: print ', '.join(map(lambda x: str(x), symbol_cipher))

	keys = []

	ctr =0
	for i, letter in enumerate(constraints):
		keys.append( (letter[0], []) )
		for j in range(0, letter[1]):
			if ctr<len(symbol_cipher):
				#print str(ctr)+": "+str(symbol_cipher[ctr])
				keys[i][1].append(symbol_cipher[ctr])
				ctr = ctr + 1
			else:
				print "Out of bounds:"+str(ctr)#+": "+str(symbol_cipher[ctr])
				print "symbol_cipher: "+str(symbol_cipher)
				print "constraints: "+str(constraints)
				print "keys: "+str(keys)

				sys.exit()

	return keys


'''
input:
	[	('a', [40, 30, 81, 44, 3, 80, 69, 4, 97, 70])
		('b', [47]) 	]
output: [(a, 40), (a, 30), ...]
'''
def flatten(input):
	return [(letter[0], sym) for letter in input for sym in letter[1] ] 

'''
constraints is keys distribution i.e.
	('a', 8)
	('b', 1) 
	etc
n = 103, which is the number of cipher symbols total
ciphertext is the cipher text
alphabets is the alphabets i.e. [a, b, c,...]
symbol_cipher is the set of symbols i.e. [0, 1, 2, ..., 102]
See page 27 http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf for pseudo

return score
'''
def random_initial(constraints, n, ciphertext, alphabets, symbol_cipher):
	global K 
	global bestInitKey 
	global bestKey 
	global R

	bestInitScore = sys.maxint
	for r in range(1, R+1):
		#randomly initialize K = (k1, k2, . . . , kn) satisfying constraints na, nb, . . . , nz
		#e.g. 	current_constraints  =  [('I', [1]), ('L', [15]), ('S', [43]), ('K', [23]), ('T', [32,36]), ('E', [54, 87]), ('R', [78]), ('H', [87])]
		#		K = [('I', 0), ('L', 1), ('S', 2), ('K', 3), ('T', 4), ('T', 7), ('E', 5), ('E', 9), ('R', 6), ('H', 8)]
		current_constraints = rand(symbol_cipher, constraints)
		K = flatten(current_constraints)
		if DEBUG_OUTER:
			print 'Random constraints i.e. the putative key, K:'
			print '\n'.join(''.join(str(row)) for row in K)

		#Generate the putative plaintext based on the constraints
		putative_plaintext = get_putative_plaintext(ciphertext, K)
		#if DEBUG_OUTER: print "putative_plaintext = " + putative_plaintext
		#DP = digram matrix from DC and K
		digram_putative_plaintext = create_digram_frequency(putative_plaintext, alphabets)
		
		if DEBUG_OUTER:
			print 'Dp, Digram plaintext: '
			print '\n'.join(''.join(str(row)) for row in digram_putative_plaintext)
		
		initScore = inner_hill_climb( digram_putative_plaintext, n, ciphertext, alphabets )
		if DEBUG_OUTER: print "Score: "+str(initScore)

		if initScore < bestInitScore:
			bestInitScore = initScore
			bestInitKey = K

			if IS_PRINT_SCORES:
				#print "bestInitScore: "+str(bestInitScore)
				print "\tA candidate plaintext = " + get_putative_plaintext(ciphertext, bestInitKey)+" Score: "+str(bestInitScore)
		
			
	return bestInitScore

'''
**********************************************************************************
									Outer Hill Climb 
**********************************************************************************
'''
'''
constraints is keys distribution i.e.
	('a', 8)
	('b', 1) 
	etc
	mj[1] must be greater than one!

See page 26 on outer swap 
'''
def outer_swap(constraints, mi, mj):
	if constraints[mj][1]>1:
		constraints[mi] = (constraints[mi][0], constraints[mi][1] + 1)  
		constraints[mj] = (constraints[mj][0], constraints[mj][1] - 1)  
	return constraints
'''
ciphertext i.e. '24,6,64'. 
'''
DEBUG_OUTER = False

def outer_hill_climb(ciphertext):
	global K 
	global bestInitKey 
	global bestKey 

	#distribution of the symbols to each letter
	#Current mappings of letters to symbols
	#initialize na, nb, . . . , nz as in Table 7 i.e. a pair of alphabet and distribution
	constraints = [
		('a', 10), 
		('b', 1), 
		('c', 2), 
		('d', 4), 
		('e', 15),
		('f', 2), 
		('g', 1), 
		('h', 5), 
		('i', 7), 
		('j', 1), 
		('k', 1), 
		('l', 4), 
		('m', 2), 
		('n', 7), 
		('o', 8), 
		('p', 1), 
		('q', 1), 
		('r', 6), 
		('s', 6), 
		('t', 11), 
		('u', 2), 
		('v', 1), 
		('w', 2), 
		('x', 1), 
		('y', 1), 
		('z', 1)
	]
	
	alphabets = [x[0] for x in constraints ]
	symbol_cipher = [x for x in range(103) ]

	#parse ciphertext to determine Dc, the ciphertext_digram, N by N
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	unique_arr_cipher = sorted(set(ciphertext.strip().replace(' ', ',').split(',')))	
	ciphertext_digram = create_digram_frequency(ciphertext, unique_arr_cipher) #n by n, n = number of unique cipher symbols
	n = 103	#len(unique_arr_cipher)

	if DEBUG_OUTER:
		print ', '.join(unique_arr_cipher)
		print '\n'.join(''.join(str(row)) for row in ciphertext_digram)

	#(m1, m2, . . . , m26) = (na, nb, . . . , nz)
	constraints_m = list(constraints)

	#na to nz constraints initialize
	bestScore = random_initial(constraints_m, n, ciphertext, alphabets, symbol_cipher)	
	bestKey = bestInitKey

	for i in range(0, 25):
		for j in range(0, 26-i):
			#(m'1, m'2, . . . , m'26) = (m1, m2, . . . , m26)
			constraints_mprime = list(constraints_m)

			#outerswap: m'j, m'j+i
			if constraints_mprime[j+i][1]>1:
				constraints_mprime = outer_swap(constraints_mprime, j, j+i)

				score = random_initial(constraints_mprime, n, ciphertext, alphabets, symbol_cipher)	
				if score<bestScore:
					constraints_m = constraints_mprime
					bestScore = score
					bestKey = bestInitKey
				else:
					constraints_mprime = constraints_m
					if constraints_mprime[j][1]>1:
						constraints_mprime = outer_swap(constraints_mprime, j+i, j)
						score = random_initial(constraints_mprime, n, ciphertext, alphabets, symbol_cipher)	
						if score < bestScore:
							constraints_m = constraints_mprime
							bestScore = score
							bestKey = bestInitKey
				if IS_PRINT_SCORES:
					#print "bestScore: "+str(bestScore)
					print "Current best guess for plaintext = " + get_putative_plaintext(ciphertext, bestKey)+" Score: "+str(bestScore)
		
	return bestKey

print "Sample ciphertext: 24,6,64 54,42,75"
input_var = raw_input("Enter the ciphertext: ")
key = outer_hill_climb(input_var)#(input_var.split(' '))	
print ("My guess for " + str(input_var)+" is "+get_putative_plaintext(input_var, key)) 

