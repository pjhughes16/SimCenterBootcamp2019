
#include "AddVarArgs.h"
#include <stdarg.h>

AddVarArgs::AddVarArgs(int n, ...)
{
  int i;
  double val;
  va_list vl;
  va_start(vl,n);
  sum=va_arg(vl,double);
  for (i=1;i<n;i++) {
    double val = va_arg(vl,double);
    sum += val;
  }
  va_end(vl);  
}
AddVarArgs::~AddVarArgs() {

}
int 
AddVarArgs::runTask(void) {
  // already done
  return 0;
}
  
void 
AddVarArgs::Print(ostream &s) {
  s << sum << "\n";
}

