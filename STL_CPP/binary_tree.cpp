#include<iostream>

using namespace std;

struct node
{
	int data;
	struct node *left;
	struct node *right;
};

static int search_tree(struct node *node,int target){

	if (node==NULL){
		return false;
	}

	else{
		if(target == node->data) return(true);
		else{
			if(target<node->data) return search_tree(node->left,target);
			else return search_tree(node->right,target);
		}
	}
}

struct node* NewNode(int data){
	struct node *node = new(struct node);
	node->data = data;
	node->left= NULL;
	node->right= NULL;

	return node;
}

struct node* insert(struct node *node,int data){
	if(node==NULL){
		return NewNode(data);
	}
	else{
		if(data <= node->data) node->left = insert(node->left,data);
		else node->right = insert(node->right,data);

		return node;
	}
}

int main(){
	node *root;
	insert(root,1);
	return 0;
}
