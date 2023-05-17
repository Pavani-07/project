# Generated by Django 4.1.7 on 2023-04-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BTFacultyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FacultyId', models.IntegerField(default=100)),
                ('Name', models.CharField(max_length=255)),
                ('Phone', models.TextField()),
                ('Email', models.CharField(max_length=255)),
                ('Dept', models.IntegerField()),
                ('Working', models.BooleanField()),
            ],
            options={
                'db_table': 'BTFacultyInfo',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BTStudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RegNo', models.IntegerField()),
                ('RollNo', models.IntegerField()),
                ('Name', models.CharField(max_length=255)),
                ('Regulation', models.FloatField()),
                ('Dept', models.IntegerField()),
                ('AdmissionYear', models.IntegerField()),
                ('Gender', models.CharField(max_length=10)),
                ('Category', models.CharField(max_length=30)),
                ('GuardianName', models.CharField(max_length=255)),
                ('Phone', models.TextField()),
                ('email', models.TextField()),
                ('Address1', models.TextField()),
                ('Address2', models.TextField(null=True)),
                ('cycle', models.IntegerField(choices=[(10, 'PHYSICS'), (9, 'CHEMISTRY')], default=0)),
            ],
            options={
                'db_table': 'BTStudentInfo',
                'managed': True,
            },
        ),
        migrations.AddConstraint(
            model_name='btstudentinfo',
            constraint=models.UniqueConstraint(fields=('RegNo',), name='unique_BTStudent Info_RegNo'),
        ),
        migrations.AddConstraint(
            model_name='btstudentinfo',
            constraint=models.UniqueConstraint(fields=('RollNo',), name='unique_BTStudentInfo_RollNo'),
        ),
        migrations.AddConstraint(
            model_name='btfacultyinfo',
            constraint=models.UniqueConstraint(fields=('FacultyId',), name='unique_BTfacultyinfo_facultyid'),
        ),
    ]