#include <stdio.h>

#define OUT 0
#define IN 1
#define MAXWORD 11
#define MAXHIST 15

int main() {
	int c, i, state, len;
	int wc, maxvalue, overflow;
	int wl[MAXWORD];

	/* 各変数の数値を0に設定する */
	state = OUT;
	wc = overflow = 0;
	for (i = 1; i < MAXWORD; ++i) {
		wl[i] = 0;
	}
	
	while ((c = getchar()) != EOF) {
		if (c == '\n' || c == '\t' || c == ' ') {
			if (wc > 0 && wc < MAXWORD)
				++wl[wc];
			else if (c >= MAXWORD) {
				++overflow;
			}
			state = OUT;
			wc = 0; 
		}
		else if (state == OUT) {
			wc = 1;
			state = IN;
		}
		else {
			++wc;
		}
	}
	maxvalue = 0;
	/* 単語の長さの最大値を求める */	
	for (i = 1; i < MAXWORD; ++i) {
		if (wl[i] > maxvalue)
			maxvalue = wl[i];
	}

	for (i = 1; i < MAXWORD; ++i) {
		printf("%2d - %2d\n", i, wl[i]);
		if (wl[i] > 0) {
			if ((len = wl[i] * MAXHIST / maxvalue) <= 0) {
				len = 1;	
			}
		}
		else {
			len = 0;
		}
		while (len > 0) {
			putchar('*');
			--len;
		}
		putchar('\n');
	}
	printf("number of overflow is %d\n", overflow);
}
