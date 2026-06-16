import os
import sys
employees = {}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def Add_employer():
    clear_console()
    print("=== ADD Employee ===")
    Name = str(input("1.Employee Name: ")).upper()
    Age = int(input("2.Employee Age: "))
    Salary = int(input("3.Employee Salary: "))
    Department = str(input("4.Employee Department: ")).upper()
    if Name in employees:
        clear_console()
        print("Name Alrady in DB Try Again!")
        return
    elif Age <= 0 or Age > 100:
         clear_console()
         print("Age between 1-100 ")
         return
    elif Salary < 0 or Salary > 99999:
        clear_console()
        print("Salary between 0-99999")
        return
    employees[Name] = dict(age_value = Age , Salary_value = Salary , Department_value = Department)
    clear_console()
    print("\nSaved!!\nName:",Name,"\nAge:",employees[Name]["age_value"],"\nSalary:",employees[Name]["Salary_value"],"\nDepartmet:",employees[Name]["Department_value"])

def View_employer():
    clear_console()
    print("=== List Employees ===")
    if not employees:
        print("Its Empty!!")
        return
    for i in employees:   
        print("Name:",i,"\nAge:",employees[i]["age_value"],"\nSalary:",employees[i]["Salary_value"],"\nDepartmet:",employees[i]["Department_value"],"\n=====================")

def Search_employer():
    clear_console()
    print("=== Search Employee ===")
    search = str(input("-Employee Name: ")).upper()
    clear_console()
    if search not in employees:
        print("\nNo Employer With This Name in DB")
        return
    else:
        print("== Found IT! ==")
        print("Name:",search,"\nAge:",employees[search]["age_value"],"\nSalary:",employees[search]["Salary_value"],"\nDepartmet:",employees[search]["Department_value"])

def Delete_employer():
    clear_console()
    print("=== Delete Employee ===")
    Name = str(input("Employee Name: ")).upper()
    if Name not in employees:
        clear_console()
        print("Invalid Name!")
        return
    employees.pop(Name)
    clear_console()
    print("Done Employer Got Removed!!\n")

def Update_Salary():
    clear_console()
    print("=== Update Employee Salary ===")
    Name = str(input("Name: ")).upper()
    if Name not in employees:
        clear_console()
        print("Invalid Name")
        return
    Salary = int(input("New Salary: "))
    if Salary <0 or Salary>99999:
        clear_console()
        print("Invalid Input Try Again Between 0-99999")
    employees[Name]["Salary_value"] = Salary
    clear_console()
    print("Done! The New Salary Of ",Name," Is",Salary)
    

while True:
    exit_flag = False
    clear_console()
    print("=== Employee Management System ===\n")
    print("1. Add Employee \n2. View Employees\n3. Search Employee\n4. Delete Employee\n5. Update Salary\n6. Quit")
    Choise = input()
    try:
        if Choise == "1":
            Add_employer()
        if Choise == "2":
            View_employer()
        if Choise == "3":
            Search_employer()
        if Choise == "4":
            Delete_employer()
        if Choise == "5":
            Update_Salary()
        if Choise == "6":
            #Exit Choice
            clear_console()
            print("See You Soon <3")
            exit_flag = True
            sys.exit()
    except ValueError:
        print("Invalid Number!")
    finally:
        if not exit_flag:
            input("Press Any Key To Back to Menu...")
            clear_console()