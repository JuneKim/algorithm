#include <iostream>
#include <stdio.h>

int sample[] = {4, 2, 6, 7, 10};

void powerSet(int arr[], int n, int depth)
{
	if (n == depth) {
		printf("{");
		for (int i = 0; i < n; i++) {
			if (arr[i] == 1) printf("%d ", sample[i]); 
		}
		printf("}\n");
		return;
	}

	arr[depth] = 1;
	powerSet(arr, n, depth+1);
	arr[depth] = 0;
	powerSet(arr, n, depth + 1);
}

int main(int argc, char *argv[])
{
	int arr[100] = {0, };
//	freopen("input.txt", "r", stdin);

	powerSet(arr, sizeof(sample)/sizeof(int), 0);

	return 0;	
}
