#ifndef _ADD2
#define _ADD2

#include "Task.h"

class Add2 :public Task {
 public:
  Add2(double a, double b);
  ~Add2();
  int runTask(void);
  
  void Print(ostream &s);

 private:
  double a, b, c;
};

#endif
