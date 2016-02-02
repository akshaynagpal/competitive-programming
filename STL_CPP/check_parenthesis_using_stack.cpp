#include<iostream>
#include<stack>
#include<string>

using namespace std;

int main(){
    stack <char> myStack;
    string randomCodeString;

    cout<<"Enter code string for which you want to check parenthesis completeness: ";
    cin>>randomCodeString;
    
    for(int i=0;i<randomCodeString.size();i++){

    	if(randomCodeString[i]=='{')
    		myStack.push('{');
    	else if(randomCodeString[i]=='}'){

    		if(!myStack.empty() && myStack.top()=='{')
    			myStack.pop();
    		else
    			myStack.push('}');
    	}
    }
    
    if(myStack.empty())
    	cout<<endl<<"string is balanced!";
    else
    	cout<<endl<<"string is not balanced!";
}