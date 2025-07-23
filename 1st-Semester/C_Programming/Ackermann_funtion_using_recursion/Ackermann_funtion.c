/*
 ============================================================================
 Name        : Ackermann_function.c
 Author      : Vignesh
 Version     :
 Copyright   : ...
 Description : This Program is about the Ackermann function using recursion
 ============================================================================
 */

#include <stdio.h>
// #include <stdlib.h>
// #include <conio.h>

	int A(int m, int n);
	int main()
	{
		int m,n;
		// setbuf(stdout,NULL);
	    printf("Enter two numbers :: \n");
	    scanf("%d%d",&m,&n);
	    printf("\nOUTPUT :: %d\n",A(m,n));
	}
	int A(int m,int n)
	{
		if(m==0)
			return n+1;
		else if(n==0)
		return A(m-1,1);
		else
			return A(m-1,A(m,n-1));
}

