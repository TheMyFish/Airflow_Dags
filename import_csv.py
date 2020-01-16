import csv

def bulk_insert(table_name, **kwargs):

    mysqlConnection = MySqlHook(mysql_conn_id='id_db')
    a = mysqlConnection.get_conn()
    c = a.cursor()

    with open('arquivo.csv') as f: 
        reader = csv.reader(f, delimiter='\t')

        sql ="""INSERT INTO user (id,user_name) VALUES""" 

            for row in reader:
                sql ="""INSERT INTO user (id,user_name) VALUES"""            
                sql +="(" + row[0] + " , '" + row[1] + "'),"
            c.execute(sql[:-1])  

    a.commit()