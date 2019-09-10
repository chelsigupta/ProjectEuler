#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(long n)
{
	bool k = true;
	
	for(int i=3; i<= sqrt(n); i+=2)
	{
		if(n%i == 0)
		{
			k = false;
			break;
		}
	}
	
	return k;
}

int main()
{
    long long sum = 2;
	
	for(long i=3; i<2000000; i+=2)
	{
		if(isPrime(i))
		{
			sum = sum + i;
		}		
	}
	
	cout<<sum;
	
    return 0;
}