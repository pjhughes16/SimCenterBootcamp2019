#include <iostream>
#include "Domain.h"
#include "Node.h"
#include "Constraint.h"

// domain methods ====================================================================================================
Domain::Domain() {
  theNode.empty();
  theConstraint.empty();
}

Domain::~Domain() {
  theNode.empty();
  theConstraint.empty();
}

//void
//Domain::Print(std::ostream &s){
//
//  s << "The Nodes:\n";
//  std::map<int, Node *>::iterator it = theNode.begin();
//  while (it != theNode.end()) {
//      Node *theNode = it->second;
//      theNode->Print(s);
//      it++;
//
//    }
//
//  s << "The Constraints:\n";
//  std::map<int, Constraint *>::iterator it = theConstraint.begin();
//  while (it != theConstraint.end()) {
//      Constraint *theConstraint = it->second;
//      theConstraint->Print(s);
//      it++;
//
//    }
//}

// node methods ====================================================================================================
Node *
Domain::getNode(int tag){
  Node *res = NULL;

  std::map<int, Node *>::iterator it = theNode.find(tag);

  if (it != theNode.end()) {
      Node *theNode = it->second;
      return theNode;
  }
  return res;
}

int
Domain::AddNode(Node *theNod) {
  if (theNode.insert (std::map<int, Node *>::value_type(theNod->GetTag(), theNod)).second == false)
    return false;
  else
    return true;
}

void
Domain::PrintNode(std::ostream &s){
  s << "The Nodes:\n";
  std::map<int, Node *>::iterator it = theNode.begin();
  while (it != theNode.end()) {
      Node *theNode = it->second;
      theNode->Print(s);
      it++;

    }
}

// constraint methods ====================================================================================================
Constraint *
Domain::getConstraint(int tag){
  Constraint *res = NULL;

  // create iterator & iterate over all elements
  std::map<int, Constraint *>::iterator it = theConstraint.find(tag);

  if (it != theConstraint.end()) {
      Constraint *theConstraint = it->second;
      return theConstraint;
  }
  return res;
}

void
Domain::PrintConstraint(std::ostream &s){
  s << "The Constraints:\n";
  std::map<int, Constraint *>::iterator it = theConstraint.begin();
  while (it != theConstraint.end()) {
      Constraint *theConstraint = it->second;
      theConstraint->Print(s);
      it++;

    }
}
//function.insert(std::map<int, int>::value_type(0, 42));
int
Domain::AddConstraint(Constraint *theConstrain) {
  if (theConstraint.insert (std::map<int, Constraint *>::value_type(theConstrain->GetTag(), theConstrain)).second == false)
    return false;
  else
    return true;
}
