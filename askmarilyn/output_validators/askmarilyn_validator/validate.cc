#include <utility>
#include <string>
#include <cassert>
#include <cstring>
#include <cmath>
#include "validate.h"

using namespace std;

void check_case() {
    string line;
    /* Get test mode description from judge input file */
    assert(getline(judge_in, line));

    int strategy;
    int rounds = 1000;
    int doors = 3;
    int where;
    sscanf(line.c_str(), "%d %d", &strategy, &where);
    // strategy == 0 : Monty Hall (opens empty door)
    // strategy == 1 : opens random door
    // strategy == 2 : opens door with drink
    // where == 0: puts beer behind random door
    // where == 1,2,3: always places drink behind door behind A, B, C

    int ctr = 0;
    for (int r = 0; r < rounds; ++r)
    {
        unsigned char drink = 'A' + ( (where == 0) ? random() % doors : where - 1);
        unsigned char first_guess;
	author_out >> first_guess;
	if (first_guess < 'A' || first_guess > 'D') {
            wrong_answer("First guess in round %d out of range: %c\n", r+1, first_guess);
        } 
	unsigned char hint;
	switch (strategy) {
		case 0:
			hint = 'A' + random() % doors;
			while (hint == drink || hint == first_guess)
				hint = 'A' + (hint - 'A' + 1) % doors;
			break;
		case 1:
			hint = 'A' + random() % doors;
			while (hint == first_guess)
				hint = 'A' + (hint - 'A' + 1) % doors;
			break;
		case 2:
			hint = drink;
			break;
	}
	cout << hint << ' ' << (hint == drink) << endl;
	cout.flush();

	unsigned char second_guess;
	author_out >> second_guess;
	if (second_guess < 'A' || first_guess > 'D') {
            wrong_answer("Final guess in round %d out of range: %c\n", r+1, first_guess);
        } 
	if (second_guess == drink) ++ctr;
	cout << (second_guess == drink) << ' ' << drink << endl;
	cout.flush();
	//judge_message("Score %d: %d\n", r+1, ctr);
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
