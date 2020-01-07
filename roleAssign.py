import pymysql

class roleAssign:


    def conn(self):
        connection = pymysql.connect(host='localhost',user='root',password='',charset="utf8mb4")
        return connection

    def roleMaping(self,c):

        #database name: USER_MANAGER
        #SAP table name: AGR_USERS with 2 attribute UNAME(user),AGR_NAME(role))
        
        #Create new Users if not present in SAP
        cursor = c.cursor()
        select_sap = "SELECT uname,agr_name FROM user_manager.agr_users as l LEFT JOIN mysql.default_roles as r on(l.uname=r.user) WHERE uname not in(SELECT user FROM mysql.default_roles)"
        cursor.execute(select_sap)
        rows_insert = cursor.fetchall()
        c.commit()
        rowcount = cursor.rowcount
        if rowcount > 0:
            for row in rows_insert:
                row1 = row[0]
                row2 = row[1]
                createUser = "CREATE USER '"+ row1 +"'@'localhost'"
                cursor.execute(createUser)
                c.commit()
                grantRole = "GRANT '"+ row2 +"' TO '"+ row1 +"'@'localhost'"
                cursor.execute(grantRole)
                c.commit()

                setDefaultRole = "SET DEFAULT ROLE '"+ row2 +"' TO '"+ row1 +"'@'localhost' "
                cursor.execute(setDefaultRole)
                c.commit()
            print("\n\n"+str(rowcount)+" New User Added successfully\n")


        #Upadate role of user if role changed in SAP
        selectUpdate = "SELECT uname,agr_name FROM user_manager.agr_users AS l LEFT JOIN mysql.default_roles AS r ON(l.uname=r.user) WHERE l.uname = r.user AND l.agr_name != r.default_role_user"
        cursor.execute(selectUpdate)
        rows_update = cursor.fetchall()
        c.commit()
        rowcount2 = cursor.rowcount
        
        if rowcount2 > 0:
            for row in rows_update:
                row1 = row[0]
                row2 = row[1]
                select_current_role = "SELECT default_role_user FROM mysql.default_roles WHERE user = '"+ row1 +"' "
                cursor.execute(select_current_role)
                c.commit()
                current_role = cursor.fetchone()
                revoke_old_role = "REVOKE '"+ current_role[0] +"' FROM '"+ row1 +"'@'localhost'"
                cursor.execute(revoke_old_role)
                c.commit()
                grant_new_role = "GRANT '"+ row2 +"' TO '"+ row1 +"'@'localhost'"
                cursor.execute(grant_new_role)
                c.commit()
                set_new_DefaultRole = "SET DEFAULT ROLE '"+ row2 +"' TO '"+ row1 +"'@'localhost'"
                cursor.execute(set_new_DefaultRole)
                c.commit()
            print(str(rowcount2)+" New User Updated successfully\n")

            
        #delete user and assigned role if user is not present in SAP
        selectD = "SELECT user,default_role_user FROM mysql.default_roles WHERE user NOT IN(SELECT uname FROM user_manager.agr_users)"
        cursor.execute(selectD)
        rows_delete = cursor.fetchall()
        c.commit()
        rowcount3 = cursor.rowcount
        if rowcount3 > 0:
            for row in rows_delete:
                row1 = row[0]
                row2 = row[1]
                revoke_role = "REVOKE '"+ row2 +"' From '"+ row1 +"'@'localhost'"
                cursor.execute(revoke_role)
                c.commit()
                drop_user = "DROP user '"+ row1 +"'@'localhost'"
                cursor.execute(drop_user)
                c.commit()
            print(str(rowcount3)+" User Deleted successfully\n")

        print("\nUSER Role mapping successfull\n\n")



userRoles = roleAssign()
c=userRoles.conn()
userRoles.roleMaping(c)
