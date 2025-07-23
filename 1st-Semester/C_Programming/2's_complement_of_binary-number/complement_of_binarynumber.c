/*
 ============================================================================
 Name        : complement_of_binarynumber.c
 Author      : Vignesh
 Version     :
 Copyright   : Your copyright notice
 Description : This Program contains checking the 2's complement of binarynumber
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
// #include <conio.h>
int main(void) {
	int n;
	// setbuf(stdout,NULL);
	puts("Enter the number of bits do you want to enter : ");
	scanf("%d",&n);
	char binary[n+1];
	char onescomplement[n+1];
	char twoscomplement[n+1];
	int carry=1;
	printf("\nEnter the binary number : ");
	scanf("%s",binary);
	printf("%s",binary);
	printf("\nThe ones complement of the binary number is : ");
	for(int i=0;i<n;i++)
	{
		if (binary[i]=='0')
			onescomplement[i]='1';
		else if(binary[i]=='1')
			onescomplement[i]='0';
	}
	onescomplement[n]='\0';
	printf("%s",onescomplement);
	printf("\nThe twos complement of a binary number is : ");
	for(int i=n-1;i>=0;i--)
	{
		if(onescomplement[i]=='1'&&carry==1)
		{
			twoscomplement[i] = '0';
		}
		else if (onescomplement[i]=='0' && carry ==1)
		{
			twoscomplement[i]='1';
			carry = 0;
		}
		else
		{
			twoscomplement[i] =onescomplement[i];
		}
	}
	twoscomplement[n]='\0';
	printf("%s",twoscomplement);
	return EXIT_SUCCESS;
}
