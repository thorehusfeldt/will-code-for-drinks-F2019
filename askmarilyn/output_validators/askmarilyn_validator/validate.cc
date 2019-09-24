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
    // where == 1,2,3: always places drink behind door where

    int ctr = 0;
    for (int r = 0; r < rounds; ++r)
    {
        int drink;
       
	if (where == 0) // random door
		drink = 1 + random() % doors;
	else
		drink = where;
    //    judge_message("Drink is behind door %d\n", drink);
	int first_guess;
	if (!(author_out >> first_guess)) {
            wrong_answer("No door guessed in round %d\n", r+1);
	}
	if (first_guess < 1 || first_guess > doors) {
            wrong_answer("First guess in round %d out of range: %d\n", r+1, first_guess);
        } 
     //   judge_message("Guess %d (1) is %d\n", r + 1, first_guess);
	int hint;
	if (strategy == 0)
	{
		hint = 1 + random() % doors;
		while (hint == drink || hint == first_guess)
			hint = 1 + (hint + 1) % doors;
	}
	if (strategy == 1)
	{
		hint = 1 + random() % doors;
	}
	if (strategy == 2)
	{ 
		hint = drink;
	}
	cout << "Interesting choice. Let me open one door for you.\n";
	if (hint == drink)
	{
		cout << "There is a drink behind door ";
	}
	else
	{
		cout << "There is nothing behind door ";
	}
	cout << hint;
	cout << " .\n";
	cout.flush();

	int second_guess = -1;
	if (!(author_out >> second_guess)) {
            wrong_answer("No 2nd response guessed in round %d\n", r+1);
	}
	if (second_guess == drink)
	{
	    cout << "Enjoy your drink!\n";
	    ctr++;
	}
	else
	{
	    cout << "Bad luck.\n";
	}
	cout << "Rounds: " << r+1 << ". Drinks: " << ctr << ".\n";
	cout.flush();
	judge_message("Score %d: %d\n", r+1, ctr);
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
