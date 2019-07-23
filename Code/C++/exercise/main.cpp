#include <iostream>
#include "Program.h"
#include "Add2.h"
#include "AddVarArgs.h"

int main(int argc, char **argv) {
  Program p1;
  Add2 task1(2,3);
  Add2 task2(2,4);
  AddVarArgs task3(3, 1.1,2.2,3.3);  // first number is number of args
  p1.addTask(&task1);
  p1.addTask(&task2);
  p1.addTask(&task3);
  p1.runTasks(cout);

  p1.addTask(&task1);
  p1.runTasks(cout);

  return 0;
}
