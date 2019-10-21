#include <utility>
#include <string>
#include <cassert>
#include <cstring>
#include <cmath>
#include "validate.h"

using namespace std;

class miniPRG {
	unsigned int _seed = 0;
	unsigned int _a = 1016404597;
	unsigned int _c = 12345;

	public:
	int myrnd() {
		_seed = (_a * _seed + _c );
		return (int) (_seed >> 1);
	}
};

int check_case() {
	string line;
	/* Get test mode description from judge input file */
	assert(getline(judge_in, line));


	miniPRG R;
	int strategy;
	int rounds = 1000;
	int doors = 3;
	int where;
	char drink = 'A';
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
				drink = (char) ('A' + R.myrnd() % doors);
				break;
			case 1:
			case 2:
			case 3:
				drink = (char) ('A' + where - 1);
				break;
			case 4:
				drink = (char) ('A' + (drink + 1 - 'A') % doors);
				break;
		}

		char first_guess;
		if (!(author_out >> first_guess)) {
			author_message("You must begin round %d by guessing a door", r+1);
			wrong_answer("Round %d(1): No door guessed", r+1);
		}
		if (first_guess < 'A' || first_guess >= 'A' + doors) {
			author_message("Your guess must be a door, such as A");
			wrong_answer("Round %d(1): Invalid door name: %c", r+1, first_guess);
		} 
		char hint;
		switch (strategy) {
			case 0:
				do {
					hint = (char) ('A' + R.myrnd() % doors);
				} while (hint == drink || hint == first_guess);
				break;
			case 1:
				do {
					hint = (char) ('A' + R.myrnd() % doors);
				} while (hint == first_guess);
				break;
			case 2:
				if (drink != first_guess) {
					hint = drink;
				}
				else {
					do {
						hint = (char) ('A' + R.myrnd() % doors);
					} while (hint == first_guess);
				}
				break;
		}
		assert(hint != first_guess);
		cout << hint << ' ' << (hint == drink) << endl;

		char second_guess;
		if (!(author_out >> second_guess)) {
			author_message("You must give me a final guess in round %d",r+1);
			wrong_answer("Round %d(2): No door guessed", r+1);
		}
		if (second_guess < 'A' || second_guess >= 'A' + doors) {
			author_message("Your guess must be a door, such as A");
			wrong_answer("Round %d(2): Invalid door name: %c", r+1, second_guess);
		} 
		if (second_guess == drink) ++ctr;
		cout << (second_guess == drink) << ' ' << drink << endl;
	}
	if  (ctr < 600) { // error prob. < .0001
	 	author_message("%d drinks in 1000 rounds. Too bad.", ctr);
		wrong_answer("Too few drinks: %d", ctr);
	}

	return ctr;
}

int main(int argc, char **argv) {
	init_io(argc, argv);

	int res = check_case();

	/* Check for trailing output. */
	string trash;
	if (author_out >> trash) {
	 	author_message("You won't stop talking!");
		wrong_answer("Trailing output");
	}

	/* Yay! */
	author_message("Congratulations! You got %d drinks", res);
	accept();
}
