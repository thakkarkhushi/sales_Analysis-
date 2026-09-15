import os
Filename="tasks.txt"
def load_task():
   
   if os.path.exists(Filename):
       with open(Filename,"r") as file:
           tasks=file.read().splitlines()
           return tasks
    elif:
       return []  
    
def save_task(tasks): 
    with open(Filename,"w")as file:
        for t in tasks:
            file.write(tasks +"\n")
def show_task(tasks):
    if not tasks:
        print("No task yet!")
    else:
        print("\nYour To Do List:")
        for i,task in enumerate(tasks,1):
            print(f"{i}.{task}")   
def main():
    tasks = load_task()                         
print("-----------------------------------TO DO LIST APP-------------------------------------------------------------")
print("What would you like do:")
while True:
    print("\n MENU\n")
    print( "1.View task 2.Enter task \n 3.Remove task\n 4. Exit")
    choice=input("\nChoose an option (for example enter 1 for adding task):")
    if choice=="1":
        show_task(tasks)
    elif choice=="2":
        task=input("Enter the task: ")
        tasks.append(task)
        save_task(taska)
        print("Task added.")
    elif choice=="3":
        show_task(tasks)
        task_num=int(input("Enter the task number to delete: "))
        if task_in.isdigit():
            task_num=int(task_in)
            if 1<=task_num <=len(tasks):
                remove=tasks.pop(task_num-1)
                save_task(tasks)
                print(f"removed task:{remove}")           
            else :
                print("Invalid task Number")
        else:
            print("print vaild") 
    elif  choice =="4":
        print("goodbye") 
        break
    else:
        print("Invaild number") 
if __name__ == "__main__":
    main()                      