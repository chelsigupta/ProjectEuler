#include <iostream>

using namespace std;


int hcf(long a, int b)
	{
		while(a!=b)
		{
			if(a>b)
			{
				a = a-b;
			}
			else
			{
				b = b-a;
			}
		}
		
		return a;
	}
	

int lcm(long a, int b)
	{
		long k = (a*b)/hcf(a,b);
		return k;
	}	
	

int main()
{
    long LCM = 20;	
	
	for(int i=19;i>=11;i--)
	{
		LCM = lcm(LCM,i);
	}
	
	cout<<LCM;
	
	
    return 0;
}
