#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
	for (int i = 0; i < 1000; i++) {
		char initial = (char)('A' + rand() % 3);
		cout << initial << endl;
		char door;
		int status;
		cin >> door >> status;
		if (status == 1) {
			cout << door << endl;
		} else {
			cout << (char)(initial ^ door ^ 'A' ^ 'B' ^ 'C') << endl;
		}
		cin >> status >> door;
	}
}
