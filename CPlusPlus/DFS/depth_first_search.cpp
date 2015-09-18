/**
 * @maintainer June Kim<infinite.minjune.kim@gmail.com>
 * @brief simple dfs in c++
 * @date 18/09/15
 */

#include <iostream>
#include "stack.h"

using namespace std;

class Graph {
private:
	int _number;
	int **_array;
public:
	Graph(int num = 2);
	~Graph();
	void addEdge(int r1, int r2);
	void depthFirstSearch(int origin, int destination);
	int isConnected(int r1, int r2);
	void displayEdge();
};

Graph::Graph(int num)
{
	int idx, idy;
	if (num < 2) return;

	_number = num;

	_array = new int*[num+1];	
	// two-demension array(num X num)  cf. _array = (int*)malloc(sizeof(int*) * num); _array[idx] = malloc(sizeof(int) * num);
	for (idx = 0; idx < num+1; idx++) {
		_array[idx] = new int[num+1];
	}

	// initialize
	for (idx = 0; idx < num + 1; idx++) {
		for (idy = 0; idy < num + 1; idy++) {
			_array[idx][idy] = 0;
		}
	}
}

Graph::~Graph()
{
	int i = 0;
	if (_number > 0) {
		for (i = 0; i < _number + 1; i++) {
			delete []_array[i];
		}
		delete []_array;
	}
}

void Graph::displayEdge()
{
	int idx, idy;
	for (idx = 1; idx < _number + 1; idx++) {
		for (idy = 1; idy < _number + 1; idy++) {
			cout << " " << _array[idx][idy] << " ";
		}
		cout << endl;
	}
}

int Graph::isConnected(int r1, int r2)
{
	if (r1 == r2) return 1;
	if (r1 < 0 || r1 > _number || r2 < 0 || r2 > _number) return -1;

	return _array[r1][r2] == 1 ? 1: 0;
}

void Graph::addEdge(int r1, int r2)
{
	if (r1 == r2) return;
	if (r1 < 0 || r1 > _number || r2 < 0 || r2 > _number) return;
	_array[r1][r2] = _array[r2][r1] = 1;
}

void Graph::depthFirstSearch(int origin, int destination)
{
#ifdef RECURSIVE
	if (origin == destination)
		return false;
#else
	int idx = 0;
	bool ret = false;
	StackInt *nodes = new StackInt;
	int *visited = new int[_number + 1];	// why 1 added ? disgard 0th index for unambiguous indexing

	for (idx = 0; idx < _number + 1; idx++)
		visited[idx] = 0;

	if (origin == destination) {
		return;
	}
	//displayEdge();
	visited[origin] = true;
	if (origin == destination) return;
	int k = origin;

	while(k == origin || !(ret = nodes->isEmpty())) {
		if (k == destination) {
			nodes->push(k);
			break;
		}

		for (idx = _number; idx > 0; idx--) {
			if (isConnected(k, idx) == 1 && visited[idx] == false) {
				nodes->push(k);
				k = idx;
				visited[idx] = 1;
				break;
			}
		}

		if (idx <= 0) {
			k = nodes->pop();
		}

	}

	cout << "result :" << endl;
	nodes->display();	

	cout << endl;
	delete []visited;
#endif
}

int main(int argc, char *argv[])
{
	Graph path(8);

	path.addEdge(1,2);
	path.addEdge(1,3);
	path.addEdge(1,4);
	path.addEdge(2,5);
	path.addEdge(2,6);
	path.addEdge(4,7);
	path.addEdge(4,8);
	path.addEdge(6,7);
	path.addEdge(7,8);

	path.depthFirstSearch(1,6);

	return 0;
}
