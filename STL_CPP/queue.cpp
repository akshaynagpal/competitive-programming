#include<iostream>
#include<queue>

using namespace std;

int main(){
    
    queue <int> myQueue;

    for(int i=0;i<10;i++){
        myQueue.push(i);
    }

    while(!myQueue.empty()){
        cout<<myQueue.front()<<endl;
        myQueue.pop();
    }
}
