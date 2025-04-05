
from Classes import Task

## testing the Task class
def test_task_class():
    # Test Part 1
    t1 = Task("program hello world", "Eric", 3) # calling the constructor
    print(t1.id, t1.description, t1.programmer, t1.workload)

    print(t1) # printing the string representation of the object
    #print(t1.__str__()) # to verify the __str__ method
    print(t1.finished) # printing the finished attribute


    t1.mark_finished() # calling the mark_finished method
    print(t1)
    print(t1.finished) # printing the return value of the is_finished method

    print("--------" * 20)
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)

    print(t2)
    print(t3)
    
        
if __name__ == "__main__":
    test_task_class()