# Generated by Django 3.2.8 on 2021-12-20 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20211129_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='students_attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.students_detail')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.subjects_detail')),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.teachers_detail')),
            ],
        ),
    ]
