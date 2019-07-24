#ifndef _CONSTRAINT
#define _CONSTRAINT

#include <iostream>

class Constraint {
 public:
  Constraint(int tag, bool fix1, bool fix2, bool fix3);
  int GetTag(void); 
  const double *GetFixity();
  void Print(std::ostream &s);
 private:
  int tag;
  double fixity[3];
};

#endif
