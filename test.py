#from attack import * 


'''
**********************************************************************************
								Digram tests
**********************************************************************************
'''
def test_create_digram_frequency():
	#Note that the spaces in the cipher texts are preserved
	ciphertext = '0,9,4,9,8,2,4,9,5,0,7,2,9,8,5,2,2,8,6,1,0,7,2,3,0,9,3,9,8,2,4,8,0,5,9,0,1,0,7,6,8,6,1,0,7,6,4,4,8,5,2,0,7'
	arr_cipher = ciphertext.split(',')
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	unique_arr_cipher = sorted(set(arr_cipher))
	
	#unique_ciphersymbols = [0, 1, 2, 3, 4, 5 ,6 ,7, 8 ,9]; #preserve the order in the digram matrix
	expected_output = [
		[0, 1, 0, 0, 0, 1, 0, 5, 0, 2],
		[3, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 2, 0, 0, 0, 1, 1],
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 1, 0, 0, 0, 2, 2],
		[1, 0, 2, 0, 0, 0, 0, 0, 0, 1],
		[0, 2, 0, 0, 1, 0, 0, 0, 1, 0],
		[0, 0, 2, 0, 0, 0, 2, 0, 0, 0],
		[1, 0, 2, 0, 0, 2, 2, 0, 0, 0],
		[1, 0, 0, 1, 1, 1, 0, 0, 3, 0]
	]
	
	computed = create_digram_frequency(ciphertext, unique_arr_cipher)
	print '\n'.join(''.join(str(row)) for row in expected_output)
	print '-'
	print '\n'.join(''.join(str(row)) for row in computed)

	if computed == expected_output:
		print("create_digram_frequency() Success!")
	else:
		print("create_digram_frequency() Fail")

def test_create_digram_frequency2():
	#page 20 of http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf

	#Note that the spaces in the cipher texts are preserved
	ciphertext = 'I,S,T,S,H,E,T,S,E,I,T,E,S,H,E,E,E,H,R,L,I,T,E,K,I,S,K,S,H,E,T,H,I,E,S,I,L,I,T,R,H,R,L,I,T,R,T,T,H,E,E,I,T'
	unique_arr_cipher = ['E', 'T', 'I', 'S', 'H', 'R', 'L', 'K']
	expected_output = [
		[3, 2, 2, 2, 1, 0, 0, 1],
		[2, 1, 0, 2, 2, 2, 0, 0],
		[1, 5, 0, 2, 0, 0, 1, 0],
		[1, 1, 1, 0, 3, 0, 0, 1],
		[4, 0, 1, 0, 0, 2, 0, 0],
		[0, 1, 0, 0, 1, 0, 2, 0],
		[0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0]
	]
	
	computed = create_digram_frequency(ciphertext, unique_arr_cipher)
	print '\n'.join(''.join(str(row)) for row in expected_output)
	print '-'
	print '\n'.join(''.join(str(row)) for row in computed)

	if computed == expected_output:
		print("create_digram_frequency() Success!")
	else:
		print("create_digram_frequency() Fail")
'''
**********************************************************************************
								Inner Hill Climb Tests
**********************************************************************************
'''
def test_inner_hill_climb():
	#page 19 of http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf

	test_get_putative_plaintext()
	test_create_digram_frequency2()
	test_get_putative_plaintext2()

def test_get_putative_plaintext():
	#page 19 of http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf
	#Assume E and T map to some symbol already (from outer hill climb)
	#initial putative keys, element = (cipher symbol, plaintext letter)
	putative_key =  [('I', [0] ), ('L', [1]), ('E', [2, 5]), ('K', [3]), ('T', [4, 7]), ('R', [6]), ('H', [8]), ('S', [9])]
	ciphertext = '0,9,4,9,8,2,4,9,5,0,7,2,9,8,5,2,2,8,6,1,0,7,2,3,0,9,3,9,8,2,4,8,0,5,9,0,1,0,7,6,8,6,1,0,7,6,4,4,8,5,2,0,7'
	expected_putative_plaintext = 'I,S,T,S,H,E,T,S,E,I,T,E,S,H,E,E,E,H,R,L,I,T,E,K,I,S,K,S,H,E,T,H,I,E,S,I,L,I,T,R,H,R,L,I,T,R,T,T,H,E,E,I,T'

	computed = get_putative_plaintext(ciphertext, flatten(putative_key))
	if computed == expected_putative_plaintext:
		print("get_putative_plaintext() Success!")
	else:
		print("get_putative_plaintext() Fail")

def test_get_putative_plaintext2():
	#page 20 of http://www.cs.sjsu.edu/~stamp/RUA/homophonic.pdf
	#initial putative keys, element = (cipher symbol, plaintext letter)
	putative_key =  [('I', [0]), ('L', [1]), ('S', [2]), ('K', [3]), ('T', [4, 7]), ('E', [5, 9]), ('R', [6]), ('H', [8])]
	ciphertext = '0,9,4,9,8,2,4,9,5,0,7,2,9,8,5,2,2,8,6,1,0,7,2,3,0,9,3,9,8,2,4,8,0,5,9,0,1,0,7,6,8,6,1,0,7,6,4,4,8,5,2,0,7'
	expected_putative_plaintext = 'I,E,T,E,H,S,T,E,E,I,T,S,E,H,E,S,S,H,R,L,I,T,S,K,I,E,K,E,H,S,T,H,I,E,E,I,L,I,T,R,H,R,L,I,T,R,T,T,H,E,S,I,T'

	computed = get_putative_plaintext(ciphertext, flatten(putative_key))
	if computed == expected_putative_plaintext:
		print("get_putative_plaintext() Success!")
	else:
		print("get_putative_plaintext() Fail")

	digram = create_digram_frequency(computed, ['E', 'T', 'I', 'S', 'H', 'R', 'L', 'K'])
	print '\n'.join(''.join(str(row)) for row in digram)

def run_get_putative_plaintext3():
	putative_key =  [('I', [0]), ('K', [1]), ('E', [2, 5]), ('L', [3]), ('T', [4, 7]), ('R', [6]), ('H', [8]), ('S', [9])]
	ciphertext = '0,9,4,9,8,2,4,9,5,0,7,2,9,8,5,2,2,8,6,1,0,7,2,3,0,9,3,9,8,2,4,8,0,5,9,0,1,0,7,6,8,6,1,0,7,6,4,4,8,5,2,0,7'
	computed = get_putative_plaintext(ciphertext, flatten(putative_key))

	digram = create_digram_frequency(computed, ['E', 'T', 'I', 'S', 'H', 'R', 'L', 'K'])
	print '\n'.join(''.join(str(row)) for row in digram)


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
	arr_cipher = (ciphertext.strip().replace(' ', ',')).split(',')
	#Form a list of unique ordered symbol based on the ciphertext i.e. [0, 1, 2, ...]
	#unique_arr_cipher = sorted(set(arr_cipher))
	print str(arr_cipher)
	#updated = previously_calculated_digram
	#updated[]
	#Form the matrix
	need_update = [swapI[0], swapJ[0]]

	matrix = previously_calculated_digram#[[0]*len(unique_symbols) for _ in range(len(unique_symbols))]
	#Set what needs to be updated to zero
	for i in range(len(arr_cipher)-1):
		char1 = arr_cipher[i]
		char2 = arr_cipher[i + 1]
		if char1 in need_update or char2 in need_update:
			#get indices for the matrix
			ind1 = unique_symbols.index(char1)
			ind2 = unique_symbols.index(char2)
			matrix[ind1][ind2] = 0
	
	#Recalculate
	for i in range(len(arr_cipher)-1):
		char1 = arr_cipher[i]
		char2 = arr_cipher[i + 1]
		if char1 in need_update or char2 in need_update:
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

def test_efficient_digram_frequency():
	putative_plaintext = 'I,E,T,E,H,S,T,E, E,I,T,S,E,H,E,S,S,H,R,L,I,T,S,K,I,E,K,E,H,S,T,H,I,E,E,I,L,I,T,R,H,R,L,I,T,R,T,T,H,E,S,I,T'#['I', 'E', 'T', 'E', 'H', 'S', 'T', 'E', 'E', 'I', 'T', 'S', 'E', 'H', 'E', 'S', 'S', 'H', 'R', 'L', 'I', 'T', 'S', 'K', 'I', 'E', 'K', 'E', 'H', 'S', 'T', 'H', 'I', 'E', 'E', 'I', 'L', 'I', 'T', 'R', 'H', 'R', 'L', 'I', 'T', 'R', 'T', 'T', 'H', 'E', 'S', 'I', 'T']

	unique_arr_cipher = ['E', 'T', 'I', 'S', 'H', 'R', 'L', 'K']

	previously_calculated_digram = [
		[3, 2, 2, 2, 1, 0, 0, 1],
		[2, 1, 0, 2, 2, 2, 0, 0],
		[1, 5, 0, 2, 0, 0, 1, 0],
		[1, 1, 1, 0, 3, 0, 0, 1],
		[4, 0, 1, 0, 0, 2, 0, 0],
		[0, 1, 0, 0, 1, 0, 2, 0],
		[0, 0, 3, 0, 0, 0, 0, 0],
		[0, 0, 1, 1, 0, 0, 0, 0]
	]

	expected_output = [
		[2, 1, 2, 2, 3, 0, 0, 1],
		[2, 1, 0, 2, 2, 2, 0, 0],
		[3, 5, 0, 2, 0, 0, 1, 0],
		[1, 2, 1, 1, 1, 0, 0, 1],
		[2, 0, 1, 2, 0, 2, 0, 0],
		[0, 1, 0, 0, 1, 0, 2, 0],
		[0, 0, 3, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0, 0, 0]
	]
	computed = efficient_digram_frequency(previously_calculated_digram, ('E', 2), ('S', 0), putative_plaintext, unique_arr_cipher)
	print '\n'.join(''.join(str(row)) for row in expected_output)
	print '-'
	print '\n'.join(''.join(str(row)) for row in computed)

	if computed == expected_output:
		print("efficient_digram_frequency() Success!")
	else:
		print("efficient_digram_frequency() Fail")

	
#run_get_putative_plaintext3()
#test_inner_hill_climb()

#test_create_digram_frequency()
#testswap()

test_efficient_digram_frequency()

#the --> 24,6,64
#abet --> 71,47,64,73
#acetylsalicylic --> '71,77,64,73,72,35,82,15,56,84,77,72,35,52,27'
#the mow --> 24,6,64 54,42,75
#the go at me --> 24,6,64 101,88 87,6 54,65
#mozambique hates mozzarella --> '79,87,95,15,54,47,86,33,56,23 61,21,87,23,44 79,54,95,95,81,4,60,35,35,21'
#superintending surfboards zoysia yellow wolfs virilities urger 
#	--> 44,56,73,65,26,59,20,24,54,31,82,84,20,12 44,56,4,91,47,35,81,4,24,36 95,42,72,36,64,2 72,58,56,69,42,65 65,35,35,19,65 62,64,88,84,56,84,87,64,61,65 4,92,87,33,4
#outer_hill_climb('24,6,64')
#outer_hill_climb('71,47,64,73')
#outer_hill_climb('71,77,64,73,72,35,82,15,56,84,77,72,35,52,27')
'''
print "Sample ciphertext: 24,6,64 54,42,75"
input_var = raw_input("Enter the ciphertext: ")
key = outer_hill_climb(input_var)#(input_var.split(' '))	
print ("My guess for " + str(input_var)+" is "+get_putative_plaintext(ciphertext, flatten(key))) 

per_word = input_var.split(' ')
for word in per_word:
	output = outer_hill_climb(word)	
	print ("My guess for " + str(word)+" is "+output) 
'''

