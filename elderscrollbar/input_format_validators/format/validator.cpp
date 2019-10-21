#include "validator.h"
#include <regex>

regex text_format("[a-zA-Z][a-zA-Z ]{0,78}[a-zA-Z]|[a-zA-Z]");

void run() {
	Int(3, 200);
	Space();
	Int(3, 200);
	Space();
	Int(0, 30000);
	Space();
	int n = Int(1, 30000);
	Endl();

	for (int i = 0; i < n; ++i) {
		string line = Line();
		assert( regex_match(line, text_format));
	}
}
