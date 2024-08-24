#include <stdio.h>

int main() {
	int c, i, nwhite, nother;
	int ndigit[10];

	/* 各変数の数値を0に設定する */
	nwhite = nother = 0;
	for (i = 0; i < 10; ++i) {
		ndigit[i] = 0;
	}

	while ((c = getchar()) != EOF) {
		if (c >= '0' && c <= '9') {
			++ndigit[c - '0'];
		}
		else if (c == ' ' || c == '\n' || c == '\t') {
			++nwhite;	
		}
		else {
			++nother;
		}
	}
	/* 各変数の出現回数を出力する  */
	for (i = 0; i < 10; ++i) {
		printf("%2d count: %2d\n", i, ndigit[i]);
	}
	printf("%d %d\n", nwhite, nother);
}
