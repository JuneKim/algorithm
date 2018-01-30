#include <iostream>
#include "numberbaseball.h"

using namespace std;

int expect[DIGIT_NUM];
int numCnt[NUMBER_MAX];

int T;

extern int process(int *guessNum);

bool isValid(int *guessNum)
{
	int cntArr[NUMBER_MAX] = {0, };
	for (int idx = 0; idx < DIGIT_NUM; ++idx) {
		if (guessNum[idx] < 0 || guessNum[idx] > 9 || cntArr[guessNum[idx]] > 0) return false;
		cntArr[guessNum[idx]]++;
	}

	return true;
}

Result query(int *guessNum) {
	Result ret = { -1, -1};

	if (!isValid(guessNum)) {
		return ret;
	}

	ret.strikes = 0;
	ret.balls = 0;

	for (int idx = 0; idx < DIGIT_NUM; ++idx) {
		if (expect[idx] == guessNum[idx]) {
			ret.strikes++;
		} else if (numCnt[guessNum[idx]] > 0) {
			ret.balls++;	
		}
	}

	return ret;
}

int main(int argc, char *argv[])
{
	char ch;
	int ret = 0;
	bool isFailed = false;
	int candidate[DIGIT_NUM];
	freopen("input.txt", "r", stdin);
	setbuf(stdout, NULL);

	cin >> T;
	for (int testcase = 1; testcase <= T; ++testcase) {
		// init code
		isFailed = false;
		for (int n = 0; n < NUMBER_MAX; ++n) {
			numCnt[n] = 0;
		}

		for (int idx = 0; idx < DIGIT_NUM; ++idx) {
			do scanf("%c", &ch); while (ch < '0' || ch > '9');
			expect[idx] = ch - '0';
			numCnt[expect[idx]]++;
		}

		ret = process(candidate);
		if (!isValid(candidate)) isFailed = true;
		else {
		}

		cout << "#" << testcase << " " << ret << " " << (isFailed == true ? "Failed":"Success") << endl;
	}
	return 0;
}
