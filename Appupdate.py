
# Main Menu Index
add_task= "1" 
view_tasks = "2"
mark_complete= "3"
delete_task = "4"
quit = "5"

#List Index
full_list= [] 
checkoff_list = []
checkoff_join = " ".join(checkoff_list)
task_list = []
comp_list = []
comp_join = " ".join(comp_list)

#App begining
#Greeting
print()
app_user = input("Hello! Please enter your name: ")
#This is the main menu
def main ():
   
    print()
    print("                     "+ app_user)
    print("         Let's get stuff done together!")
        
        #If you change this you will need to change the main menu index
    print()
    print("     TASK MENU:")
    print()
    print("            1)    Add Task")
    print("            2)    View Tasks")
    print("            3)    Mark Complete")
    print("            4)    Delete Task")
    print("            5)    Quit")
        
    
    print()
    
    menu1 = (input(f"{add_task}, {view_tasks}, {mark_complete}, {delete_task}, {quit}: ")) #DONT CHANGE NAME MENU1
        
    while True:
                if menu1 == quit:
                        print()
                        print("Happy Tasking!") 
                        exit()
                        break
                else:
                        
                        menu1 = (input(f"Invalid input. Input: {add_task}, {view_tasks}, {mark_complete}, {delete_task}, {quit}: "))
                       
                                
                        
                        if menu1 == add_task:
                             while True:
                                        print()
                                        
                                        user_input= input("What would you like to add? Type 'quit' once done: ").lstrip().rstrip()
                                        if user_input == "quit":
                                                print()
                                                print(f"I like that list!{task_list}.")
                                                print()            
                                                break
                                        
                                        else:                            
                                                full_list.append(user_input)
                                                checkoff_list.append(user_input)
                                                task_list.append(user_input)                        
                                                print(f"Your tasks so far {task_list}")


                        elif menu1 == view_tasks:
                            print()
                            print(f"Let's look at your tasks! Completed: {comp_list} Incomplete: {checkoff_list}")
                            print()
                            clear_completed =input("Clear Completed Tasks? y or n: ")
                            if clear_completed == "y":                                    
                                    comp_list.clear()                                    
                                    print()
                                    print(comp_list)
                                    print()
                                    print("Heres your updated lists: ")
                                    print(f"Completed: {comp_list}")
                                    print(f"Incomplete: {checkoff_list}")
                                    print()


                        elif menu1 == mark_complete.lower():
                                checkoff_join = " ".join(checkoff_list)
                                while True:
                                        print() 
                                        user_input2= input(f"Which task would you like to complete? Type 'quit' once done: {checkoff_list} ")
                                        if user_input2 in checkoff_join:
                                                print()
                                                print(checkoff_list)
                                                checkoff_list.remove(user_input2)
                                                comp_list.append(user_input2)
                                                print()
                                                print(checkoff_list)
                                                print()

                                                                                                                                
                                        elif user_input2 == "quit":
                                                        print()
                                                        print("One task at a time!")
                                                        print()
                                                        break

                                        elif user_input2 not in checkoff_join:
                                                        print() 
                                                        user_input2 = input("Not in a list, would you like to add it? y or n: ")
                                                        if user_input2 == "y":
                                                                full_list.append(user_input2)
                                                                checkoff_list.append(user_input2)                                                                
                                                                task_list.append(user_input2)
                                                                print()
                                                                print("Added to list!")
                                                                print()                                                               
                                        else:
                                                        user_input2 not in checkoff_list
                                                        print() 
                                                        print("Not a valid input")
                                                        print()                                


                        elif menu1 == delete_task:
                                full_join = " ".join(full_list)
                                checkoff_join = " ".join(checkoff_list)
                                while True:
                                        print() 
                                        user_input3= input(f"Which task would you like to delete? Type 'quit' once done: {full_list} ")                                       
                                        if user_input3 in full_join and user_input3 in comp_join:
                                                print()
                                                print(full_list)
                                                full_list.remove(user_input3)
                                                comp_list.remove(user_input3) 
                                                print()                                                                                                                                           
                                                print(full_list)
                                                print()
                                        elif user_input3 in full_join and user_input3 in checkoff_join:
                                                print()
                                                print(full_list)
                                                full_list.remove(user_input3)
                                                checkoff_list.remove(user_input3) 
                                                print()                                                                                                                                           
                                                print(full_list)
                                                print()
                                        elif user_input3 in full_join:
                                                print()
                                                print(full_list)
                                                full_list.remove(user_input3)                                                
                                                print()                                                                                                                                           
                                                print(full_list)
                                                print()                                       
                                                print("Not in list!")
                                        elif user_input3 == "quit":
                                                print()
                                                print("Good riddance")
                                                print()
                                                break
                                        else: 
                                                user_input3 not in full_join
                                                print("Not in list!")


                repeat = input("Return to menu? y or n: ").lower()
                if repeat == "y":
                        main()
                else:
                        print("Happy Tasking")
                        exit()
                       
                                
main()


                

                

