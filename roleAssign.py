import pymysql

class roleAssign:


    def conn(self):
        connection = pymysql.connect(host='localhost',user='root',password='',charset="utf8mb4")
        return connection

    def roleMaping(self,c):
        

        cursor = c.cursor()
        selectSap = "SELECT uname,agr_name FROM user_manager.agr_users as l LEFT JOIN mysql.default_roles as r on(l.uname=r.user) WHERE uname not in(SELECT user FROM mysql.default_roles)"
        cursor.execute(selectSap)
        rowsC = cursor.fetchall()
        c.commit()
        rowcount = cursor.rowcount
        if rowcount > 0:
            for row in rowsC:
                row1 = row[0]
                row2 = row[1]
                createUser = "CREATE USER '"+ row1 +"'@'localhost'"
                cursor.execute(createUser)
                c.commit()
                grantRole = "GRANT '"+ row2 +"' to '"+ row1 +"'@'localhost'"
                cursor.execute(grantRole)
                c.commit()

                setDefaultRole = "SET DEFAULT ROLE '"+ row2 +"' TO '"+ row1 +"'@'localhost' "
                cursor.execute(setDefaultRole)
                c.commit()

        selectUpdate = "SELECT uname,agr_name FROM user_manager.agr_users as l LEFT JOIN mysql.default_roles as r on(l.uname=r.user) WHERE l.uname = r.user and l.agr_name != r.default_role_user"
        cursor.execute(selectUpdate)
        rowsU = cursor.fetchall()
        c.commit()
        rowcount2 = cursor.rowcount
        
        if rowcount2 > 0:
            for row in rowsU:
                row1 = row[0]
                row2 = row[1]
                select_current_role = "SELECT default_role_user from mysql.default_roles where user = '"+ row1 +"' "
                cursor.execute(select_current_role)
                c.commit()
                current_role = cursor.fetchone()
                revokeR = "REVOKE '"+ current_role[0] +"' FROM '"+ row1 +"'@'localhost'"
                cursor.execute(revokeR)
                c.commit()
                grantUR = "GRANT '"+ row2 +"' TO '"+ row1 +"'@'localhost'"
                cursor.execute(grantUR)
                c.commit()
                setUDefaultRole = "SET DEFAULT ROLE '"+ row2 +"' TO '"+ row1 +"'@'localhost'"
                cursor.execute(setUDefaultRole)
                c.commit()
        selectD = "select user,default_role_user from mysql.default_roles where user not in(select uname from user_manager.agr_users)"
        cursor.execute(selectD)
        rowsD = cursor.fetchall()
        c.commit()
        rowcount3 = cursor.rowcount
        if rowcount3 > 0:
            for row in rowsD:
                row1 = row[0]
                row2 = row[1]
                revokeD = "REVOKE '"+ row2 +"' From '"+ row1 +"'@'localhost'"
                cursor.execute(revokeD)
                c.commit()
                dropU = "DROP user '"+ row1 +"'@'localhost'"
                cursor.execute(dropU)
                c.commit()



userRoles = roleAssign()
c=userRoles.conn()
userRoles.roleMaping(c)
