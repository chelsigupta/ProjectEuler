#include <iostream>
#include <math.h>

using namespace std;

bool isPrime(int n)
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
    int  x = 2;
	int n = 3;
	
	while(x <= 10001)
	{
		if(isPrime(n))
		{
			x++;
		}
		
		n += 2;
	}
	
	cout<<n-2;
	
    return 0;
}