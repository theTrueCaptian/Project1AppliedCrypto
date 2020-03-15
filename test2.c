#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

//number of random start points
int numOfStart = 40;
int inputSize = 1000;
//frequency array for the 26 characters
int freqArr[] = {8, 1, 3, 4, 13, 2, 2, 6, 7, 1, 1, 4, 2, 7, 8, 2, 1, 6, 6, 9, 
					 3, 1, 2, 1, 2, 1};

//result return by the inner-hill climbing
struct interResult {
	int score;
	int keyArr[26][14];
};

/*int const A::digram[10][10] = { 
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0},  
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 0, 0, 0, 0, 0, 0, 0}, 
  {0, 0, 0, 7, 7, 7, 7, 0, 0, 0}, 
  {0, 0, 0, 7, 7, 7, 7, 0, 0, 0}, 
  {0, 0, 0, 7, 7, 7, 7, 0, 0, 0}, 
  {0, 0, 0, 7, 7, 7, 7, 0, 0, 0}
};

/*void print2DArray(int *array){
	for(int i = 0; i < (sizeof( array ); i++) {
		for(int j = 0; j < (sizeof( array[i] ); j++) {
	 		printf("%d ", array[i][j]);
		}
		printf("\n");
	} 
}
void printArray(int *array){
	int i;
	for (i=0;i < (sizeof (array) /sizeof (array[0]));i++) {
		printf("%lf ",array[i]);
	}
	printf("\n");
}*/
//innerHillClimb
struct interResult innerHillClimb(int keyArr[][14], int c[], int diFreqMatrix[][28]) {
	printf("Input to innerHillClimb: \n");
	for (int i=0;i < (sizeof (c) /sizeof (int));i++) {
		printf("%lf ",c[i]);
	}
	printf("\n");
		/*
	print2DArray(keyArr);
	printArray(c);
	print2DArray(diFreqMatrix);*/
}

//Create random keys
void createKeys(int keyArr[][14]) {
	int val[103];
	int i, j;
	struct timeval tm;
	gettimeofday(&tm, NULL);
	srandom(tm.tv_sec + tm.tv_usec * 1000000ul);
	for (i=0; i<103; i++) {
		val[i] = 0;
	}
	for (i=0; i<26; i++) {
		for (j=0; j<14; j++) {
			int succeed = 1;
			while (succeed) {
				int v = rand()%103;
				if (val[v] == 0) {
					keyArr[i][j] = v;
					succeed = 0;
				}
			}
			//use -1 to terminate 
			if (j == freqArr[i] - 1) {
				keyArr[i][j+1] = -1;
				break;
			}
		}
	}
}

//decrypt the ciphertext based on the key Array
void dec(int keyArr[][14], int c[], int p[]) {
	int i;
	for (i=0; i<inputSize; i++) {
    	if (c[i] != -1 && c[i] != -2) {
    		int m, n;
			for (m=0; m<26; m++) {
				for (n=0; n<14; n++) {
					if (keyArr[m][n] == c[i]) {
						p[i] = m;
					}
				}
			}
    	} else if (c[i] == -2) {
    		p[i] = -2;
    	} else {
    		p[i] = -1;
    		break;
    	}
	}
	
	//print the plaintext
	/*printf("The plaintext is:\n");
    for (i=0; i<inputSize; i++) {
    	if (p[i] != -1) {
    		printf("%d ", p[i]);
    	} else {
    		printf("\n");
    		break;
    	}
		
	}*/
	
}

//create digram frequency matrix based on the array p, containing an array of cipher letters 
void createDiFreqMatrix(int diFreqMatrix[][28], int p[]) {
	int i, m, n;
	for (m=0; m<28; m++) {
		for (n=0; n<28; n++) {
			diFreqMatrix[m][n]=0;
		}
	}
	//build a matrix like the digram frequency matrix for English
	for (i=0; i<inputSize; i++) {
		if (p[i] != -1 && p[i] != -2) {
			p[i]++;
		} else if (p[i] == -2) {
			p[i] = 0;
		} else {
			break;
		}
	}
	for (i=0; i<inputSize; i++) {
    	if (p[i+1] != -1 ) {
			diFreqMatrix[p[i]][p[i+1]]++;
		} else {
    		break;
    	}
	}
	
	//print the digram frequency matrix
	/*for (m=0; m<28; m++) {
		for (n=0; n<28; n++) {
			printf("%d ", diFreqMatrix[m][n]);
		}
		printf("\n");
	}*/
	
}

//random solution generator
void randomGen(int keyArr[][14], int c[]) {
	int score = 10000000;
	int r;
	for (r=0; r<numOfStart; r++) {
		createKeys(keyArr);
		int diFreqMatrix[28][28];
		//int p[inputSize];
		//dec(keyArr, c, p);
		createDiFreqMatrix(diFreqMatrix, c);
		struct interResult ir = innerHillClimb(keyArr, c, diFreqMatrix);
		//update the score and key array, if the returned score is smaller
		if (ir.score < score) {
			score = ir.score;
			int m, n;
			for (m=0; m<26; m++) {
				for (n=0; n<14; n++) {
					if (ir.keyArr[m][n] != -1) {
						keyArr[m][n] = ir.keyArr[m][n];
					} else {
						keyArr[m][n] = -1;
						break;
					}
				}
			}
		}
	}
}

//encrypt the plaintext
void enc(char *p, int encKey[][14], int c[]) {
	createKeys(encKey);
	//print the key used to encrypt the plaintext
	int i, j;
	printf("Keys to encrypt the plaintext:\n");
	for (i=0; i<26; i++) {
		for (j=0; j<14; j++) {
			if (encKey[i][j] != -1) {
				printf("%d ", encKey[i][j]);
			} else {
				break;
			}
		}
		printf("\n");
	}
	int schedule;
	int n;
	for (i = 0; i < inputSize; i++ ) {
		struct timeval tm;
		gettimeofday(&tm, NULL);
		srandom(tm.tv_sec + tm.tv_usec * 1000000ul);
		//change n to change the encryption scheme
		n = rand();
		switch(p[i]) {
			case 'a' :
				schedule = n%freqArr[0];
				c[i] = encKey[0][schedule];
				break;
			case 'b' :
				schedule = n%freqArr[1];
				c[i] = encKey[1][schedule];
				break;
			case 'c' :
				schedule = n%freqArr[2];
				c[i] = encKey[2][schedule];
				break;
			case 'd' :
				schedule = n%freqArr[3];
				c[i] = encKey[3][schedule];
				break;
			case 'e' :
				schedule = n%freqArr[4];
				c[i] = encKey[4][schedule];
				break;
			case 'f' :
				schedule = n%freqArr[5];
				c[i] = encKey[5][schedule];
				break;
			case 'g' :
				schedule = n%freqArr[6];
				c[i] = encKey[6][schedule];
				break;
			case 'h' :
				schedule = n%freqArr[7];
				c[i] = encKey[7][schedule];
				break;
			case 'i' :
				schedule = n%freqArr[8];
				c[i] = encKey[8][schedule];
				break;
			case 'j' :
				schedule = n%freqArr[9];
				c[i] = encKey[9][schedule];
				break;
			case 'k' :
				schedule = n%freqArr[10];
				c[i] = encKey[10][schedule];
				break;
			case 'l' :
				schedule = n%freqArr[11];
				c[i] = encKey[11][schedule];
				break;
			case 'm' :
				schedule = n%freqArr[12];
				c[i] = encKey[12][schedule];
				break;
			case 'n' :
				schedule = n%freqArr[13];
				c[i] = encKey[13][schedule];
				break;
			case 'o' :
				schedule = n%freqArr[14];
				c[i] = encKey[14][schedule];
				break;
			case 'p' :
				schedule = n%freqArr[15];
				c[i] = encKey[15][schedule];
				break;
			case 'q' :
				schedule = n%freqArr[16];
				c[i] = encKey[16][schedule];
				break;
			case 'r' :
				schedule = n%freqArr[17];
				c[i] = encKey[17][schedule];
				break;
			case 's' :
				schedule = n%freqArr[18];
				c[i] = encKey[18][schedule];
				break;
			case 't' :
				schedule = n%freqArr[19];
				c[i] = encKey[19][schedule];
				break;
			case 'u' :
				schedule = n%freqArr[20];
				c[i] = encKey[20][schedule];
				break;
			case 'v' :
				schedule = n%freqArr[21];
				c[i] = encKey[21][schedule];
				break;
			case 'w' :
				schedule = n%freqArr[22];
				c[i] = encKey[22][schedule];
				break;
			case 'x' :
				schedule = n%freqArr[23];
				c[i] = encKey[23][schedule];
				break;
			case 'y' :
				schedule = n%freqArr[24];
				c[i] = encKey[24][schedule];
				break;
			case 'z' :
				schedule = n%freqArr[25];
				c[i] = encKey[25][schedule];
				break;
			// \n will be encrypted as -1
			case '\n' :
				c[i] = -1;
				break;
			//space will be encrypted as -2
			case ' ' :
				c[i] = -2;
				break;
		}
    }
    //print ciphertext
    /*printf("The ciphertext is:\n");
    for (i=0; i<inputSize; i++) {
    	if (c[i] != -1) {
    		printf("%d ", c[i]);
    	} else {
    		printf("\n");
    		break;
    	}
		
	}*/
}

//cleans
/*int[] cleanInput(c){
	return int[0];
}*/

void main() {
	int keyArr[26][14];
	//get plaintext and generate ciphertext
	int encKey[26][14];
	int c[inputSize];
	char *input;
	input = malloc(inputSize * sizeof(*input)); 
	fgets (input, inputSize, stdin);  
	printf("Creating test cases.");
	enc(input, encKey, c);
	//int cleanc = cleanInput(c);
	/*printf("Done creatin test cases.");
	for (int i=0;i < (sizeof (c) /sizeof (int));i++) {
		printf("%lf ",c[i]);
	}
	printf("\n");*/
	//random solution generator
	randomGen(keyArr, c);
}