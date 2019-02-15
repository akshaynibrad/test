import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demoproject.settings')
django.setup()

from demoapp.models import College, Student


def insert_college():
    new_college_obj = College(college_name='SIOMS',
                              college_city='Pune')
    new_college_obj.save()
    print 'College = ', new_college_obj.college_name
    return


def insert_student():
    college_obj = College.objects.get(college_name='SIOMS')
    new_student_obj_ak = Student(name='Akshay', city='Pune',
                              college_id=1)
    new_student_obj_ak.save()
    new_student_obj_as = Student(name='Ashvini', city='Pune',
                              college=college_obj)
    new_student_obj_as.save()
    new_student_obj_am = Student(name='Amit', city='Pune',
                                 college_id=college_obj.id)
    new_student_obj_am.save()
    # print 'College = ', new_student_obj.name
    return


def select_data():
    for student_obj in Student.objects.all():
        print student_obj.name, student_obj.city, student_obj.college.college_name, student_obj.college.college_city


if __name__ == "__main__":
    # insert_college()
    # insert_student()
    select_data()
    pass



