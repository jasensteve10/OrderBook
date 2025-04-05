## part 1 of the code

# This file contains the classes used in the project

# The classes are: Task

class Task:  

    ## static counter to keep track of the number of tasks created
    counter = 1

    ## constructor to initialize the task object
    def __init__(self , description, programmer, workload):
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = False
        self.id = Task.counter
        Task.counter += 1
    
    ## setter method to set finished to True
    def mark_finished(self):
        self.finished = True
    
    ## returns True if return FINISHED, NOT FINISHED otherwise
    def is_finished(self):
        if self.finished:
            return "FINISHED"
        else:
            return "NOT FINISHED"


    def __str__(self):
        return f"{self.id}: {self.description}({self.workload} hours), programmer {self.programmer} {self.is_finished()}"
