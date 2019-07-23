#include "domain1.h"
#include "node.h"
#include "constraint.h"

int main(int argc, char **argv) {
  Domain theDomain;
  theDomain.theNodes=0;
  theDomain.theConstraints=0;
  theDomain.numNodes=0;
  theDomain.maxNumNodes=0;
  theDomain.numConstraints=0;
  theDomain.maxNumConstraints=0;
  
  domainAddNode(&theDomain, 1, 0.0, 0.0);
  domainAddNode(&theDomain, 2, 1.0, 0.0);
  domainAddNode(&theDomain, 3, 2.0, 0.0);
  domainAddNode(&theDomain, 4, 1.0, 1.0);
  printf("Nodes added.\n");
  
  domainAddConstraint(&theDomain, 1, 1, 1, 0);
  domainAddConstraint(&theDomain, 2, 1, 1, 0);
  domainAddConstraint(&theDomain, 3, 1, 1, 1);
  printf("Constraints added.\n");
  
  domainPrint(&theDomain);

  // get and print singular node
  printf("\nsingular node w/ constraint:\n");
  Node *theNode = domainGetNode(&theDomain, 2);
  nodePrint(theNode);
  Constraint *theConstraint = domainGetConstraint(&theDomain, 2);
  constraintPrint(theConstraint);
}
