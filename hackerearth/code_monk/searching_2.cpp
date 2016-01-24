//https://www.hackerearth.com/code-monk-searching/algorithm/monks-encounter-with-polynomial/

#include <iostream>
#include <math.h>
using namespace std;

int func1(int a,int b,int c,int k)
{
	for(int j=0;;j++)
    	{
    		if( ((a*pow(j,2)) + (b*j) + c)>=k )
    		{
    			return j;
    		}
    	}
    return 0;
}

int main()
{
    int a,b,c,k,n;
    cin>>n;
    
    for(int i=0;i<n;i++)
    {
    	cin>>a>>b>>c>>k;
    	cout<<func1(a,b,c,k)<<endl;
    }
}