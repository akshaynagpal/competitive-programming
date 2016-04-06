#include <iostream>
#include <math.h>
using namespace std;

int checkPrime(long int j){
    long int maxp = sqrt(j);
    for(long int k=2;k<=maxp;k++){
        if(j%k==0)
            return 0;
    }
    return 1;
}

int main() {

    long int n,i,j,a,b;
	cin>>n;
	for(i=0;i<n;i++){
        cin>>a>>b;
        for(j=a;j<=b;j++){
            if(j==1)
                continue;
            else if(j==2){
                cout<<j<<"\n";
            }
            else if(j%2!=0 && checkPrime(j))
                cout<<j<<"\n";
        }
	}
	return 0;
}
