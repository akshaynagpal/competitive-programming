//https://www.hackerearth.com/code-monk-searching/algorithm/the-old-monk/

#include <iostream>
using namespace std;

int main()
{
    int tc,n;
    cin>>tc;
    for(int i=0;i<tc;i++)
    {
    	cin>>n;
    	int A[n],B[n],M,MaxM=0;
    	
    	for(int i=0;i<n;i++)
    	{
    		cin>>A[i];
    	}
    	
    	for(int i=0;i<n;i++)
    	{
    		cin>>B[i];
    	}
    	
    	for(int i=0;i<n-2;i++)
    	{
    		for(int j=0;j<n-2;j++)
    		{
    			if(j>=i && B[j]>=A[i])
    			{
    				M=j-1;
    			}
    			else M=0;
    			
    			if (M>MaxM)
    			{
    				MaxM = M;
    			}
    				
    		}
    	}
    	
    	cout<<MaxM<<endl;
    	
    }
    return 0;
}
