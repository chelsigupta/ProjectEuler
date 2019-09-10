#include <iostream>

using namespace std;


long reverse_number(long m)
	{ 
		long  rem = 0;
		long rev_num = 0;

	while(m>0)
		{
			rem = m % 10;
			rev_num = rev_num * 10 + rem;
			m /= 10;
		}
		
		//cout<<rev_num<<' ';
		return rev_num;
	}

bool isPalindrome(long m)
	{
		if(m == reverse_number(m))
		{
			//cout<<true;
			return true;
		}
		else
		{	
			//cout<<false;
			return false;
		}
	}
		
int main()
{	
	int max = 0;
	
	for(int i=999;i>=100;i--)
	{
		for(int j=999;j>=100;j--)
		{
			long prod = i*j;
			//cout<<i<<"	"<<j<<"	"<<prod<<endl;
			if(isPalindrome(prod)==true && max < prod)
			{
				max = prod;
			}
		}
		
	}
	
	cout<<max;
	
    return 0;
}