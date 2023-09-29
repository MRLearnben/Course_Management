import mysql.connector

try:
    my_conn=mysql.connector.connect(host='127.0.0.1',user='root',port="3306",database="thilak",password="Thilak@2003",auth_plugin='mysql_native_password')
    my_cursor=my_conn.cursor()
    print("You are connected")
except Exception as e:
    print("Error",e)