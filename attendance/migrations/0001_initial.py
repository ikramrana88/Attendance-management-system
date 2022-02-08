# Generated by Django 3.2.8 on 2021-11-11 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='subjects_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=80)),
                ('semester', models.CharField(choices=[('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('4th', '4th'), ('5th', '5th'), ('6th', '6th'), ('7th', '7th'), ('8th', '8th')], max_length=10)),
                ('teacher_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='teachers_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('degree', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='students_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('registration_no', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('semester', models.CharField(max_length=10)),
                ('section', models.CharField(max_length=1)),
                ('department', models.CharField(max_length=80)),
                ('subject_id', models.ManyToManyField(to='attendance.subjects_detail')),
            ],
        ),
    ]
