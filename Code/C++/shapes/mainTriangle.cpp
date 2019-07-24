#include "Triangle.h"
#include <iostream>
#include <fstream>

int main(int argc, char **argv) {
  Triangle theTriangle(12.0,5.0);
  theTriangle.PrintArea(std::cout);
 std::ofstream theFile;
 theFile.open("triFile.txt");
 theTriangle.PrintArea(theFile);
 theFile.close();
  return 0;
};
