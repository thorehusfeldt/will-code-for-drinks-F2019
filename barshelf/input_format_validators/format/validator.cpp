#include "validator.h"

void run() {
	int n = Int(1, Arg("n"));
	Endl();
	SpacedInts(n, 1, 1'000'000'000);
}
