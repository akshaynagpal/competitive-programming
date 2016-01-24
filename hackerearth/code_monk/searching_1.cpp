//https://www.hackerearth.com/code-monk-searching/algorithm/discover-the-monk/
#include <iostream>
using namespace std;

int binary_search(int A[], int n, int x)
{
	int lb=0,ub=n-1,mid;
	
	while(lb<=ub)
	{
		mid=lb+(ub-lb)/2;
		
		if (A[mid]==x) return 1;
		else if(x>A[mid])
		{
			lb=mid+1;
		}
		else ub=mid-1;
	}
	
	return 0;
}
int main()
{
    int n,q,query;
    cin>>n>>q;
    int Arr[n];
    
    for(int i=0;i<n;i++)
    	cin>>Arr[i];

    //sorting the array using Insertion Sort
    for(int i=0;i<n;i++)
    {
    	int temp = Arr[i];
    	int j=i;
    	
    	while(temp<Arr[j-1]&&j>0)
    	{
    		Arr[j]=Arr[j-1];
    		j -= 1;
    	}
    	
    	Arr[j] = temp;
    }
    //sorting done
    
    for(int j=0;j<q;j++)
    {
    	cin>>query;
    	if (binary_search(Arr, n, query)) 
    		cout<<"YES"<<endl;
    	else
    		cout<<"NO"<<endl;
    	
    }
    return 0;
}