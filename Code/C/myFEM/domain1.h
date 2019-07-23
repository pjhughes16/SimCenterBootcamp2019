#include "node.h"
#include "constraint.h"

typedef struct struct_domain {
  Node **theNodes;
  Constraint **theConstraints;
  int numNodes;
  int maxNumNodes;
  int numConstraints;
} Domain;

void domainPrint(Domain *theDomain);

void domainAddNode(Domain *theDomain, int tag, double crd1, double crd2);
void domainPrintNodes(Domain *theDomain);
Node *domainGetNode(Domain *, int nodeTag);

void domainAddConstraint(Domain *theDomain, int tag, bool fix1, bool fix2, bool fix3);
void domainPrintConstraints(Domain *theDomain);
Constraint *domainGetConstraint(Domain *, int nodeTag);
