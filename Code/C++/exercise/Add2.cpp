
#include "Add2.h"

Add2::Add2(double first, double second)
  :a(first), b(second), c(0) 
{
  
}
Add2::~Add2() {

}
int 
Add2::runTask(void) {
  c = a+b;
  return 0;
}
  
void 
Add2::Print(ostream &s) {
  s << c << "\n";
}

