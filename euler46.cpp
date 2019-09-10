#include <iostream>
#include <math.h>


using namespace std;


bool isPrime(int n)
{
	for(int i=3; i<= sqrt(n); i+=2)
	{
		if(n%i == 0)
		{
			return false;
		}
	}
	
	return true;
}


bool conjecture(int n)
{
	for(int i=(n-2);i>=2;i--)
	{
		if(isPrime(i)==true)
		{
			for(int j=1;j<= sqrt((n/2)-1);j++)
			{
				if((i+2*pow(j,2))==n)
				{
					return true;
				}
			}
		}
	}
	
	return false;
}


int main()
{
	bool x = true;
	int i = 9;
	
    while(x!=false)
	{
		if(isPrime(i)==false)
		{
			if(conjecture(i)==false)
			{
				x = false;
			}
		}
		
		i +=2;
	}
	
	cout<<(i-2);
	
    return 0;
}