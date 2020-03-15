/*  Maeda Hanafi 
	Inner Hill Climbing

	Input: Arbitrary Solution from Random Solution Generator
	Method: 
		Performs Fast algorithm for homophonic substitution cipher and derives local optimum solution.
		During the iterations, the solution is incrementally modified by swapping two elements at a time. 
	Output: The local optimum solution and corresponding score to the Random Solution Generator layer.
*/

/* 
	Global Variable: Distribution Matrix for the English Language
*/
DistributionMatrixEnglishLanguage[][];
/*
	Global Variable: Distribution Matric for the ciphertext 
*/
DistributionMatrixCipherText[][];

/*
	Input: Arbitrary Solution from Random Solution Generator
	Output: The local optimum solution and corresponding score to the Random Solution Generator layer.
*/
function InnerHillClimbing(arbitrarySolution[][]){
	/* Iterations */
	/* 
		Alter the key a little by swapping two elements. 
		Swap such that the frequency scores that already match with the frequency isn't moved 
	*/
	arbitrarySolution = smartswap(arbitrarySolution);
	/*
		Update the distribution matrix for the ciphertext with the modified key
	*/
	ModifiedDistributionMatrixCipherText = update_cipher_distribution();
	/*
		Compute score for the modified key using the modified distribution matrix
	*/
	score = getScore(ModifiedDistributionMatrixCipherText);

}

function getScore(ModifiedDistributionMatrixCipherText[][]){
	//See page 18
	/*
		Calculates how close distribution matrix of the cipher text is to the distribution of the expected language of plaintext
	*/
	
}

function test_smartswap_oneletterswap1(){
	//See pg. 22
	// Cipher
	cipher_symbol = [0, 1, 2, 3, 4, 5, 6];
	frequency = [8.3, 7.5, 6.7, 6.6, 6.3, 5.5, 4.4];
	candidate_plaintext_letters = ['O', 'A', 'E', 'E', 'I', 'T', 'T'];
	expected_output = ['A', 'E', 'O', 'E', 'I', 'T', 'T'];

	computed = smartswap();
	if(computed == expected){
		print("smartswap() Success!");
	}else{
		print("smartswap() Fail");
	}
}

function test_smartswap_oneletterswap2(){
	//See pg. 22
	// Cipher
	cipher_symbol = [0, 1, 2, 3, 4, 5, 6];
	frequency = [8.3, 7.5, 6.7, 6.6, 6.3, 5.5, 4.4];
	candidate_plaintext_letters = ['A', 'E', 'O', 'E', 'I', 'T', 'T'];
	expected_output = ['A', 'O', 'T', 'E', 'E', 'T', 'T'] 

}



