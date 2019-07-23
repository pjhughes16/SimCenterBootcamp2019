#include <stdio.h>
#include <omp.h>
#include <time.h>

int main() {
	int nStep = 0;
	printf("How many steps? "); // request number of steps
	scanf("%d",&nStep); // read number of steps
	double dx = 1.0/nStep; // finite increment length
	double x = 0; // initialize the x coordinate
	double pi = 0; // initialize pi
	double start = omp_get_wtime(); // set the starting time
	for (int i = 0; i < nStep; i++) {
		x = (i+0.5) * dx; // increment x
		pi += ( (4.0/(1.0+(x*x))) * dx ); // increment pi
	}
	printf("pi = %.15f in %.4e sec\n",pi,omp_get_wtime()-start); // print pi and current time
	return 0;
}
