#include <stdio.h>

int main() {
	char c;
	
	c = getchar();
	if ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'))
		printf("%c is alphabet\n", c);
	else {
		printf("%c is not alphabet\n", c);
	}
}
