#include <stdio.h>

int sumInt(int intA, int intB);

int main() {
	int int1, int2, sum;
	printf("Enter first integer: ")			; // request first integer
	scanf("%d",&int1)				; // read first integer
	printf("Enter second integer: ")		; // request second integer
	scanf("%d",&int2)				; // read second integer
	sum = sumInt(int1,int2)				; // add the integers
	printf("Sum = %d + %d = %d\n",int1,int2,sum)	; // display the sum
	return 0;
}

int sumInt(int intA, int intB) {
	return intA + intB;
}
