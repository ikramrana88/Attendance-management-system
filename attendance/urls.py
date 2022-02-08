from django.contrib import admin
from django.urls import path
from attendance import views

urlpatterns = [
    path("", views.index, name='welcome'),
    path("login", views.loginuser, name='login'),
    path("home", views.home, name='home'),
    path("teachers", views.teacher, name='teacher'),
    path("addteacher", views.addteacher, name='addteacher'),
    path("students", views.student, name='student'),
    path("addstudent", views.addstudent, name='addstudent'),
    path("subjects", views.subject, name='subject'),
    path("addsubject", views.addsubject, name='addsubject'),
    path("reports", views.reports, name='reports'),
    path("takeattendance", views.takeattendance, name='takeattendance'),
    path("logout", views.logoutuser, name='logout'),
    path("teacher-login", views.teacherlogin, name='teacher-login'),
    path("teacher-home", views.teacherhome, name='teacher-home'),
    path("addstudents", views.addstudents, name='addstudents'),
    path("addsubjects", views.addsubjects, name='addsubjects'),
    path("report", views.report, name='report'),
    path("student", views.students, name='students'),
    path("subject", views.subjects, name='subjects'),
    path("attendance", views.attendance, name='attendance'),
    path("teacher", views.teachers, name='teachers')


]
