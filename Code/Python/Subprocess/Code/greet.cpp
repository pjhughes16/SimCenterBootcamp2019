#include <iostream>
#include <string>

using namespace std;

int main() {

   string firstname;
   string lastname;

   cout << "First name: ";
   cin >> firstname;

   cout << "Last name:  ";
   cin >> lastname;
   cout << endl;

   cout << "Hello, ";
   cout << firstname << " " << lastname;
   cout << "!" << endl;
}


