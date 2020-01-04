import pymysql

class roleAssign:


    def conn(self):
        connection = pymysql.connect(host='localhost',user='root',password='',database='user_manager')
        return connection

    def roleMaping(self,c,option):

        if(option == 0):
            cursor = c.cursor()
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
        else:
            cursor = c.cursor()
            showUser= " select User , default_role_user as ROLE from mysql.default_roles ORDER BY user"
            cursor.execute(showUser)
            c.commit()
            rows = cursor.fetchall()
            print("UNAME     |  ROLE")
            for row in rows:
                l= " "*(13 - len(row[0]))
                print(row[0] + l + row[1])


        
userRoles = roleAssign()
c=userRoles.conn()
userRoles.roleMaping(c,1)