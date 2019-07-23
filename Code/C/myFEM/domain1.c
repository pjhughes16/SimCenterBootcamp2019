#include <stdio.h>
#include <stdlib.h>
#include "domain1.h"
#include "node.h"
#include "constraint.h"

// domain methods ====================================================================================================
void domainPrint(Domain *theDomain) {
  printf("The Nodes:\n");
  domainPrintNodes(theDomain);
  printf("The Constraints:\n");
  domainPrintConstraints(theDomain);
}

// node methods ====================================================================================================
void domainAddNode(Domain *theDomain, int tag, double crd1, double crd2) {

  // create the new node
  Node *theNextNode = (Node *)malloc(sizeof(Node));
  nodeSetup(theNextNode, tag, crd1, crd2);

  // get size of current array and max size
  int numNodes = theDomain->numNodes;
  int maxNumNodes = theDomain->maxNumNodes;

  // if current size = maxSize, we need to increase storage capacity
  if (numNodes == maxNumNodes) {
    Node **theNextNodes = (Node **)malloc((maxNumNodes+10)*sizeof(Node*));
    for (int i=0; i<numNodes; i++) 
      theNextNodes[i] = theDomain->theNodes[i];
    for (int i=numNodes; i<maxNumNodes+10; i++)
      theNextNodes[i] = 0;
    if (maxNumNodes != 0)
      free(theDomain->theNodes);
    theDomain->maxNumNodes = maxNumNodes+10;
    theDomain->theNodes= theNextNodes;
  }

  // add the node
  theDomain->theNodes[numNodes] = theNextNode;
  theDomain->numNodes++;
}

void domainPrintNodes(Domain *theDomain) {
  int numNodes = theDomain->numNodes;
  for (int i=0; i<theDomain->numNodes; i++)
    nodePrint(theDomain->theNodes[i]);
}

Node *domainGetNode(Domain *theDomain, int nodeTag) {
  int numNodes = theDomain->numNodes;
  for (int i=0; i<numNodes; i++) {
    Node *theCurrentNode = theDomain->theNodes[i];
    if (theCurrentNode->tag == nodeTag) {
      return theCurrentNode;
    } 
  }
  return NULL;
}

// constraint methods ====================================================================================================
void domainAddConstraint(Domain *theDomain, int tag, bool fix1, bool fix2, bool fix3) {

  // create the new constraint
  Constraint *theNextConstraint = (Constraint *)malloc(sizeof(Constraint));
  constraintSetup(theNextConstraint, tag, fix1, fix2, fix3);

  // get size of current array and max size
  int numConstraints = theDomain->numConstraints;
  int maxNumConstraints = theDomain->maxNumConstraints;

  // if current size = maxSize, we need to increase storage capacity
  if (numConstraints == maxNumConstraints) {
    Constraint **theNextConstraints = (Constraint **)malloc((maxNumConstraints+10)*sizeof(Constraint*));
    for (int i=0; i<numConstraints; i++) 
      theNextConstraints[i] = theDomain->theConstraints[i];
    for (int i=numConstraints; i<maxNumConstraints+10; i++)
      theNextConstraints[i] = 0;
    if (maxNumConstraints != 0)
      free(theDomain->theConstraints);
    theDomain->maxNumConstraints = maxNumConstraints+10;
    theDomain->theConstraints= theNextConstraints;
  }

  // add the constraint
  theDomain->theConstraints[numConstraints] = theNextConstraint;
  theDomain->numConstraints++;
}

void domainPrintConstraints(Domain *theDomain) {
  int numConstraints = theDomain->numConstraints;
  for (int i=0; i<theDomain->numConstraints; i++)
    constraintPrint(theDomain->theConstraints[i]);
}

Constraint *domainGetConstraint(Domain *theDomain, int nodeTag) {
  int numConstraints = theDomain->numConstraints;
  for (int i=0; i<numConstraints; i++) {
    Constraint *theCurrentConstraint = theDomain->theConstraints[i];
    if (theCurrentConstraint->tag == nodeTag) {
      return theCurrentConstraint;
    } 
  }
  return NULL;
}
