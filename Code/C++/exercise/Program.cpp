#include <stdio.h>
#include "Program.h"
#include "Task.h"

Program::Program() {

}

Program::~Program() {

}

int 
Program::addTask(Task *theTask)
{
  taskQueue.push(theTask);
  return 0;
}
int 
Program::runTasks(ostream &s)
{
  while (!taskQueue.empty()) {
      Task *theTask = taskQueue.front();
      theTask->runTask();
      theTask->Print(s);
      taskQueue.pop();
  }
  return 0;
}
