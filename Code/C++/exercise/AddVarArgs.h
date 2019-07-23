#ifndef _ADD_VAR_ARGS
#define _ADD_VAR_ARGS
#include "Task.h"

// variable number of args to a function!
// http://www.cplusplus.com/reference/cstdarg/va_arg/

class AddVarArgs :public Task {
 public:
  AddVarArgs(int n, ...);
  ~AddVarArgs();
  int runTask(void);
  
  void Print(ostream &s);

 private:
  double sum;
};

#endif
