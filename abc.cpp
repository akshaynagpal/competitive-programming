#include<iostream>
#include<cmath>

using namespace std;

long int calc_next(long int pressed_keys[], long int k, long int m, int n){
	int summ = 0;
	for(int i=1;i<n+1;i++){
		summ += pow(-1,i+1) * pressed_keys[k-i];
	}
	long int temp = summ%m;
	
	if(temp >= 0) return temp;
	else return temp+m;
}

int main(){
	int num_test,n;
	long int m,z,current_length;
	long int *pressed_keys;
	
	cin>>num_test;

	for(int j=0;j<num_test;j++){
		cin>>n>>m>>z;
	
	pressed_keys = new long int[z+1];

	for(int k=0;k<n;k++){
		cin>>pressed_keys[k];
	}
	current_length = n;
	while(current_length!=z+1){
		pressed_keys[current_length] = calc_next(pressed_keys,current_length,m,n);
		current_length += 1;
	}
	cout<<pressed_keys[current_length-1]<<endl;
	}
	return 0;
}