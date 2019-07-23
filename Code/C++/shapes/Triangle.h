#ifndef _TRIANGLE
#define _TRIANGLE

#include "Shape.h"

class Triangle: public Shape {
 public:
  Triangle(double b, double h);
  ~Triangle();
  double GetArea(void);

 private:
  double base;
  double height;
};

#endif // _TRIANGLE
  
