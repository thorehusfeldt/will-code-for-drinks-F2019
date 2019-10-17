#include "validator.h"

void run() {
	int maxN = Arg("n");
	int n = Int(1, maxN);
	Endl();
	for (int i = 0; i < n; i++) {
		Int(1, 1000000000);
		if (i < n-1) 
			Space();
	}
	Endl();
	Eof();
}
