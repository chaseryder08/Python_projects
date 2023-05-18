#Easy to do list project: 

todo_list = []

def add_item():
    item = input("Enter item to add: ")
    todo_list.append(item)
    print(f"{item} has been added!")
    
def remove_item():
    item = input("Enter item you want to remove: ")
    if item in todo_list:
        todo_list.remove(item)
        print(f"{item} has been removed!")
    else:
        print("That item does not exist")
            
def display_list():
    if todo_list:
        print("To do list:")
        for item in todo_list:
            print("- " + item)
    else:
        print("item list is empty!")
            
       
def main():
    print("Welcome to my to do list: ")
    while True:
        print("\nChoose an option:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. Display the todo list")
        print("4. Quit")
    
        choice = input("Enter a number: ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_list()
        elif choice == "4":
            print("GOODBYE!")
            break
        else:
            print("Invalid selection -- try again!")
        
if __name__ == '__main__':
    main()
                         
        
