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
        print("4. Manage contact numbers")
        print("5. Cancel")
        ch = int(input("Your choice> "))
        if ch == 1:
            store_add()
        elif ch == 2:
            store_update()
        elif ch == 3:
            store_delete()
        elif ch == 4:
            store_contactnos()
        elif ch == 5:
            break
        else:
            print("Invalid choice. Please try again")
    return

def store_contactnos ():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new contact number")
        print("2. Delete existing contact number")
        print("3. Go back")
        ch = int(input("Your choice> "))
        if ch == 3:
            break
        elif ch == 1:
            store_contactnos_add()
        elif ch == 2:
            store_contactnos_delete()
        else:
            print("Invalid input. Please enter a valid option.")
            input("Press ENTER key to continue>")
    return

def store_contactnos_add():
    try:
        print("Please enter the required details.")
        sn = input("Store number: ")
        store_exist(sn)
        cn = input("Contact number: ")
        query = f"insert into STORE_CONTACTNOS values ('{sn}', '{cn}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return

def store_contactnos_delete():
    try:
        print("Please enter the required details.")
        sn = input("Store number: ")
        store_exist(sn)
        cn = input("Contact number: ")
        cur.execute(f"select * from STORE_CONTACTNOS where StoreNo='{sn}' and ContactNo='{cn}';")
        con.commit()
        rows = cur.fetchall()
        if (len(rows) == 0):
            raise Exception("This entry does not exist.")
        else:
            query = f"delete from STORE_CONTACTNOS where StoreNo='{sn}' and ContactNo='{cn}';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
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
        print("4. Manage contact numbers")
        print("5. Go back")
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

#DEPENDANT related functions
def dependant_exist(eid, fn, mn, ln):
    query = f"select * from DEPENDANT where DependsOn='{eid}' and Fname='{fn}' and Mname='{mn}' and Lname='{ln}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if len(rows) > 0:
        return
    else:
        raise Exception(f"Gun with Manufacturer {gmm} and Model Type {gmmt} does not exist in the database. Please try again.")
    return

def dependant():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new dependant")
        print("2. Delete existing dependant")
        print("3. Go back")
        ch = int(input("Your choice> "))
        if ch == 3:
            break
        elif ch == 1:
            dependant_add()
        elif ch == 2:
            dependant_delete()
        else:
            print("Invalid input. Please enter a valid option.")
            input("Press ENTER key to continue>")
    return

def dependant_add():
    try:
        print("Please enter the required details.")
        eid = int(input("Employee ID: "))
        employee_exist(sn)
        fn = input("First name: ")
        mn = input("Middle name: ")
        ln = input("Last name: ")
        cn = input("Contact number: ")
        query = f"insert into DEPENDANT values ('{eid}', '{fn}', '{mn}', '{ln}', {cn}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return

def dependant_delete():
    try:
        print("Please enter the required details.")
        eid = input("Employee ID: ")
        fn = input("First name: ")
        mn = input("Middle name: ")
        ln = input("Last name: ")
        dependant_exist(eid, fn, mn, ln)
        cn = input("Contact number: ")
        cur.execute(f"select * from DEPENDANT where EmployeeID='{eid}' and Fname='{fn}' and Mname='{mn}' and Lname='{ln}';")
        con.commit()
        rows = cur.fetchall()
        if (len(rows) == 0):
            raise Exception("This entry does not exist.")
        else:
            query = f"delete from DEPENDANT where EmployeeID='{eid}' and Fname='{fn}' and Mname='{mn}' and Lname='{ln}';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return


#EMPLOYEE_CONTACT_NOS related functions
def employee_contactnos ():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new contact number")
        print("2. Delete existing contact number")
        print("3. Go back")
        ch = int(input("Your choice> "))
        if ch == 3:
            break
        elif ch == 1:
            employee_contactnos_add()
        elif ch == 2:
            employee_contactnos_delete()
        else:
            print("Invalid input. Please enter a valid option.")
            input("Press ENTER key to continue>")
    return

def employee_contactnos_add():
    try:
        print("Please enter the required details.")
        sn = int(input("Employee ID: "))
        employee_exist(sn)
        cn = input("Contact number: ")
        query = f"insert into EMPLOYEE_CONTACTNOS values ('{sn}', '{cn}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return

def employee_contactnos_delete():
    try:
        print("Please enter the required details.")
        sn = input("Employee ID: ")
        employee_exist(sn)
        cn = input("Contact number: ")
        cur.execute(f"select * from EMPLOYEE_CONTACTNOS where EmployeeID='{sn}' and ContactNo='{cn}';")
        con.commit()
        rows = cur.fetchall()
        if (len(rows) == 0):
            raise Exception("This entry does not exist.")
        else:
            query = f"delete from EMPLOYEE_CONTACTNOS where EmployeeID='{sn}' and ContactNo='{cn}';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
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
        print("3. Delete a manufacturer")
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

#FACTORY related functions
def factory_exist(mn, lid):
    query = f"select * from FACTORY where ManufacturerName='{mn}' and LocationID='{lid}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if len(rows) > 0:
        return
    else:
        raise Exception(f"Factory belonging to manufacturer {mn} in {lid} does not exist in the database. Please try again.")
    return

def factory():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new factory")
        print("2. Delete existing factory")
        print("3. Manage contact numbers")
        print("4. Go back")
        ch = int(input("Your choice> "))
        if ch == 4:
            break
        elif ch == 1:
            factory_add()
        elif ch == 2:
            factory_delete()
        elif ch == 3:
            factory_contactnos()
        else:
            print("Invalid input. Please enter a valid option.")
            input("Press ENTER key to continue>")
    return

def factory_add():
    try:
        print("Please enter the required details.")
        sn = input("Manufacturer Name: ")
        manufacturer_exist(sn)
        cn = input("Factory Location: ")
        query = f"insert into FACTORY values ('{sn}', '{cn}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return

def factory_delete():
    try:
        print("Please enter the required details.")
        sn = input("Manufacturer Name: ")
        manufacturer_exist(sn)
        cn = input("Location: ")
        cur.execute(f"select * from FACTORY where ManufacturerName='{sn}' and LocationID='{cn}';")
        con.commit()
        rows = cur.fetchall()
        if (len(rows) == 0):
            raise Exception("This entry does not exist.")
        else:
            query = f"delete from FACTORY where ManufacturerName='{sn}' and LocationID='{cn}';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return
 
def factory_contactnos ():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new contact number")
        print("2. Delete existing contact number")
        print("3. Go back")
        ch = int(input("Your choice> "))
        if ch == 3:
            break
        elif ch == 1:
            factory_contactnos_add()
        elif ch == 2:
            factory_contactnos_delete()
        else:
            print("Invalid input. Please enter a valid option.")
            input("Press ENTER key to continue>")
    return

def factory_contactnos_add():
    try:
        print("Please enter the required details.")
        sn = input("Manufacturer Name: ")
        lid = input("Location: ")
        factory_exist(sn, lid)
        cn = input("Contact number: ")
        query = f"insert into FACTORY_CONTACTNOS values ('{sn}', '{lid}', '{cn}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
    return

def factory_contactnos_delete():
    try:
        print("Please enter the required details.")
        sn = input("Manufacturer Name: ")
        lid = input("Location: ")
        factory_exist(sn, lid)
        cn = input("Contact number: ")
        cur.execute(f"select * from FACTORY_CONTACTNOS where ManufacturerName='{sn}' and LocationID='{lid}' and ContactNo='{cn}';")
        con.commit()
        rows = cur.fetchall()
        if (len(rows) == 0):
            raise Exception("This entry does not exist.")
        else:
            query = f"delete from FACTORY_CONTACTNOS where ManufacturerName='{sn}' and LocationID='{lid}' and ContactNo='{cn}';"
            cur.execute(query)
            con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to update")
        print(">>>", e)
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

def choice_customer():
    while ( 1 ):
        clear()
        print("What would you like to do?")
        print("1. Add new customer")
        print("2. Update existing customer information")
        print("3. Manage contact numbers")
        print("4. Go back")
        ops = int(input("Your choice> "))
        if ops == 1:
            customer_add()
        elif ops == 2:
            customer_update()
        elif ops == 3:
            customer_contactnos()
        elif ops == 4:
            break
        else:
            print("Invalid option. Please try again.")
            input("Press ENTER to continue>")
    return

# GUN_MODEL related functions
def gunmodel_exist(gmm, gmmt):
    query = f"select ModelType from GUN_MODEL where Manufacturer='{gmm}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if len(rows) != 0:
        return
    else:
        raise Exception(f"Gun with Manufacturer {gmm} and Model Type {gmmt} does not exist in the database. Please try again.")
    return

def gunmodel_add():
    try:
        gunmodel = {}
        clear()
        while ( 1 ):
            print("The allowed gun manufacturer names are non null strings shorter than 40 characters")
            gunmodel["manid"] = input("Gun Manufacturer Name: ")
            if 0 < len(gunmodel["manid"]) < 40 :
                break
            else:
                print("Invalid Gun Manufacturer name. Please try again.")
        while ( 1 ):
            print("The allowed gun model types are non null strings shorter than 40 characters")
            gunmodel["typeid"] = input("Gun Model Type: ")
            if 0 < len(gunmodel["typeid"]) < 40 :
                break
            else:
                print("Invalid Gun Model type. Please try again.")
        gunmodel["cost"] = input("Cost: ")
        gunmodel["firerate"] = input("Firerate: ")
        gunmodel["colour"] = input("Colour: ")
        query = f"insert into GUN_MODEL values ('{gunmodel['manid']}', '{gunmodel['typeid']}', '{gunmodel['cost']}', '{gunmodel['firerate']}', '{gunmodel['colour']}');"
        cur.execute(query)
        con.commit()
        print("Inserted into database")
    except Exception as e:
        con.rollback()
        print("Failed to insert")
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
            print("The allowed cartridge names are non null strings shorter than 40 characters")
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
        print("Failed to insert")
        print(">>>", e)
        input("Press ENTER to continue>")
    return

def gunmodel_update():
    try:
        clear()
        gmm = input("Manufacturer of the gun model you want to edit: ")
        gmmt = input("Type of the gun model you want to edit: ")
        gunmodel_exist(gmm, gmmt)
        while ( 1 ):
            clear()
            print("What attribute do you want to edit?")
            print("1. Manufacturer Name")
            print("2. Model Type")
            print("3. Cost")
            print("4. Firerate")
            print("5. Colour")
            ops = int(input("Your choice> "))
            query = ""
            if ops == 1:
                while ( 1 ):    
                    inp = input("Updated Gun Manufacturer Name: ")
                    if 0 < len(inp) < 40:
                        break
                    else:
                        print("Invalid Gun Manufacturer Name. Please try again.")
                query = f"update GUN_MODEL set Manufacturer='{inp}' where Manufacturer='{gmm}' and ModelType='{gmmt}';"
            elif ops == 2:
                while ( 1 ):
                    inp = input("Updated Gun Model Type: ")
                    if 0 < len(inp) < 40:
                        break
                    else:
                        print("Invalid Gun Model Type. Please try again.")
                query = f"update GUN_MODEL set ModelType='{inp}' where Manufacturer='{gmm}' and ModelType='{gmmt}';"
            elif ops == 3:
                inp = input("Updated cost: ")
                query = f"update GUN_MODEL set Cost='{inp}' where Manufacturer='{gmm}' and ModelType='{gmmt}';"
            elif ops == 4:
                inp = input("Updated firerate: ")
                query = f"update GUN_MODEL set Firerate='{inp}' where Manufacturer='{gmm}' and ModelType='{gmmt}';"    
            elif ops == 5:
                inp = input("Updated colour: ")
                query = f"update GUN_MODEL set Colour='{inp}' where Manufacturer='{gmm}' and ModelType='{gmmt}';"
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
  

def ammo_update():
    try:
        clear()
        cartridgename = input("Name of the cartridge you want to edit: ")
        ammo_exist(cartridgename)
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


def gunmodel_delete():
    try:
        clear()
        gmm = input("Manufacturer of the gun model you want to delete: ")
        gmmt = input("Type of the gun model you want to delete: ")
        gunmodel_exist(gmm, gmmt)
        query = f"delete from GUN_MODEL where Manufacturer='{gmm}' and ModelType='{gmmt}';"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to delete")
        print(">>>", e)
        input("Press ENTER to continue>")

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


def choice_gunmodel():
    while ( 1 ):
        clear()
        print("1. Add a new gun model")
        print("2. Update existing gun model information")
        print("3. Delete a gun model")
        print("4. Go back")
        ch = int(input("Your choice> "))
        if ch == 1:
            gunmodel_add()
        elif ch == 2:
            gunmodel_update()
        elif ch == 3:
            gunmodel_delete()
        elif ch == 4:
            break
        else:
            print("Invalid choice. Please try again")
            input("Press ENTER to continue>")
    return

def choice_ammo():
    while(1):
        clear()
        print("1. Add a new cartridge")
        print("2. Update existing ammo information")
        print("3. Delete a cartridge")
        print("4. Go back")
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


# ATTACHMENT related functions
def attachment_exist(mn, mdt):
    query = f"select ModelType from ATTACHMENT where Manufacturer='{mn}';"
    cur.execute(query)
    con.commit()
    rows = cur.fetchall()
    if mdt in rows['ModelType']:
        return
    else:
        raise Exception(f"Attachment with Manufacturer {mn} and Model Type {mdt} does not exist \
                in the database. Please try again.")
    return

def choice_attachment():
    while ( 1 ):
        clear()
        print("What would you like to do?\n" +
                "1. Add a new attachment\n" +
                "2. Go back")
        ch = int(input("Your choice> "))
        if ch == 2:
            break
        elif ch == 1:
            attachment_add()
        else:
            print("Invalid choice. Please try again.")
            input("Press ENTER to continue>")
    return

def attachment_add():
    try:
        clear()
        att = {}
        print("Please enter attachment information.")
        att["mn"] = input("Manufacturer name: ")
        att["mdt"] = input("Model type: ")
        att["cost"] = int(input("Cost: "))
        ch = 0 
        while ( 1 ):
            print("Please select an attachment type:\n" +
                    "1. Barrel\n" +  
                    "2. Flashlight\n" +  
                    "3. Laser\n" +  
                    "4. Magazine\n" +  
                    "5. Grip\n" +  
                    "6. Scope")
            ch = int(input("Your choice> "))
            if ch == 1:
                att["at"] = "Barrel"
            elif ch == 2:
                att["at"] = "Flashlight"
            elif ch == 3:
                att["at"] = "Laser"
            elif ch == 4:
                att["at"] = "Magazine"
            elif ch == 5:
                att["at"] = "Grip"
            elif ch == 6:
                att["at"] = "Scope"
            else:
                print("Invalid choice. Please enter a valid number.")
                input("Press ENTER to continue>")
                continue
            break
        query = f"insert into ATTACHMENT values ('{att['mn']}', '{att['mdt']}', '{att['cost']}', '{att['at']}');"
        cur.execute(query)
        con.commit()
        if ch == 1:
            barrel_add(att["mn"], att["mdt"])
        elif ch == 2:
            flashlight_add(att["mn"], att["mdt"])
        elif ch == 3:
            laser_add(att["mn"], att["mdt"])
        elif ch == 4:
            magazine_add(att["mn"], att["mdt"])
        elif ch == 5:
            grip_add(att["mn"], att["mdt"])
        elif ch == 6:
            scope_add(att["mn"], att["mdt"])
    except Exception as e:
        con.rollback()
        print("Failed to insert attachment")
        print(">>>", e)
        input("Press ENTER to continue>")
    return


def barrel_add(mn, mdt):
    try:
        bl = float(input("Barrel length: "))
        query = f"insert into BARREL values ('{mn}', '{mdt}', '{bl}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert barrel")
        print(">>>", e)
    return

def flashlight_add(mn, mdt):
    try:
        rng = float(input("Range: "))
        query = f"insert into FLASHLIGHT values ('{mn}', '{mdt}', '{rng}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert flashlight")
        print(">>>", e)
    return

def laser_add(mn, mdt):
    try:
        wl = float(input("Barrel length: "))
        clr = input("Colour: ")
        rng = input("Range: ")
        query = f"insert into LASER values ('{mn}', '{mdt}', '{wl}', '{clr}', '{rng}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert LASER")
        print(">>>", e)
    return

def magazine_add(mn, mdt):
    try:
        ln = float(input("Magazine length: "))
        cap = int(input("Capacity: "))
        query = f"insert into MAGAZINE values ('{mn}', '{mdt}', '{ln}', '{cap}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert magazine")
        print(">>>", e)
    return

def grip_add(mn, mdt):
    try:
        ln = float(input("Grip length: "))
        mat = input("Material: ")
        query = f"insert into GRIP values ('{mn}', '{mdt}', '{ln}', '{mat}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert grip")
        print(">>>", e)
    return

def scope_add(mn, mdt):
    try:
        typ = input("Scope Type: ")
        zm = float(input("Zoom: "))
        query = f"insert into SCOPE values ('{mn}', '{mdt}', '{typ}', '{zm}');"
        cur.execute(query)
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed to insert scope")
        print(">>>", e)
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
    elif ch == 5:
        choice_attachment()
    elif ch == 6:
        choice_ammo()
    elif ch == 7:
        choice_gunmodel()
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
    username = "enikhil12"
    password = "21lihkine"

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
                print("\n\n\t\tWELCOME TO THE GUN STORE DATABASE!\n\n")
                print(' \n\
 ,________________________________       \n\
|__________,----------._ [____]  ""-,__  __...-----==="\n\
        (_(||||||||||||)___________/   ""             |\n\
           `-----------\'        [ ))"-,               |\n\
                                ""    `,  _,--...___  |\n\
                                        `/          """"\n\
                                        \n\n')
                print("Which information would you like to access today?")
                print("1. Stores")
                print("2. Employees")
                print("3. Customers")
                print("4. Manufacturers")
                print("5. Attachments")
                print("6. Ammo")
                print("7. Gun Models")
                print("10. Logout")
                ch = int(input("Enter choice> "))
                clear()

                if ch == 10:
                    break
                else:
                    choices(ch)
                    input("Enter any key to CONTINUE>")

    except:
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        input("Press ENTER to continue>")
        exit(0)
    
