from attack import * 

def test_modify_putative_key():
	unique_ciphertext_symbols = [0,1,2,3,4,5,6,7,8,9]
	initial_keys = ['S','H', 'I', 'E', 'E', 'T', 'T', 'K', 'R', 'L']
#def test_initial_key():
#Page 19 example test case
#	ciphertext = []
'''
**********************************************************************************
							Smart Swap Tests
**********************************************************************************
'''
def test_smartswap_oneletterswap1():
	#See pg. 22
	# Cipher
	cipher_symbol = [0, 1, 2, 3, 4, 5, 6]
	frequency = [8.3, 7.5, 6.7, 6.6, 6.3, 5.5, 4.4]
	candidate_plaintext_letters = ['O', 'A', 'E', 'E', 'I', 'T', 'T']
	expected_output = ['A', 'O', 'E', 'E', 'I', 'T', 'T']

	computed = smartswap(cipher_symbol, frequency, candidate_plaintext_letters)
	print ', '.join(expected_output)
	print ', '.join(computed)
	if computed == expected_output:
		print("smartswap() Success!")
	else:
		print("smartswap() Fail")
	
def test_smartswap_oneletterswap2():
	#See pg. 22
	# Cipher
	cipher_symbol = [0, 1, 2, 3, 4, 5, 6]
	frequency = [8.3, 7.5, 6.7, 6.6, 6.3, 5.5, 4.4]
	candidate_plaintext_letters = ['A', 'O', 'E', 'E', 'I', 'T', 'T']
	expected_output = ['A', 'E', 'O', 'E', 'I', 'T', 'T']

	computed = smartswap(cipher_symbol, frequency, candidate_plaintext_letters)
	if computed == expected_output:
		print("smartswap() Success!")
	else:
		print("smartswap() Fail")


def test_smartswap_oneletterswap3():
	#See pg. 22
	#Cipher
	cipher_symbol = [0, 1, 2, 3, 4, 5, 6];
	frequency = [8.3, 7.5, 6.7, 6.6, 6.3, 5.5, 4.4];
	candidate_plaintext_letters = ['A', 'E', 'O', 'E', 'I', 'T', 'T'];
	expected_output = ['A', 'O', 'T', 'E', 'E', 'T', 'T'] 

	computed = smartswap(cipher_symbol, frequency, candidate_plaintext_letters)
	if computed == expected_output:
		print("smartswap() Success!")
	else:
		print("smartswap() Fail")

def testswap():
	#Must have swap 2 called after swap 1
	test_smartswap_oneletterswap1() #swaps 0 with 1
	test_smartswap_oneletterswap2()	#swaps 1 with 2
	test_smartswap_oneletterswap3()	#swaps 2 with 4, since swapping with 3rd will make no difference (they are both E's!)

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
								Digram
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

#run_get_putative_plaintext3()
#test_inner_hill_climb()

#test_create_digram_frequency()
#testswap()

#the --> 24,6,64
#abet --> 71,47,64,73
random_initial('24,6,64')
#random_initial('71,47,64,73')

