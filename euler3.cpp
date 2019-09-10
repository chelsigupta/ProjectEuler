#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int i,j=0,a[100],max=0;	
	long long n = 600851475143;
	
	while(n%2==0)
	{
		a[j]=i;
		n = n/2;
		j = j+1;
	}
	
	for(i=3;i<=sqrt(n);i+=2)
	{
		while(n%i==0)
		{
			a[j]=i;
			n = n/i;
			j = j+1;
		}
	}
	
	if(n>2)
	{
		a[j] = n;
	}
	
		
	for(i=0;i<=j;i++)
	{
		if(a[i]>max)
		{
			max = a[i];
		}
	}
	
	cout<<max;
	
    return 0;
}