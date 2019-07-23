#ifndef _PROGRAM
#define _PROGRAM

#include <iostream>
#include <queue>

class Task;

class Program {
 public:
  Program();
  ~Program();
  int addTask(Task *);
  int runTasks(ostream &s);
 private:
  std::queue<Task *>taskQueue;
};

#endif
