import pymysql

class roleAssign:


    def conn(self):
        connection = pymysql.connect(host='localhost',user='root',password='',charset="utf8mb4")
        return connection

    def roleMaping(self,c,option):

        if(option == 0):
            print("Enter user name")
            user = input()
            cursor = c.cursor()
            access = "SELECT user,default_role_user from mysql.default_roles WHERE user = '"+ user +"'"
            access = cursor.execute(access)
            allUsers = cursor.fetchall()
            c.commit()
            getUsers = cursor.rowcount
  

            if getUsers > 0:
                print("\nUser found in database\n")
                for getUser in allUsers:
                    #l= " "*(13 - len(row[0]))
                    #print(row[0] + l + row[1])
                    row1 = getUser[0]
                    row2 = getUser[1]
                    tempUser = "select uname,agr_name from user_manager.agr_users where uname = '"+ row1 +"' and agr_name != '"+row2+"'"
                    cursor.execute(tempUser)
                    c.commit()
                    getTempUser = cursor.fetchall()
                    for tempUserIn in getTempUser:
                        row3 = tempUserIn[0]
                        row4 = tempUserIn[1]
                        update = "update table user_manager.agr_users set agr_name = '" + row4 + "' where uname = '"+ row3 +"'"
                        cursor = cursor.execute(update)
                        c.commit()


            elif getUsers == 0:
                print('this user is not availbal on database')
                if user == '':
                    print("User cant be empty")
                else:

                    print("Creating a new user as "+ user)
                    print('Assign role to this user')
                    selectUser = "select user from mysql.user where user = '"+user+"'"
                    cursor.execute(selectUser)
                    c.commit()
                    usercount = cursor.rowcount
                    print(usercount)
                    if usercount > 0:


                        #createUser = "CREATE USER '"+user+"'@'localhost'"
                        #cursor.execute(createUser)
                        #c.commit()

                        print('Enter a number assign with roles:\n1>admin \n2>developer \n3>manager \n4>user_read')
                        rOption = input()
                        if rOption == "1":
                            #revoke = "revoke 'admin' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'admin' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "set default role 'admin' to '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()
                        elif rOption == "2":
                            #revoke = "revoke 'developer' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'developer' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "set default role 'developer' to '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()

                        elif rOption == "3":
                            #revoke = "revoke 'manager' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'manager' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "SET default role 'manager' TO '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()
                        elif rOption == "4":
                            #revoke = "revoke 'user_read' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'user_read' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "set default role 'user_read' to '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()
                        else:
                            print('invalid input\n\n')
                    elif usercount == 0:
                        createUser = "CREATE USER '"+user+"'@'localhost'"
                        cursor.execute(createUser)
                        c.commit()

                        print('Enter a number assign with roles:\n1>admin \n2>developer \n3>manager \n4>user_read')
                        rOption = input()
                        if rOption == "1":
                            #revoke = "revoke 'admin' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'admin' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "set default role 'admin' to '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()
                        elif rOption == "2":
                            #revoke = "revoke 'developer' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'developer' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "set default role 'developer' to '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()

                        elif rOption == "3":
                            #revoke = "revoke 'manager' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'manager' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "SET default role 'manager' TO '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()
                        elif rOption == "4":
                            #revoke = "revoke 'user_read' from '"+ user +"'@'localhost'"
                            #cursor.execute(revoke)
                            grant = "GRANT 'user_read' to '"+ user +"'@'localhost'"
                            cursor.execute(grant)
                            c.commit()
                            setRole = "set default role 'user_read' to '"+ user +"'@'localhost'"
                            cursor.execute(setRole)
                            c.commit()
                        else:
                            print('invalid input\n\n')
                    

        else:
                cursor = c.cursor()
                #showUser= " select User , default_role_user as ROLE from mysql.default_roles ORDER BY user"
                #cursor.execute(showUser)
                #c.commit()
                #rows = cursor.fetchall()
                #print("UNAME     |  ROLE")
                #for row in rows:
                #    l= " "*(13 - len(row[0]))
                #    print(row[0] + l + row[1])
                update = "UPDATE user_manager.agr_users as l JOIN mysql.default_roles as R ON(l.uname=r.user) SET l.agr_name=r.default_role_user where l.uname=r.user"
                cursor.execute(update)
                c.commit()
                #insert = " INSERT INTO user_manager.agr_users (agr_name,uname) SELECT default_role_user,user FROM mysql.default_roles as r where r.user not in(select uname from user_manager.agr_users AS l JOIN mysql.default_roles as r ON(l.uname=r.user) WHERE l.uname=r.user AND l.agr_name not in(select r.default_role_user from r where r.default_role_user not in(select agr_name from user_manager.agr_users)))" 
                #insert = "insert into user_manager.agr_users (agr_name,uname) select default_role_user,user from mysql.default_roles as r where r.user not in(select uname from user_manager.agr_users group by uname Having count(distinct agr_name)>1)"
                insert = "insert into user_manager.agr_users (agr_name,uname) select default_role_user,user from mysql.default_roles as r where r.user not in(select uname from user_manager.agr_users)"

                cursor.execute(insert)
                c.commit()
                delete = " DELETE FROM user_manager.agr_users as l where l.uname NOT IN (SELECT user from mysql.default_roles) "
                cursor.execute(delete)
                c.commit()
                select = "select uname,agr_name from user_manager.agr_users order by uname"
                cursor.execute(select)
                rows = cursor.fetchall()
                c.commit()
                print("UNAME     |  ROLE")
                for row in rows:
                    l= " "*(13 - len(row[0]))
                    print(row[0] + l + row[1])


        
userRoles = roleAssign()
c=userRoles.conn()
userRoles.roleMaping(c,0)
userRoles.roleMaping(c,1)
