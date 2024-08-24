#include <stdio.h>

#define TABINC 8

int main()
{
	int c, pos, num_space, num_tab;
	
	num_space = num_tab = 0;
	for (pos = 0; (c = getchar()) != EOF; ++pos) {
		if (c == ' ') {
			if (pos % TABINC != 0) {
				++num_space;
			}
			else {
				num_space = 0;
				++num_tab;
			}
		}
		else {
			for ( ; num_tab > 0; --num_tab) {
				putchar('\t');
			}
			if (c == '\t') {
				num_space = 0; /* Because it jumps to tab stop if c is '\t' */
			}
			for ( ; num_space > 0; --num_space) {
				putchar(' ');
			}
			putchar(c);
			if (c == '\n') {
				pos = 0;
			}
			else if (c == '\t') {
				pos = pos + (TABINC - (pos - 1) % TABINC) - 1;	
			}
		}
	}
}
