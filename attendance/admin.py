from django.contrib import admin
from attendance.models import students_detail, subjects_detail, teachers_detail, students_attendance

# Register your models here.
admin.site.register(teachers_detail)
admin.site.register(subjects_detail)
admin.site.register(students_detail)
admin.site.register(students_attendance)
