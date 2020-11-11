from Model import *

session = get_session()

student_query = session.query(Student)
                    .filter(Student.name.contains('Rob'))

print(student_query.count())
for student in student_query.all():
    print(student.id, student.name)