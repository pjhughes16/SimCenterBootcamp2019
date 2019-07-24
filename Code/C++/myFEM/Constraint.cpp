#include "Constraint.h"

Constraint::Constraint(int id, bool fix1, bool fix2, bool fix3)
  :tag(id)
{
  fixity[0] = fix1;
  fixity[1] = fix2;
  fixity[2] = fix3;
}

int
Constraint::GetTag(void) {
  return tag;
}

const double *
Constraint::GetFixity() {
  return fixity;
}

void 
Constraint::Print(std::ostream &s){
  s << "Node: " << tag;
  s << " Fixity: " << fixity[0] << " " << fixity[1] << " " << fixity[2] << "\n";
}

