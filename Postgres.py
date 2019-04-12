import psycopg2

connect_dbname = 'dbname=Netology'
connect_user = 'postgres'
coonect_password = '123154'
# params = {'dbname': 'Netology', 'user': 'postgres', 'password': '123154'}


def create_db(): # создает таблицы
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            cur.execute("CREATE TABLE IF NOT EXISTS student (id serial PRIMARY KEY, name varchar(100),\
             gpa numeric(10, 2), birth timestamp with time zone);")
            cur.execute("CREATE TABLE IF NOT EXISTS course (id serial PRIMARY KEY, name varchar(100));")
            cur.execute("CREATE TABLE IF NOT EXISTS student_course (id serial PRIMARY KEY,\
             student_id integer references student(id) ON DELETE CASCADE,\
             course_id integer references course(id) ON DELETE CASCADE);")


def drop_db(name):
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            cur.execute('DROP TABLE %s;', (name, ))



def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            cur.execute('select student.name from student '
                        'join student_course on student.id = student_course.student_id '
                        'where student_course.course_id = %s;', (course_id, ))
            student_list = list(cur)
    return student_list


def add_course(course_name):
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            cur.execute('insert into course (name) values (%s)', (course_name, ))


def add_students(id_course, students): # создает студентов и записывает их на курс
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            for student in students:
                cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s) returning id',
                (student['name'], student['gpa'], student['birth']))
                student_id = cur.fetchone()[0]
                cur.execute('select exists(select * from course where id = %s);', (id_course, ))
                if cur.fetchone()[0]:
                    cur.execute('insert into student_course (course_id, student_id) values (%s, %s)',
                                (id_course, student_id))
                else:
                     print('No course')


def add_student(student): # просто создает студента
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s)',
                        (student['name'], student['gpa'], student['birth']))


def get_student(student_id):
    with psycopg2.connect(connect_dbname, user=connect_user, password=coonect_password) as con:
        with con.cursor() as cur:
            cur.execute('select * from student where id = %s;', (student_id, ))
            students = cur.fetchone()
    return students



student1 = {'name': 'Иван Иванов', 'gpa': '9.34', 'birth': '1991-01-01'}
student2 = {'name': 'Петр Петров', 'gpa': '9.25', 'birth': '1992-02-02'}
students = [student1, student2]

add_students(6, students)
#create_db()
#drop_db()
#add_student(student2)
#for row in get_students(1):
#    print(row)
#print(get_student(3))
#course_name = 'Java'
#add_course(course_name)
