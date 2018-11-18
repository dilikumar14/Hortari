#include<stdio.h>
void main()
{
	int i,n;
	int jump=0;
	printf("Enter the no of Jumps\t");
	scanf("%d",&n);
	if(n==1)
		jump=0;

	for(i=2;i<=n;i++)
	{
		jump=i+jump;
	}
		
	printf("For %d jumps Jack is in %d step\n",n,jump);
	
}