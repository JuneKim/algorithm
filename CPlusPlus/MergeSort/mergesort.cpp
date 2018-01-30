#include <iostream>

using namespace std;

#define TEST
#ifdef TEST
#include <stdio.h>
#define DBG printf
#else
#define DBG
#endif

#define MAXN 100

int arr[MAXN];

int buffer1[MAXN];
int buffer2[MAXN];
void merge(int low, int mid, int high)
{
	int head1, rear1, head2, rear2, curr;
	head1 = rear1 = low;
	for (register int i = low; i <= mid; ++i)
		buffer1[rear1++] = arr[i];
	rear1 = mid;

	head2 = rear2 = mid + 1;
	for (register int i = mid + 1; i <= high; ++i) 
		buffer2[rear2++] = arr[i];
	rear2 = high;

	curr = low;
	/* compare the value of buffer1 and buffer2. this condition will be modified by the requirement */
	while (head1 <= rear1 && head2 <= rear2) {
		if (buffer1[head1] < buffer2[head2]) {
			arr[curr] = buffer1[head1];
			++head1;
			++curr;
		} else {
			arr[curr] = buffer2[head2];
			++head2;
			++curr;
		}
	}	
	/* copy remained item of buffer1 or buffer2 */
	while (head1 <= rear1) {
		arr[curr] = buffer1[head1];
		++head1;
		++curr;
	}

	while (head2 <= high) {
		arr[curr] = buffer2[head2];
		++head2;
		++curr;
	}
}
/*
MergeSort has the complexity of O(nlogn)
*/
void mergeSort(int low, int high)
{
	int mid;
	if (low < high) {
		mid = (low + high) / 2;
		mergeSort(low, mid);
		mergeSort(mid + 1, high);
		merge(low, mid, high);
	}
}

int T;
int N;

int main(int argc, char *argv[])
{
	setbuf(stdout, NULL);
	freopen("input.txt", "r", stdin);

	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		cin >> N;
		for (register int idx = 0; idx < N; idx++) {
			cin >> arr[idx];
		}

		DBG("before \n");
		for (int i = 0; i < N; i++) {
			DBG("%d ", arr[i]);
		}
		DBG("\n");
		mergeSort(0, N - 1);
		DBG("after \n");
		for (int i = 0; i < N; i++) {
			DBG("%d ", arr[i]);
		}
		DBG("\n");

		//cout << "#" << testcase << endl;
	}
}
