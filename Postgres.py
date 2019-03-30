import psycopg2

student1 = {'name': 'Иван Иванов', 'gpa': '9.34', 'birth': '1991-01-01'}
student2 = {'name': 'Петр Петров', 'gpa': '9.25', 'birth': '1992-02-02'}

def create_db(): # создает таблицы
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute("CREATE TABLE student (id serial PRIMARY KEY, name varchar(100),\
             gpa numeric(10, 2), birth timestamp with time zone);")
            cur.execute("CREATE TABLE course (id serial PRIMARY KEY, name varchar(100));")
            cur.execute("CREATE TABLE student_course (id serial PRIMARY KEY,\
             student_id integer references student(id), course_id integer references course(id));")

def drop_db1():
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('DROP TABLE student;')

def drop_db2():
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('DROP TABLE course;')

def get_students(course_id): # возвращает студентов определенного курса
    pass

def add_course(course_name):
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('insert into course (name) values (%s)', (course_name))

def add_students(course_id, students): # создает студентов и записывает их на курс
    pass


def add_student(student): # просто создает студента
    pass

def get_student(student_id):
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('select 1 from student', (student_id))
            print(cur)


#create_db()
#drop_db2()
#add_student(student2)
#get_student(1)
