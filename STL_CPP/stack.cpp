#include<iostream>
#include<stack>

using namespace std;

int main(){
    stack <int> myStack;
    
    for(int i=0;i<5;i++){
        myStack.push(i);
    }
    
    cout<<"size of myStack is: "<<myStack.size()<<endl;
    if(!myStack.empty()){
        cout<<"top element of stack is"<<myStack.top()<<endl;
    }
    
    if(myStack.empty()){
        cout<<"myStack is empty!"<<endl;
    }
    else{
        cout<<"myStack is not empty!"<<endl;
    }
    
}