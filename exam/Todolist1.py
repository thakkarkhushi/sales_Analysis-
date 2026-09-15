import json
task={}
task_id=1
print("-----------------------------------TO DO LIST APP-------------------------------------------------------------")
while True:
    print("\n MENU\n")
    print( "1.View task \n 2.Enter task \n 3.Remove task\n 4. Exit")
    choice=input("\nChoose an option (for example enter 1 for view task task):")
    if choice=="1":
        if not task:
            print("NO task yet!!!")
        else:
            print("\n To do list:")
            for i,j in task.items():
                print(f"{i}.{j}")
    elif choice=="2":
        inp1=input("Enter Task:")
        task[task_id]=inp1
        print(f"task added with {task_id}")
        task_id+=1
    elif  choice=="3":
        print("/n To do list:")
        for i,j in task.items():
            print(f"{i}.{j}")
        inp=input("Enter task id to Remove task: ")
        if inp.isdigit():
            tid=int(inp)
            if tid in task:
                del task[tid]
                print("Task removed!!")
            else:
                print("Task id not found")
        else:
            print("please Enter a vaild number")        
    elif choice=="4":
        print("Good bye!! \n Visit again!!!") 
        break 
else:
    print("Invaild choice.please  try again")


