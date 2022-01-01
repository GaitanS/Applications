import mysql.connector as mysql
import datetime


def create_structure():
    conn = mysql.connect(host='localhost', user='root', password='Frectie!234')
    with conn.cursor() as c:
        c.execute('CREATE DATABASE IF NOT EXISTS db_tasks;')
        c.execute('CREATE TABLE IF NOT EXISTS db_tasks.tasks ('
                  'id INTEGER PRIMARY KEY AUTO_INCREMENT NOT NULL,'
                  'task TEXT NOT NULL,'
                  'done BOOLEAN NOT NULL DEFAULT 0);')
    conn.close()


def show_menu1():
    print('1.show task list')
    print('2.mark task as done')
    print('3.add new task')
    print('4.exit application')


create_structure()

conn = mysql.connect(host='localhost', user='root', password='Frectie!234', database='db_tasks')


def populare1():
    with conn.cursor() as c:
        c.execute(f'''INSERT INTO tasks (task) VALUES ('To do234') ;''')
        conn.commit()


def show_task_list():
    with conn.cursor() as c:
        c.execute(f"SELECT * FROM tasks ORDER BY id")
        results = c.fetchall()
        for result in results:
            print(result)


def mark_task_as_done():
    with conn.cursor() as c:
        c.execute(f"SELECT * FROM tasks ORDER BY id")
        results = c.fetchall()
        for result in results:
            print(result)
        task_name = int(input(f'Which id to mark as done : '))
        c.execute(f'UPDATE tasks SET done=1 WHERE id={task_name} AND done=0')
        conn.commit()


def add_new_task():
    with conn.cursor() as c:
        task_name = input(f'Enter a new task : ')
        c.execute(f'''INSERT INTO tasks (task) VALUES ('{task_name}') ;''')
        conn.commit()
        print('Task added!')


# populare1()

while True:
    show_menu1()
    option = int(input(f'Enter your option: '))
    if option == 4:
        break
    elif option == 1:
        show_task_list()
    elif option == 2:
        mark_task_as_done()
    elif option == 3:
        add_new_task()
