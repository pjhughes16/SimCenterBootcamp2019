#include <iostream>
#include "Domain.h"
#include "Node.h"
#include "Constraint.h"

int main(int argc, char **argv) {

  // generate nodes
  Node *node1 = new Node(1,0.0,0.0);
  Node *node2 = new Node(2,1.0,0.0);
  Node *node3 = new Node(3,2.0,0.0);
  Node *node4 = new Node(4,1.0,1.0);
  std::cout << "Nodes generated.\n";

  // generate constraints
  Constraint *constraint1 = new Constraint(1,1,1,0);
  Constraint *constraint2 = new Constraint(2,1,1,0);
  Constraint *constraint3 = new Constraint(3,1,1,1);
  std::cout << "Constraints generated.\n";

  // generate empty domain
  Domain theDomain;
  std::cout << "Empty domain generated.\n";

  // add nodes to the domain
  theDomain.AddNode(node1);
  theDomain.AddNode(node2);
  theDomain.AddNode(node3);
  theDomain.AddNode(node4);
  std::cout << "Nodes added to the domain.\n";

  // add constraints to the domain
  theDomain.AddConstraint(constraint1);
  theDomain.AddConstraint(constraint2);
  theDomain.AddConstraint(constraint3);
  std::cout << "Constraints added to the domain.\n";

  theDomain.PrintNode(std::cout);
  theDomain.PrintConstraint(std::cout);

  std::cout << "Individual node & constraint:\n";
  Node *theNode = theDomain.getNode(2);
  if (theNode != 0)
    theNode->Print(std::cout);
  Constraint *theConstraint = theDomain.getConstraint(2);
  if (theConstraint != 0)
    theConstraint->Print(std::cout);

}
