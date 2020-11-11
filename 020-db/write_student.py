from Model import *

session = get_session()

new_student = Student(name = 'Robert')

session.add(new_student)
session.commit()



