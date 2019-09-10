#include <iostream>
#include <math.h>

using namespace std;


bool PythagoreanTriplet(int a, int b, int c)
{
	if(pow(a,2) + pow(b,2)== pow(c,2))
	{
		return true;
	}
	
	return false;
}


int main()
{
	int c = 997,b=2,k=0;
	
	while(c>b)
	{
		int a=1, b = 1000-c-1;
		
		while(b>a)
		{
			if(PythagoreanTriplet(a,b,c)==true)
			{
				cout<<a*b*c;
				k = 1;
				break;
			}
			
			a++;
			b--;
		}
		
		if(k==1)
		{
			break;
		}
		
		c--;
	}
	
    return 0;
}