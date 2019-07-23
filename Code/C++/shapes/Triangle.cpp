#include <Triangle.h>

Triangle::~Triangle() {
  std::cout << "Triangle Destructor\n";
}

Triangle::Triangle(double b, double h) {
  base = b;
  height = h;
}

double
Triangle::GetArea(void) {
  return (0.5 * base * height);
}