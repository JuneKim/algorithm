#ifndef __STACK_H__
#define __STACK_H__

#include <iostream>

using namespace std;

class StackNode {
private:
	int _data;
	StackNode *_prev;
public:
	StackNode() : _data(0), _prev(NULL) {}
	virtual ~StackNode() {}
	void setData(int data) { _data = data; }
	void setPrev(StackNode *ptr) { _prev = ptr; }
	int getData() { return _data;}
	StackNode *getPrev() { return _prev;}
};

class StackInt {
private:
	int _cnt;
	StackNode *_top;
public:
	StackInt() : _cnt(0), _top(NULL) {}
	virtual ~StackInt();
	int pop();
	int push(int data);
	bool isEmpty();
	void display();
};

StackInt::~StackInt()
{
	while (isEmpty() != true) {
		pop();
	}
}

void StackInt::display()
{
	int idx = 0;
	StackNode *ptr = NULL;
	ptr = _top;
	while(!isEmpty()){
		cout << pop() << " ";
	}

}


int StackInt::push(int data)
{
	StackNode *node = new StackNode;
	if (node == NULL) {
		return -1;
	}
	node->setData(data);
	node->setPrev(_top);
	_top = node;
	_cnt++;

	return 0;
}

int StackInt::pop()
{
	if (isEmpty() == true) {
		return 0;
	}

	StackNode *node = _top;

	_cnt--;
	_top = node->getPrev();

	node->setPrev(NULL);

	return node->getData();
}

bool StackInt::isEmpty()
{
	return _cnt == 0 ? true: false;
}

#endif /* __STACK_H__ */
