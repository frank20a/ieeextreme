#include <iostream>

using namespace std;

struct Node{
	int name = -1;			//node name
	Node *children [10000];	//children stack
	int ch = 0;				//children stack pointer
	bool visited = false;	//all nodes initially unvisited
};

bool solve(*Node root){
	cout << root->visited << " ";
	if (root->visited) {
		cout << "checking node " << root->name << " loop found" << endl;
		return true;
	}
	
	root->visited = true;
	for (int i = 0; i < root.ch; i++){
		cout << "checking node " << root.name << " redirect to " << root.children[i]->name << endl;
		if (solve(*root.children[i])) return true;
	}
	cout << endl;
	
	return false;
}

int main() {
    int t, n, m, a, b;
    cin >> t;
    
    for (int i = 0; i < t; i++){
    	cin >> n >> m;
    	    	
		//Data reading
    	Node *nodes = new Node[1000];					//Create array of nodes
    	for (int j = 0; j < n; j++) nodes[j].name = j;	//initialise nodes
		for (int j = 0; j < m; j++){
			cin >> a >> b;
			nodes[a].children[nodes[a].ch] = nodes + b;	//Create vertices
			nodes[a].ch++;								//Update children stack pointer
		}
		
		//if (m > n) cout << 1 << endl;
		//else{
			//Begin DFS Search for loops
			bool res = false;
			for (int j = 0; j < n; j++){
				if (!nodes[j].visited) res = solve (nodes[j]);
				if (res) break;
			}
			cout << res << endl;
		//}
		delete[] nodes;
	}
}
