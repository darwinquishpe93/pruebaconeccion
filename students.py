from peewee import *

db=SqliteDatabase('prueba.db')

class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)


    class Meta:
        database=db

students=[
    {'username':'aldo',
      'points':8},

      {'username':'granja',
        'points':10},

    {'username':'martin',
      'points':8},
      ]

def add_students():
    for student in students:
        try:
        #crear mi registro
        #metodo
            Student.create(username=student['username'],
                            points=student['points'])

        except IntegrityError:
            student_records= Student.get(username=student['username'])
            student_records.points=student['points']
            student_records.save()#guardar cambiios

#que obtenga al estudainte con mayor calificacion
def top_student():
    topcalif= Student.select().order_by(Student.points.desc()).get()
    return topcalif


if  __name__ == '__main__':

    db.connect()
    db.create_tables([Student],safe = True)
    add_students()
    print('El mejor estudiante es {}'.format(top_student().username))
