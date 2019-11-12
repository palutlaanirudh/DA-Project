import subprocess as sp
import pymysql
import pymysql.cursors

# STORE related functions
def store_exist(sn):
    query = f"select * from STORE where StoreNo={sn};"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if (len(rows) == 0):
        raise Exception(f"Store number {sn} does not exist in database. Please enter a valid store number")
    return


def store_add():
    try:
        store = {}
        clear()
        while ( 1 ):
            print("The allowed store numbers are integers greater than 0")
            store["no"] = int(input("Store number: "))
            if store["no"] > 0:
                break
            else:
                print("Invalid store number. Please try again.")
        store["loc"] = input("Store Location: ")
        query = f"insert into STORE values (\"{store['no']}\", \"{store['loc']}\");"
        #print("query: ", query)
        cur.execute(query)
        con.commit()
        print("Inserted into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert")
        print(">>>", e)
    return

def store_update():
    try:
        clear()
        store = {}
        store["no"] = int(input("Store number of the store you want to edit: "))
        store_exist(store["no"])
        while ( 1 ):
            clear()
            print("What attribute do you want to edit?")
            print("1. Store Number")
            print("2. Location")
            ops = int(input("Your choice> "))
            query = ""
            if ops == 1:
                inp = int(input("Updated store number: "))
                query = f"update STORE set StoreNo={inp} where StoreNo={store['no']};"
            elif ops == 2:
                inp = input("Updated location: ")
                query = f"update STORE set LocationID='{inp}' where StoreNo={store['no']};"
            else:
                print("Invalid input. Please try again")
                continue
            cur.execute(query)
            con.commit()
            break
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return

def store_delete():
    try:
        clear()
        store_no = int(input("Store number of store you want to delete: "))
        store_exist(store_no)
        query = f"delete from STORE where StoreNo={store_no};"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to delete")
        print(">>>", e)

def choice_store ():
    while ( 1 ):
        clear()
        print("1. Add a new store")
        print("2. Update existing store information")
        print("3. Delete a store")
        print("4. Cancel")
        ch = int(input("Your choice> "))
        if ch == 1:
            store_add()
        elif ch == 2:
            store_update()
        elif ch == 3:
            store_delete()
        elif ch == 4:
            break
        else:
            print("Invalid choice. Please try again")
    return


# EMPLOYEE related functions
def employee_exist(eid):
    query = f"select * from EMPLOYEE where EmployeeID={eid};"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if (len(rows) == 0):
        raise Exception(f"Employee ID {eid} does not exist in database. Please enter a valid employee number")
    return


def employee_add():
    try:
        employee = {}
        clear()
        while ( 1 ):
            print("The allowed employee numbers are integers greater than 0")
            employee["id"] = input("Employee ID (10-digit code consisting of characters): ")
            if len(employee["id"]) == 10:
                break
            else:
                print("Invalid Employee ID. Please try again.")
        employee["fname"] = input("First name: ")
        employee["mname"] = input("Middle name: ")
        employee["lname"] = input("Last name: ")
        employee["dob"] = input("Date of birth (YYYY-MM-DD format): ")
        employee["years_worked"] = 2019 - int(employee["dob"].split("-")[0])
        while ( 1 ):
            employee["sex"] = input("Sex (M, F, or O): ")
            if employee["sex"] != "M" and employee["sex"] != "F" and employee["sex"] != "O":
                print("Invalid sex. Please enter again.")
            else:
                break
        employee["sal"] = input("Salary: ")
        employee["mid"] = input("Manager ID (has to already exist in EMPLOYEE): ")
        employee["wat"] = input("Works at (store number): ")
        query = f"insert into EMPLOYEE values ('{employee['id']}', '{employee['fname']}', '{employee['mname']}', \
                '{employee['lname']}', '{employee['dob']}', '{employee['years_worked']}', '{employee['sex']}', \
                '{employee['sal']}', '{employee['mid']}', '{employee['wat']}');"
        cur.execute(query)
        con.commit()
        print("Inserted into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def employee_update():
    try:
        clear()
        eid = int(input("Employee ID of the employee you want to edit: "))
        employee_exist(eid)
        while ( 1 ):
            clear()
            print("What attribute do you want to edit?")
            print("1. Employee ID")
            print("2. First Name")
            print("3. Middle Name")
            print("4. Last Name")
            print("5. Date of Birth")
            print("6. Sex")
            print("7. Salary")
            print("8. Manager ID")
            print("9. Works at (Store Number)")
            ops = int(input("Your choice> "))
            query = ""
            if ops == 1:
                while ( 1 ):
                    inp = input("Updated Employee ID: ")
                    if len(inp) == 10:
                        break
                    else:
                        print("Invalid Employee ID. Please try again.")
                query = f"update EMPLOYEE set EmployeeID='{inp}' where EmployeeID='{eid}';"
            elif ops == 2:
                inp = input("Updated first name: ")
                query = f"update EMPLOYEE set Fname='{inp}' where EmployeeID='{eid}';"
            elif ops == 3:
                inp = input("Updated middle name: ")
                query = f"update EMPLOYEE set Mname='{inp}' where EmployeeID='{eid}';"
            elif ops == 4:
                inp = input("Updated last name: ")
                query = f"update EMPLOYEE set Lname='{inp}' where EmployeeID='{eid}';"
            elif ops == 5:
                inp = input("Updated DoB: ")
                query = f"update EMPLOYEE set DoB='{inp}' where EmployeeID='{eid}';"
            elif ops == 6:
                inp = input("Updated Sex: ")
                query = f"update EMPLOYEE set Sex='{inp}' where EmployeeID='{eid}';"
            elif ops == 7:
                inp = input("Updated salary: ")
                query = f"update EMPLOYEE set Salary='{inp}' where EmployeeID='{eid}';"
            elif ops == 8:
                inp = input("Updated Manager ID: ")
                query = f"update EMPLOYEE set ManagerID='{inp}' where EmployeeID='{eid}';"
            elif ops == 9:
                inp = input("Updated works at store no: ")
                query = f"update EMPLOYEE set WorksAt='{inp}' where EmployeeID='{eid}';"
            else:
                print("Invalid input. Please try again")
                input("Press ENTER to continue>")
                continue
            print(query)
            cur.execute(query)
            con.commit()
            break
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def employee_delete():
    try:
        clear()
        eid = int(input("Employee ID of employee you want to delete: "))
        employee_exist(eid)
        query = f"delete from EMPLOYEE where EmployeeID={eid};"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to delete")
        print(">>>", e)
        input("Press ENTER to continue>")

def choice_employee ():
    while ( 1 ):
        clear()
        print("1. Add a new employee")
        print("2. Update existing employee information")
        print("3. Delete an employee")
        print("4. Go back")
        ch = int(input("Your choice> "))
        if ch == 1:
            employee_add()
        elif ch == 2:
            employee_update()
        elif ch == 3:
            employee_delete()
        elif ch == 4:
            break
        else:
            print("Invalid choice. Please try again")
            input("Press ENTER to continue>")
    return


# MANUFACTURER related functions
def manufacturer_exist(mnid):
    query = f"select * from MANUFACTURER where NameID='{mnid}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if (len(rows) == 0):
        raise Exception(f"Manufacturer name {mnid} does not exist in database. Please enter a valid manufacturer name")
    return

def manufacturer_add():
    try:
        manufacturer = {}
        clear()
        while ( 1 ):
            print("The allowed manufacturer names are non null strings shorter than 40 characters")
            manufacturer["nameid"] = input("Manufacturer Name: ")
            if 0 < len(manufacturer["nameid"]) < 40 :
                break
            else:
                print("Invalid Manufacturer name. Please try again.")
        manufacturer["country"] = input("Country: ")
        manufacturer["yearest"] = input("Year established: ")
        query = f"insert into MANUFACTURER values ('{manufacturer['nameid']}', '{manufacturer['country']}', '{manufacturer['yearest']}');"
        cur.execute(query)
        con.commit()
        print("Inserted into database")
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def manufacturer_update():
    try:
        clear()
        mnid = input("Name of the manufacturer you want to edit: ")
        manufacturer_exist(mnid)
        while ( 1 ):
            clear()
            print("What attribute do you want to edit?")
            print("1. Manufacturer Name")
            print("2. Country")
            print("3. Year Established")
            ops = int(input("Your choice> "))
            query = ""
            if ops == 1:
                while ( 1 ):
                    inp = input("Updated Manufacturer Name: ")
                    if 0 < len(inp) < 40:
                        break
                    else:
                        print("Invalid Manufacturer Name. Please try again.")
                query = f"update MANUFACTURER set NameID='{inp}' where NameID='{mnid}';"
            elif ops == 2:
                inp = input("Updated country: ")
                query = f"update MANUFACTURER set Country='{inp}' where NameID='{mnid}';"
            elif ops == 3:
                while ( 1 ):
                    inp = input("Updated year established: ")
                    if 0 < int(inp) <= 2020:
                        break
                    else:
                        print("Invalid input. Please enter a valid year.")
                query = f"update MANUFACTURER set YearEst='{inp}' where NameID='{mnid}';"
            else:
                print("Invalid input. Please try again")
                input("Press ENTER to continue>")
                continue
            print(query)
            cur.execute(query)
            con.commit()
            break
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
        input("Press ENTER to continue>")
    return


def manufacturer_delete():
    try:
        clear()
        mnid = input("Name of the manufacturer you want to delete: ")
        manufacturer_exist(mnid)
        query = f"delete from MANUFACTURER where NameID='{mnid}';"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to delete")
        print(">>>", e)
        input("Press ENTER to continue>")

def choice_manufacturer():
    while ( 1 ):
        clear()
        print("1. Add a new manufacturer")
        print("2. Update existing manufacturer information")
        print("3. Delete an manufacturer")
        print("4. Cancel")
        ch = int(input("Your choice> "))
        if ch == 1:
            manufacturer_add()
        elif ch == 2:
            manufacturer_update()
        elif ch == 3:
            manufacturer_delete()
        elif ch == 4:
            break
        else:
            print("Invalid choice. Please try again")
            input("Press ENTER to continue>")
    return


# CUSTOMER related functions
def customer_exist(cid):
    query = f"select * from CUSTOMER where CustomerID='{cid}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if (len(rows) == 0):
        raise Exception(f"Customer ID {cid} does not exist in database. Please enter a valid customer ID.")
    return

def choice_customer():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new customer")
        print("2. Update existing customer information")
        print("3. Go back")
        ops = int(input("Your choice> "))
        if ops == 1:
            customer_add()
        elif ops == 2:
            customer_update()
        elif ops == 3:
            break
        else:
            print("Invalid option. Please try again.")
            input("Press ENTER to continue>")
    return

def customer_add():
    try:
        customer = {}
        print("Please enter the customer's information")
        while ( 1 ):
            customer["id"] = input("Customer ID (10-digit code consisting of characters): ")
            if len(customer["id"]) == 10:
                break
            else:
                print("Invalid Customer ID. Please enter again.")
        customer["fname"] = input("First name: ")
        mn = input("Does customer have a middle name (y for yes)?: ")
        if mn == 'y':
            customer["mname"] = input("Middle name: ")
        else:
            customer["mname"] = "NULL"
        customer["lname"] = input("Last name: ")
        customer["tpv"] = int(input("Total purchase value: "))
        customer["vfb"] = input("ID of Employee that verified the customer (has to exist in EMPLOYEE already):  ")
        query = f"insert into CUSTOMER values ('{customer['id']}', '{customer['fname']}', '{customer['mname']}', \
                '{customer['lname']}', '{customer['tpv']}', '{customer['vfb']}'); "
        print("Query = ", query)
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def customer_update():
    try:
        clear()
        cid = int(input("Customer ID of the customer you want to edit: "))
        customer_exist(cid)
        while ( 1 ):
            clear()
            print("What attribute do you want to edit?")
            print("1. First Name")
            print("2. Middle Name")
            print("3. Last Name")
            print("4. Total Purchase Value")
            ops = int(input("Your choice> "))
            query = ""
            if ops == 1:
                inp = input("Updated first name: ")
                query = f"update CUSTOMER set Fname='{inp}' where CustomerID='{cid}';"
            elif ops == 2:
                inp = input("Updated middle name: ")
                query = f"update CUSTOMER set Mname='{inp}' where CustomerID='{cid}';"
            elif ops == 3:
                inp = input("Updated last name: ")
                query = f"update CUSTOMER set Lname='{inp}' where CustomerID='{cid}';"
            elif ops == 4:
                inp = input("Updated total purchase value: ")
                query = f"update CUSTOMER set TotalPurchaseValue='{inp}' where CustomerID='{cid}';"
            else:
                print("Invalid input. Please try again")
                input("Press ENTER to continue>")
                continue
            print(query)
            cur.execute(query)
            con.commit()
            break
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

# AMMO related functions
def ammo_exist(aid):
    query = f"select * from AMMO where CartridgeName='{aid}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if(len(rows) == 0):
        raise Exception(f"Cartridge name {aid} does not exist in database. Please enter a valid cartridge name")
    return

def ammo_add():
    try:
        ammo = {}
        clear()
        while ( 1 ):
            printf("The allowed cartridge names are non null strings shorter than 40 characters")
            ammo["cartridgename"] = input("Cartridge Name: ")
            if 0 < len(ammo["cartridgename"]) < 40:
                break
            else:
                print("Invalid cartridge name. Please try again.")
        ammo["shape"] = input("Shape: ")
        ammo["noofrounds"] = input("No Of Rounds: ")
        ammo["caliber"] = input("Caliber: ")
        ammo["cost"] = input("Cost: ")
        query = f"insert into AMMO values ('{ammo['cartridgename']}', '{ammo['shape']}', '{ammo['noofrounds']}', '{ammo['caliber']}', '{ammo['cost']}');"
        cur.execute(query)
        con.commit()
        print("Inserted into database")
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def ammo_update():
    try:
        clear()
        cartridgename = input("Name of the cartridge you want to edit: ")
        ammmo_exist(cartridgename)
        while ( 1 ):
            clear()
            print("What attribute do you want to edit?")
            print("1. Cartridge Name")
            print("2. Shape")
            print("3. No Of Rounds")
            print("4. Caliber")
            print("5. Cost")
            ops = int(input("Your choice> "))
            query = ""
            if ops == 1:
                while ( 1 ):
                    inp = input("Updated Cartridge Name: ")
                    if 0 < len(inp) < 40:
                        break
                    else:
                        print("Invalid cartridge name. Please try again.")
                query = f"update AMMO set CartridgeName='{inp}' where CartridgeName='{cartridgename}';"
            elif ops == 2:
                while(1):
                    inp = input("Updated Shape: ")
                    if 0 < len(inp) < 40:
                        break
                    else:
                        print("Invalid shape. Please Try again.")
                query = f"update AMMO set Shape='{inp}' where CartridgeName='{cartridgename}'"
            elif ops == 3:
                while ( 1 ):
                    inp = input("Updated No Of Rounds: ")
                    if inp.isnumeric():
                        break
                    else:
                        print("Invalid No of Rounds. Please Try again.")
                query = f"update AMMO set NoOfRounds='{inp}' where CartridgeName='{cartridgename}'"
            elif ops == 4:
                while(1):
                    inp = input("Updated Caliber: ")
                    if 0 < len(inp) < 10:
                        break
                    else:
                        print("Invalid Caliber. Please try again.")
                query = f"update AMMO set Caliber='{inp}' where CartridgeName='{cartridgename}'"
            elif ops == 5:
                while(1):
                    inp = input("Updated Cost: ")
                    if inp.isnumeric():
                        break
                    else:
                        print("Invalid Cost. Please Try again.")
                query = f"update AMMO set Cost='{inp}' where CartridgeName='{cartridgename}'"
            else:
                print("Invalid input")
                input("Press ENTER to continue>")
                continue
            print(query)
            cur.execute(query)
            con.commit()
            break
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def ammo_delete():
    try:
        clear()
        cartridgename = input("Name of the cartridge you want to delete: ")
        ammo_exist(cartridgename)
        query = f"delete from AMMO where CartridgeName='{cartridgename}'"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to delete")
        print(">>>", e)
        input("Press ENTER to continue>")

def choice_ammo():
    while(1):
        clear()
        print("1. Add a new cartridge")
        print("2. Update existing ammo information")
        print("3. Delete a cartridge")
        print("4. Cancel")
        ch = int(input("Your choice> "))
        if ch == 1:
            ammo_add()
        elif ch == 2:
            ammo_update()
        elif ch == 3:
            ammo_delete()
        elif ch == 4:
            break
        else:
            print("Invalid choice. Please try again")
            input("Press ENTER to continue>")
    return

# Overall functions
def choices (ch):
    if ch == 1:
        choice_store()
    elif ch == 2:
        choice_employee()
    elif ch == 3:
        choice_customer()
    elif ch == 4:
        choice_manufacturer()
    else:
        print("Invalid input. Please try again.")
    return

def clear():
    sp.call('clear', shell=True)
    return


# Global
while(1):
    clear()
#    username = input("Username: ")
#    password = input("Password: ")
    username = "anirudh"
    password = "746058"

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='GUN_STORE',
                cursorclass=pymysql.cursors.DictCursor)
        clear()

        if(con.open):
            print("Connected")
        else: 
            print("Failed to connect") 
            input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while ( 1 ):
                clear()
                print("Which information would you like to access?")
                print("1. Stores")
                print("2. Employees")
                print("3. Customers")
                print("4. Manufacturers")
                print("5. Logout")
                ch = int(input("Enter choice> "))
                clear()

                if ch == 5:
                    break
                else:
                    choices(ch)
                    input("Enter any key to CONTINUE>")

    except:
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        input("Press ENTER to continue>")
        exit(0)
    
