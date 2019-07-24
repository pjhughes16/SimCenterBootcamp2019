#ifndef _DOMAIN
#define _DOMAIN

#include "Domain.h"
#include <map>

class Node;
class Constraint;

class Domain {
 public:
  Domain();
  ~Domain();

  //void Print(std::ostream &s);

  Node *getNode(int tag);
  int AddNode(Node *theNode);
  void PrintNode(std::ostream &s);

  Constraint *getConstraint(int tag);
  int AddConstraint(Constraint *theConstraint);
  void PrintConstraint(std::ostream &s);

 private:
  std::map<int, Node *>theNode;
  std::map<int, Constraint *>theConstraint;
};

#endif
