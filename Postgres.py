import psycopg2

def create_db(): # создает таблицы
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute("CREATE TABLE student (id serial PRIMARY KEY, name varchar(100),\
             gpa numeric(10, 2), birth timestamp with time zone);")
            cur.execute("CREATE TABLE course (id serial PRIMARY KEY, name varchar(100));")
            cur.execute("CREATE TABLE student_course (id serial PRIMARY KEY,\
             student_id integer references student(id), course_id integer references course(id));")

def drop_db(name):
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('DROP TABLE %s;', (name, ))


def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('select student.name from student '
                        'join student_course on student.id = student_course.student_id '
                        'where student_course.course_id = %s;', (course_id, ))
            for row in cur:
                print(row)


def add_course(course_name):
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('insert into course (name) values (%s)', (course_name, ))


def add_students(id_course, students): # создает студентов и записывает их на курс
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            for student in students:
                cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s) returning id',
                (student['name'], student['gpa'], student['birth']))
                student_id = cur.fetchone()[0]
                cur.execute('insert into student_course (course_id, student_id) values (%s, %s)',
                (id_course, student_id))


def add_student(student): # просто создает студента
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s)',
                        (student['name'], student['gpa'], student['birth']))


def get_student(student_id):
    with psycopg2.connect('dbname=Netology', user="postgres", password='123154') as con:
        with con.cursor() as cur:
            cur.execute('select * from student where id = %s;', (student_id, ))
            print(cur.fetchone())



student1 = {'name': 'Иван Иванов', 'gpa': '9.34', 'birth': '1991-01-01'}
student2 = {'name': 'Петр Петров', 'gpa': '9.25', 'birth': '1992-02-02'}
students = [student1, student2]

#add_students(1, students)
#create_db()
#drop_db()
#add_student(student2)
get_students(1)
#get_student(25)
#course_name = 'Java'
#add_course(course_name)
