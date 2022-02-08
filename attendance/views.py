from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from attendance.models import teachers_detail
from attendance.models import subjects_detail
from attendance.models import students_detail
from attendance.models import students_attendance
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
 

# Create your views here.

def index(request):
    return render(request, 'welcome.html')

def loginuser(request):
    if request.method=="POST":
        loginusername = request.POST['username']
        loginpassword = request.POST['password']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('home')
        else:
             # No backend authenticated the credentials
            return render(request, 'login2.html')
             


    return render(request, 'login2.html')
    

def home(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'home.html')


def teacher(request):
    if request.user.is_anonymous:
        return redirect('/login')

    data = teachers_detail.objects.all()
    tech = {
    "teachers_info": data
    }

    return render(request, 'teacher.html', tech)

def addteacher(request):
    if request.user.is_anonymous:
        return redirect('/login')


    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        degree = request.POST['degree']
        designation = request.POST['designation']
        teacher = teachers_detail(first_name= first_name, last_name=last_name, date_of_birth=date_of_birth,gender=gender, phone_number=phone_number, email=email, degree=degree, designation=designation)
        teacher.save(teachers_detail)
    


    return render(request, 'addteacher.html')



def student(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    data = students_detail.objects.all()
    stu = {
    "students_info": data
    }


    return render(request, 'student.html', stu)


def addstudent(request):
    if request.user.is_anonymous:
        return redirect('/login')

    
    if request.method=="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        registration_no = request.POST['registration_no']
        date_of_birth = request.POST["date_of_birth"]
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        semester = request.POST['semester']
        section = request.POST['section']
        department = request.POST['department']
        student = students_detail(first_name= first_name, last_name=last_name,registration_no=registration_no, date_of_birth=date_of_birth,gender=gender, phone_number=phone_number, email=email,semester=semester, section=section, department=department)
        student.save(students_detail)


    return render(request, 'addstudent.html')



def subject(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    data = subjects_detail.objects.all()
    sub = {
    "subjects_info": data
    }

    return render(request, 'subject.html', sub)

def addsubject(request):
    if request.user.is_anonymous:
        return redirect('/login')
    
    
    if request.method=="POST":
        subject_name = request.POST['subject_name']
        department = request.POST['department']
        semester = request.POST['semester']
        teacher_name = request.POST['teacher_name']
        subject = subjects_detail(subject_name=subject_name, department=department, semester=semester, teacher_name=teacher_name)
        subject.save(subjects_detail)



    return render(request, 'addsubject.html')

def reports(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request, 'reports.html')

def takeattendance(request):
    if request.user.is_anonymous:
        return redirect('/login')
        
    data = students_detail.objects.all()
    stud = {
    "students_info": data
    }

    return render(request, 'Takeattendance.html', stud)


def logoutuser(request):
    logout(request)
    return redirect("/")



def teacherlogin(request):
    if request.method=="POST":
        username2 = request.POST['username']
        password2 = request.POST['password']

        user = authenticate(username=username2, password=password2)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect('teacher-home')
        else:
             # No backend authenticated the credentials
             return render(request, 'teacher-login.html')


    return render(request, 'teacher-login.html')
 
def teacherhome(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    return render(request, 'teacher-home.html')

def addstudents(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    return render(request, 'addStudents.html')

def addsubjects(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    return render(request, 'addSubjects.html')

def report(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    return render(request, 'report.html')

def students(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    data = students_detail.objects.all()
    stu = {
    "students_info": data
    }

    return render(request, 'students.html', stu)

def subjects(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    data = subjects_detail.objects.all()
    sub = {
    "subjects_info": data
    }

    return render(request, 'subjects.html', sub)

def attendance(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    return render(request, 'attendance.html')

def teachers(request):
    if request.user.is_anonymous:
        return redirect('/teacher-login')
    
    data = teachers_detail.objects.all()
    tech = {
    "teachers_info": data
    }
    
    return render(request, 'teachers.html', tech)
