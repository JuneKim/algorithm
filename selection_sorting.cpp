#include <iostream>

using namespace std;

void swap (int *a, int *b)
{
		int tmp = *a;
		*a = *b;
		*b = tmp;
}

void print_array(int arr[], int num)
{
		int i = 0;
		for (i = 0; i < num; i++) {
				cout << arr[i] << " ";
		}
		cout << endl;
}

void selection_sort (int in[], int num)
{
		int i, j;
		int min_idx;

		for (i = 0; i < num; i++){
				min_idx = i;
				for (j = i+1; j < num; j++) {
						if (in[j] < in[min_idx]) min_idx = j;
				}
				swap(&in[i], &in[min_idx]);
		}
}

int main()
{
		int input[] = {2, 13, 22, 3, 4, 5, 10,7 ,8};
		int count = sizeof(input)/sizeof(int);
		cout << "before sorting" << endl;
		print_array(input, count);
		selection_sort(input, count);
		cout << "after sorting" << endl;
		print_array(input, count);
		return 0;
}
