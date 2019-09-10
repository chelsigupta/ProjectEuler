#include <iostream>
#include <math.h>

using namespace std;


int sum_of_squares(int n)
	{
		long K = (n*(n+1)*(2*n+1))/6;
		return K;
	}
	
	
int square_of_sum(int n)
	{
		long K = (n*(n+1))/2;
		return pow(K,2);
	}
	

int main()
{
    long K = square_of_sum(100) - sum_of_squares(100);
	cout<<K;
	
    return 0;
}