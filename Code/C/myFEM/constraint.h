#ifndef _CONSTRAINT
#define _CONSTRAINT 

#include <stdio.h>

typedef struct constraint {
  int tag;
  bool fixity[3];
  struct constraint *next;
} Constraint;

void constraintPrint(Constraint *);
void constraintSetup(Constraint *, int tag, bool fix1, bool fix2, bool fix3);

#endif