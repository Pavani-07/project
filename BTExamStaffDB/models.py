from django.db import models

# Create your models here.
class BTStudentInfo(models.Model):
    CYCLE_CHOICES = (
        (10, 'PHYSICS'),
        (9, 'CHEMISTRY')
    )
    RegNo = models.IntegerField()
    RollNo = models.IntegerField()
    Name = models.CharField(max_length=255)
    Regulation = models.FloatField()
    Dept = models.IntegerField()
    AdmissionYear = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Category = models.CharField(max_length=30)
    GuardianName = models.CharField(max_length=255)
    Phone = models.TextField()
    email = models.TextField()
    Address1 = models.TextField()
    Address2 = models.TextField(null=True)
    cycle = models.IntegerField(default=0, choices=CYCLE_CHOICES)
    # history = HistoricalRecords()

    class Meta:
        db_table = 'BTStudentInfo'

        constraints = [
          models.UniqueConstraint(fields=['RegNo'], name='unique_BTStudent Info_RegNo'),
          models.UniqueConstraint(fields=['RollNo'], name='unique_BTStudentInfo_RollNo'),
        ]
        managed=True


class BTFacultyInfo (models.Model):
    FacultyId = models.IntegerField(default=100)
    Name = models.CharField(max_length=255)
    Phone = models.TextField()
    Email = models.CharField(max_length=255)
    Dept = models.IntegerField()
    Working = models.BooleanField()
    #history = HistoricalRecords()

    class Meta:
      db_table = 'BTFacultyInfo'
      constraints = [
      models. UniqueConstraint(fields=['FacultyId'], name='unique_BTfacultyinfo_facultyid')
      ]
      managed = True


# #HONORS

# class HNStudent(models.Model): 
#     RegNo = models.IntegerField()
#     RollNo = models.IntegerField()
#     Name = models.CharField(max_length=255)
#     Dept = models.IntegerField()
#     AdmissionYear = models.IntegerField() 
#     Phone = models.TextField()
#     email = models.TextField()
#     class Meta: 
#         db_table = 'HNStudent' 
#         constraints = [
#                   models.UniqueConstraint(fields=['RegNo'], name='unique_HNStudent_RegNo'),
#                   models.UniqueConstraint(fields=['RollNo'], name='unique_HNStudent_RollNo'),
#                 ] 
#         managed = False 