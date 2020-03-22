import jaydebeapi, os


def main():

    dsn_database = "dev"
    dsn_hostname = "postgres_host"
    dsn_port = "13013"
    dsn_uid = "username"
    dsn_pwd = "password"
    jdbc_driver_name = "org.postgresql.Driver"
    jdbc_driver_loc = os.path.join(r'D:\Jar\postgresql-9.3-1100-jdbc41.jar')

    sql_str = "select version()"

    connection_string='jdbc:postgresql://'+ dsn_hostname+':'+ dsn_port +'/'+ dsn_database

    url = '{0}:user={1};password={2}'.format(connection_string, dsn_uid, dsn_pwd)
    print("Connection String: " + connection_string)

    conn = jaydebeapi.connect(jdbc_driver_name, connection_string, {'user': dsn_uid, 'password': dsn_pwd},
    jars=jdbc_driver_loc)

    curs = conn.cursor()
    curs.execute(sql_str)
    result = curs.fetchall()

    print(result[0])

# Run Interpreter
if __name__ == "__main__":
    main()