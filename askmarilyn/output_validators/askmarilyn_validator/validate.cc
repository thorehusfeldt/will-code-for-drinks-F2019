#include <utility>
#include <string>
#include <cassert>
#include <cstring>
#include <cmath>
#include "validate.h"

using namespace std;

class miniPRG {
	unsigned int _seed = 0;
	int _a = 1016404597;
	int _c = 12345;
	int _m = 2147483648;

	public:
	int myrnd() {
		_seed = (_a * _seed + _c ) % _m;
		return  _seed;
	}
};

void check_case() {
	string line;
	/* Get test mode description from judge input file */
	assert(getline(judge_in, line));


	miniPRG R;
	int strategy;
	int rounds = 1000;
	int doors = 3;
	int where;
	unsigned char drink = 'A';
	sscanf(line.c_str(), "%d %d", &strategy, &where);
	// strategy == 0 : Monty Hall (opens empty, other door)
	// strategy == 1 : Random (opens random other door)
	// strategy == 2 : Helpful (opens door with drink, if possible, otherwise random)
	// where == 0: puts beer behind random door
	// where == 1,2,3: always places drink behind door behind A, B, C
	// where == 4: rotates deterministically A, B, C, A, B, C ...

	int ctr = 0;
	for (int r = 0; r < rounds; ++r)
	{
		switch(where) {
			case 0:
				drink = 'A' + R.myrnd() % doors; 
				break;
			case 1:
			case 2:
			case 3:
				drink = 'A' + where - 1;
				break;
			case 4:
				drink = 'A' + (drink + 1 - 'A') % doors;
				break;
		}

		unsigned char first_guess;
		if (!(author_out >> first_guess)) {
			wrong_answer("No first door guessed in round %d\n", r+1);
		}
		if (first_guess < 'A' || first_guess >= 'A' + doors) {
			wrong_answer("First guess in round %d out of range: %c\n", r+1, first_guess);
		} 
		unsigned char hint;
		switch (strategy) {
			case 0:
				do {
					hint = 'A' + R.myrnd() % doors;
				} while (hint == drink || hint == first_guess);
				break;
			case 1:
				do {
					hint = 'A' + R.myrnd() % doors;
				} while (hint == first_guess);
				break;
			case 2:
				if (drink != first_guess) {
					hint = drink;
				}
				else {
					do {
						hint = 'A' + R.myrnd() % doors;
					} while (hint == first_guess);
				}
				break;
		}
		assert(hint != first_guess);
		cout << hint << ' ' << (hint == drink) << endl;

		unsigned char second_guess;
		if (!(author_out >> second_guess)) {
			wrong_answer("No final door guessed in round %d\n", r+1);
		}
		if (second_guess < 'A' || second_guess >= 'A' + doors) {
			wrong_answer("Final guess in round %d out of range: %c\n", r+1, second_guess);
		} 
		if (second_guess == drink) ++ctr;
		cout << (second_guess == drink) << ' ' << drink << endl;
	}
	if  (ctr < 600) // error prob. < .0001
		wrong_answer("Too few drinks\n");

	return;
}

int main(int argc, char **argv) {
	init_io(argc, argv);

	check_case();

	/* Check for trailing output. */
	string trash;
	if (author_out >> trash) {
		wrong_answer("Trailing output\n");
	}

	/* Yay! */
	accept();
}
