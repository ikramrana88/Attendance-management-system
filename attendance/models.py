from django.db import models
from django.db.migrations.operations.models import CreateModel
from django.db.models.enums import Choices

# from attendance.views import subject

 

# Create your models here.
     
class teachers_detail(models.Model):
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=boolChoice)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    degree = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
 

    def __str__(self):
        return self.first_name +' '+self.last_name



class subjects_detail(models.Model):
    semester_Choice = (
        ("1st","1st"),("2nd","2nd"),("3rd","3rd"),("4th","4th"),("5th","5th"),("6th","6th"),("7th","7th"),("8th","8th")
    )
    departments_Choice = (
        ("Computer Science","Computer Science" ),("Software Engineering","Software Engineering"),("Computer Engineering","Computer Engineering"),("Mechanical Engineering","Mechanical Engineering"),("Electrical Engineering","Electrical Engineering"),("Civil Engineering","Civil Engineering"),("Chemical Engineering","Chemical Engineering")
    )
    subject_name = models.CharField(max_length=50)
    department = models.CharField(max_length=80, choices=departments_Choice)
    semester = models.CharField(max_length=10, choices=semester_Choice)
    teacher_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class students_detail(models.Model):
    boolChoice = (
        ("Male","Male"),("Female","Female")
        )
    semester_Choice = (
        ("1st","1st"),("2nd","2nd"),("3rd","3rd"),("4th","4th"),("5th","5th"),("6th","6th"),("7th","7th"),("8th","8th")
    )
    departments_Choice = (
        ("Computer Science","Computer Science" ),("Software Engineering","Software Engineering"),("Computer Engineering","Computer Engineering"),("Mechanical Engineering","Mechanical Engineering"),("Electrical Engineering","Electrical Engineering"),("Civil Engineering","Civil Engineering"),("Chemical Engineering","Chemical Engineering")
    )
    section_Choice =(
        ("A","A"),("B","B"),("C","C")
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    subject_id = models.ManyToManyField(subjects_detail)
    registration_no = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=boolChoice)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    semester = models.CharField(max_length=10, choices=semester_Choice)
    section = models.CharField(max_length=1, choices=section_Choice)
    department = models.CharField(max_length=80, choices=departments_Choice)


    def __str__(self):
        return self.first_name+' '+self.last_name



class students_attendance(models.Model):
    attendance_Choice =(
        ("Present","Present"),("Absent","Absent")
    )
    date=models.DateField()
    student_id=models.ForeignKey(students_detail, on_delete=models.CASCADE)
    subject_id=models.ForeignKey(subjects_detail, on_delete=models.CASCADE)
    teacher_id=models.ForeignKey(teachers_detail, on_delete=models.CASCADE)
    status=models.CharField(max_length=10, choices=attendance_Choice)
