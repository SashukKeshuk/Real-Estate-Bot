from config import db_name, host, user, password
import pymysql

new_table_query = "CREATE TABLE `users` (id int AUTO_INCREMENT, name varchar(32), password varchar(32), email varchar(32), PRIMARY KEY (id));"
insert_line_query = "INSERT INTO `articles` (text, cost, type, house_type, rooms, city) VALUES ('cool house!', 999, 1, 1, '3+1.5', 'Stambool');"
select_all_lines = "SELECT * FROM `users`"
edit_data = "UPDATE `articles` SET text = 'XxxX' WHERE id = 1;"
delete_query = "DELETE FROM `articles` WHERE id = 1;"
drop_query = "DROP TABLE `users`;"

def add_line(s):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(s)
        connection.commit()
    disconnect()

def save(uid, aid):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO `saved` (user_id, article_id) VALUES ({uid}, '{aid}')")
        connection.commit()
    disconnect()

def get_saved(uid):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT article_id FROM `saved` WHERE user_id = {uid}")
        saved_art = cursor.fetchall()
    disconnect()
    return saved_art

def get_by_id(id):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM `articles` WHERE id = {id}")
        p = cursor.fetchall()
    disconnect()
    return p

def get_lines(s):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(s)
        lines = cursor.fetchall()
    disconnect()
    return lines

def del_line(s):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(s)
        connection.commit()
    disconnect()

def update_line(s):
    connect()
    with connection.cursor() as cursor:
        cursor.execute(s)
        connection.commit()
    disconnect()

def connect():
    try:
        global connection
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("connected")
    except Exception as e:
        print('failed to connect\n')
        print(e)

def disconnect():
    try:
        connection.close()
    finally:
        print('disconnected')


            #add_line(insert_line_query)

            #cursor.execute(delete_query)
            #connection.commit()
            #lines = cursor.fetchall()
            #print('#' * 20)
            #for line in lines:
            #    print(line)
            #print('#' * 20)
            #for save after insert/edit/delete data in db - connection.commit()