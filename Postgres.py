import psycopg2

connect_dbname = 'dbname=Netology'
connect_user = 'postgres'
coonect_password = '123154'
connect_params = {'dbname': 'Netology', 'user': 'postgres', 'password': '123154'}


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
    with psycopg2.connect(**connect_params) as con:
        with con.cursor() as cur:
            cur.execute('DROP TABLE %s;', (name, ))


def get_students(course_id): # возвращает студентов определенного курса
    with psycopg2.connect(**connect_params) as con:
        with con.cursor() as cur:
            cur.execute('select student.name from student '
                        'join student_course on student.id = student_course.student_id '
                        'where student_course.course_id = %s;', (course_id, ))
            student_list = list(cur)
    return student_list


def add_course(course_name):
    with psycopg2.connect(**connect_params) as con:
        with con.cursor() as cur:
            cur.execute('insert into course (name) values (%s)', (course_name, ))


def add_params(student):
    params = f"insert into student (name, gpa, birth) values ('{student['name']}', " \
        f"{student['gpa']}, '{student['birth']}') returning id"
    return params


def add_student(student): # просто создает студента
    with psycopg2.connect(**connect_params) as con:
        with con.cursor() as cur:
            cur.execute(add_params(student))


def add_students(id_course, students): # создает студентов и записывает их на курс
    with psycopg2.connect(**connect_params) as con:
        with con.cursor() as cur:
            cur.execute('select exists(select * from course where id = %s);', (id_course,))
            if cur.fetchone()[0]:
                for student in students:
                    cur.execute(add_params(student))
                    student_id = cur.fetchone()[0]
                    cur.execute('insert into student_course (course_id, student_id) values (%s, %s)',
                                (id_course, student_id))
            else:
                print('No course')


def get_student(student_id):
    with psycopg2.connect(**connect_params) as con:
        with con.cursor() as cur:
            cur.execute('select * from student where id = %s;', (student_id, ))
            students = cur.fetchone()
    return students



student1 = {'name': 'Иван Иванов', 'gpa': '9.34', 'birth': '1991-01-01'}
student2 = {'name': 'Петр Петров', 'gpa': '9.25', 'birth': '1992-02-02'}
student3 = {'name': 'Сидр Сидров', 'gpa': '9.55', 'birth': '1992-03-03'}
students = [student1, student2, student3]


# for student in get_students(4):
#     print(student)
#add_params(student3)
#add_student(student3)
#add_student(student2)
#add_students(7, students)
#create_db()
#print(get_student(3))
#course_name = 'Marketing'
#add_course(course_name)
