# Hello World program in Python
    
DEP = "Please enter the department name or EXIT when you finish"
DEP_ERROR = "The department name could not be empty. Please enter the department name or EXIT when you finish"
EMP_FIRST_NAME = "Please enter the employee first name"
EMP_LAST_NAME = "Please enter the employee last name"
EMP_SALARY = "Please enter the employee salary"
EMP_DEP = "Please enter department name"
EXIT = "EXIT"
YES = "YES"
NO = "NO"

questions = [EMP_FIRST_NAME, EMP_LAST_NAME, EMP_SALARY, EMP_DEP]
    
class Employee:
    
    firstName = ""
    lastName = ""
    salary = 0
    dep = ""
    
    def __init__(self, new_firstName, new_lastName, new_salary, new_dep):
        self.firstName = new_firstName
        self.lastName = new_lastName
        self.salary = new_salary
        self.dep = new_dep
        
class Department:
    empl_count = 0
    sum_sal = 0
    avg_sal = 0
    min_sal = None
    max_sal = 0
    
    def add_dept_salary(new_sal):
        empl_count++
        sum_sal += new_sal
        avg_sal = sum_sal / empl_count
        if (new_sal < min_sal || min_sal == None):
            min_sal = new_sal
        
        if (new_sal > max_sal):
            max_sal = new_sal
            

        
def initialize_values():
    user_input = ""  
    counter = 0
    emp_f_name = ""
    emp_l_name = ""
    emp_sal = 0
    emp_dep = ""
      
user_input = ""  

print("/////////////////////////////////////////////////////////////////")

departments = {}        
while user_input.upper() != EXIT: 
    user_input = input(DEP)
    departments[user_input] = Department()
    #Validate before add()
    
employees = []
initialize_values()

while user_input.upper() != NO:
    counter++
    user_input = input(questions[counter])
    if (counter == 1):
        emp_f_name = user_input
    else if (counter == 2):
        emp_l_name = user_input
    else if (counter == 3):
        emp_sal = user_input
    else if (counter == 4):
        emp_dep = user_input
        empl = Employee(emp_f_name, emp_l_name, emp_sal, emp_dep)
        employees.append(empl)
        if (departments.get(empl.dep) != None):
            departments.add_dept_salary(empl.)
        initialize_values()
    

for emp in employees:
    if (departments.get(emp.dep) != None):
        departments[emp.dep] += emp.salary



    
    
    
    
    
    