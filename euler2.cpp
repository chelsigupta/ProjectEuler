#include <iostream>

using namespace std;

int main()
{
    int  a = 1, b = 2, sum = 0, c = 0, i = 0;
	
	while(c<=4000000){
		c = a + b;
		a = b;
		b = c;
		
		if(c%2==0){
			sum = sum + c;
		}
		
		if(c>4000000){
			break;
		}
		//cout<<c<<' ';
		i++;
		
	}
	
	cout<<'\n'<<sum+2;
	
	
    return 0;
}