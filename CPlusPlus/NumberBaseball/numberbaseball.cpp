#include <iostream>
#include "numberbaseball.h"

using namespace std;

//#define TEST
#ifdef TEST
#define DBG printf
#else
#define DBG
#endif

#define CANDIDATES_MAX 720 // 10P3 = 10 * 9 * 8
#define QUERY_MAX 1000000

int totalCnt;
bool isCandidateAvailable[CANDIDATES_MAX];
int candidates[DIGIT_NUM][CANDIDATES_MAX];

extern Result query(int *guessWhat);

/**
depth : current position of search
n : target postion
*/
bool visit[NUMBER_MAX];
int permArr[DIGIT_NUM];
void perm(int depth, int n)
{
	if (depth == n) {
		/* end of searching perm arr */
		for (int n = 0; n < DIGIT_NUM; ++n) {
			candidates[n][totalCnt] = permArr[n];
			isCandidateAvailable[totalCnt] = true;
		}
		totalCnt++;		
		return;
	}
	for (int idx = 0; idx < NUMBER_MAX; ++idx) {
		if (visit[idx] == 0) {
			visit[idx] = 1;
			permArr[depth] = idx;
			perm(depth + 1, n);
			visit[idx] = 0;
		}
	}
}

int process(int *guessNum)
{
	int guessWhat[DIGIT_NUM];
	int searchIdx = 0;
	int queryCnt = 0;
	int guessWhatNumCnt[NUMBER_MAX] = {0, };
	Result queryResult;
	Result canResult;
	//init code
	for (register int idx = 0; idx < CANDIDATES_MAX; ++idx) {
		isCandidateAvailable[idx] = false;	
	}

	perm(0, DIGIT_NUM);
	do {
		for (int idx = 0; idx < DIGIT_NUM; ++idx) {
			guessWhat[idx] = candidates[idx][searchIdx];
		}
		queryCnt++;
		queryResult = query(guessWhat);
		if (queryResult.strikes == DIGIT_NUM) {
			for (int n = 0; n < DIGIT_NUM; ++n) {
				guessNum[n] = guessWhat[n];
			}
			
			return queryCnt;
		}
		isCandidateAvailable[searchIdx] = false;
		searchIdx = -1;
		for (int idj = 0; idj < NUMBER_MAX; ++idj)
			guessWhatNumCnt[idj] = 0;

		for (int n = 0; n < DIGIT_NUM; ++n) {
			guessWhatNumCnt[guessWhat[n]]++;
		}

		for (int canIdx = 0; canIdx < totalCnt; ++canIdx) {
			if (isCandidateAvailable[canIdx] == false) continue;
			canResult.strikes = 0;
			canResult.balls = 0;
			for (int n = 0; n < DIGIT_NUM; ++n) {
				if (candidates[n][canIdx] == guessWhat[n]) {
					canResult.strikes++;
				} else if (guessWhatNumCnt[candidates[n][canIdx]] > 0) {
					canResult.balls++;
				}
			}
			if (queryResult.strikes != canResult.strikes || queryResult.balls != canResult.balls) {
				isCandidateAvailable[canIdx] = false;
			} else if (searchIdx == -1) {
				searchIdx = canIdx;
			}
		}
	} while(queryCnt < QUERY_MAX && searchIdx > 0);
	
	return queryCnt;
}

// makes subsets

