#include<iostream>
#include<string>
#include<stack>

using namespace std;

int main(){

	stack <char> myStack;
	string s1;
	
	cin>>s1;

	for(int i=0;i<s1.size();i++){
		myStack.push(s1[i]);
	}

	while(!myStack.empty()){
		cout<<myStack.top();
		myStack.pop();
	}
}