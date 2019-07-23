#include <stdio.h>
#include "constraint.h"
// #include <stdbool.h>

void constraintPrint(Constraint *theConstraint){
  printf("Node: %d ", theConstraint->tag);
  printf("Fixity: %d %d %d ", theConstraint->fixity[0], theConstraint->fixity[1], theConstraint->fixity[2]);
}

void constraintSetup(Constraint *theConstraint, int tag, bool fix1, bool fix2, bool fix3) {
  theConstraint->tag = tag;
  theConstraint->fixity[0] = fix1;
  theConstraint->fixity[1] = fix2;
  theConstraint->fixity[2] = fix3;
  theConstraint->next = NULL;
}