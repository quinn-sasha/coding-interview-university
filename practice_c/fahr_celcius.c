#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

/*f = 0, 20, ..., 300に対してせっしかし対応表を作成する */
float fahr_to_celcius(int fahr);

int main()
{
	int i;

	for (i = LOWER; i <= UPPER; i = i + STEP) 
		printf("%3.0d\t\%6.1f\n", i, fahr_to_celcius(i));
	
}

float fahr_to_celcius(int fahr)
{
	float celcius;

	celcius = (5.0 / 9.0) * (fahr - 32.0);
	return celcius;
}
