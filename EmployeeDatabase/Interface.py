import mysql.connector

# Database Cresidentials
Hostname = "localhost"
Database = "COMPANY"
Username = "root"
Password = ""

# Connect to MySQL Database
mydb = mysql.connector.connect(user=Username, password=Password, host=Hostname, database=Database)
mycursor = mydb.cursor(buffered=True)

# MySQL queries and operations that will be used by methods in order to make updates to the database:

# Operations that relate to the EMPLOYEE table
insert_employee = "INSERT INTO EMPLOYEE (Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno) "\
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
select_employee = "SELECT * FROM EMPLOYEE WHERE Ssn=%s"
select_employee_super_dept = "SELECT E1.Fname, E1.Minit, E1.Lname, E1.Ssn, E1.Bdate, E1.Address, E1.Sex, E1.Salary, E1.Super_ssn, "\
                           "E1.Dno, E2.Fname, E2.Minit, E2.Lname, Dname FROM EMPLOYEE AS E1, EMPLOYEE AS E2,DEPARTMENT AS D "\
                           "WHERE E1.Super_ssn=E2.Ssn AND E1.Dno=D.Dnumber AND E1.Ssn=%s"
lock_employee = "SELECT * FROM EMPLOYEE WHERE Ssn=%s FOR UPDATE"
update_employee = "UPDATE EMPLOYEE SET Address=%s, Sex=%s, Salary=%s, Super_ssn=%s, Dno=%s WHERE Ssn=%s"
delete_employee = "DELETE FROM EMPLOYEE WHERE Ssn=%s"
check_employee_super = "SELECT * FROM EMPLOYEE WHERE Super_ssn=%s"

# Operations that relate to the DEPARTMENT and WORKS_ON tables
update_department = "UPDATE DEPARTMENT SET Mgr_ssn=NULL, Mgr_start_date=NULL WHERE Dnumber=%s"
select_manager = "SELECT * FROM DEPARTMENT WHERE Mgr_ssn=%s"
delete_workson = "DELETE FROM WORKS_ON WHERE Essn=%s"

# Operations that relate to the DEPENDENT table
select_dependent = "SELECT * FROM DEPENDENT WHERE Essn=%s"
insert_dependent = "INSERT INTO DEPENDENT (Essn, Dependent_name, Sex, Bdate, Relationship) VALUES (%s, %s, %s, %s, %s)"
delete_dependent = "DELETE FROM DEPENDENT WHERE Essn=%s AND Dependent_name=%s"
lock_dependent = "SELECT * FROM DEPENDENT WHERE Essn=%s FOR SHARE"

# Menu CLI
menu = ' ___________________________\n' \
       '| MENU                      |\n' \
       '|---------------------------|\n' \
       '| 1. Add new employee       |\n' \
       '| 2. View employee record   |\n' \
       '| 3. Add dependent          |\n' \
       '| 4. View dependent         |\n' \
       '| 5. Modify employee record |\n' \
       '| 6. Remove dependent       |\n' \
       '| 7. Remove employee        |\n' \
       '|___________________________|\n' \
       '*TYPE EXIT IF YOU WISH TO EXIT THE PROGRAM*\n' \
       'Select menu option: '

# Adds a new employee to database and displays the employee info along with the supervisor name and department name
def add_employee():
    print('\nFname: ')
    fname = input()
    print('\nMinit: ')
    minit = input()
    print('\nLname: ')
    lname = input()
    print('\nSsn: ')
    ssn = input()
    print('\nBdate: ')
    bdate = input()
    print('\nAddress: ')
    address = input()
    print('\nSex: ')
    sex = input()
    print('\nSalary: ')
    salary = input()
    print('\nSuper_ssn: ')
    super_ssn = input()
    print('\nDno: ')
    dno = input()

    data_employee = (fname, minit, lname, ssn, bdate, address, sex, salary, super_ssn, dno)
    mycursor.execute(insert_employee, data_employee)
    mydb.commit()
    print('\n**Employee Added to Database**\n')

# Retrieves and displays employee information for a specific ssn
def view_employee():
    print('\nEmployee Ssn: ')
    ssn = (input(),)
    print('\nEmployee info:\n')
    mycursor.execute(select_employee_super_dept, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# Adds a new dependent to the database
def add_dependent():
    print('\nEmployee Ssn: ')
    ssn = (input(),)
    print('\nCurrent dependents:\n')
    mycursor.execute(select_dependent, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print('\nDependent_name: ')
    name = input()
    print('\nSex: ')
    sex = input()
    print('\nBdate')
    bdate = input()
    print('\nRelationship: ')
    relationship = input()

    data_dependent = (ssn[0], name, sex, bdate, relationship)
    mycursor.execute(insert_dependent, data_dependent)
    mydb.commit()
    print('\n**Dependent Added to Database**\n')

# Retrieves and displays the dependent informatin of a specficic employee
def view_dependent():
    print('\nEmployee Ssn: ')
    ssn = (input(),)
    print('\nCurrent dependents:\n')
    mycursor.execute(select_dependent, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

# Modifies information for a certain employee by locking the row
def modify_employee():
    print('\nEmployee Ssn: ')
    ssn = (input(),)
    print('\nEmployee info:\n')
    mycursor.execute(lock_employee, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print('\nUpdated address: ')
    address = input()
    print('\nUpdated sex: ')
    sex = input()
    print('\nUpdated salary: ')
    salary = input()
    print('\nUpdated super_ssn: ')
    super_ssn = input()
    print('\nUpdated Dno: ')
    dno = input()

    updated_data = (address, sex, salary, super_ssn, dno, ssn[0])
    mycursor.execute(update_employee, updated_data)
    mydb.commit()
    print('\n**Employee Updated**\n')

# Removes dependent from database. Locks employee of dependent and dependents
def remove_dependent():
    print('\nEmployee Ssn: ')
    ssn = (input(),)
    print('\nEmployee info:\n')
    mycursor.execute(lock_employee, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print('\nDependent info: \n')
    mycursor.execute(lock_dependent, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    print('\nDependent name to be removed: ')
    name = input()
    data_dependent = (ssn[0], name)
    mycursor.execute(delete_dependent, data_dependent)
    mydb.commit()
    print('\n**Dependent Removed**\n')

# Removes employee from database. Locks employee
# Checks if employee has dependents
# Checks if employee is a manager, and whether all the employees under the manager have been reassigned
# Also deletes employee information from WORKS_ON table
def remove_employee():
    print('\nEmployee Ssn: ')
    ssn = (input(),)
    print('\nEmployee info:\n')
    mycursor.execute(lock_employee, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
    print('\nCurrent dependents:\n')
    mycursor.execute(select_dependent, ssn)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

    dependent_count = mycursor.rowcount
    employee_count = 0
    mycursor.execute(select_manager, ssn)
    mgr_ssn = mycursor.rowcount
    if mgr_ssn > 0:
        mycursor.execute(check_employee_super, ssn)
        employee_count = mycursor.rowcount

    print('\nAre you sure you want to remove this employee? Type Y or N: ')
    answer = input()
    if answer == 'Y':
        if dependent_count > 0:
            print('\nError: Please delete the existing dependent records before removing the employee.\n')
            return
        if employee_count > 0:
            print('\nError: Please reassign all employees working under this manager before removing the manager.\n')
            return
        mycursor.execute(delete_employee, ssn)
        mycursor.execute(delete_workson, ssn)
        print('\n**Employee Removed**\n')
    mydb.commit()

# While loop to keep program running. Exits while loop if 'EXIT' is inputted when selecting menu option
exit = False
while not exit:
    print(menu)
    menu_option = input()
    print("Menu option selected: ", menu_option)

    if menu_option == 'EXIT':
        exit = True
        break
    menu_option = int(menu_option)
    if menu_option == 1:
        add_employee()
    elif menu_option == 2:
        view_employee()
    elif menu_option == 3:
        add_dependent()
    elif menu_option == 4:
        view_dependent()
    elif menu_option == 5:
        modify_employee()
    elif menu_option == 6:
        remove_dependent()
    elif menu_option == 7:
        remove_employee()
    else:
        print('Error. Enter one of the numbers above or type EXIT to end program.\n')

# Closes connections to MySQL Database
mycursor.close()
mydb.close()
