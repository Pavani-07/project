from django.db import models

# Create your models here.
class BTSubjectInfo(models.Model):

    AYear = models.IntegerField()
    ASem = models.IntegerField()
    BYear = models.IntegerField()
    BSem = models.IntegerField()
    Regulation = models.FloatField()
    Mode = models.CharField(max_length=1)
    Dept = models.IntegerField()
    SubId = models.IntegerField()
    SubCode = models.CharField(max_length=10)
    SubName = models.CharField(max_length=100)
    Credits = models.IntegerField()
    OfferedBy = models.IntegerField()
    Type = models.CharField(max_length=10) 
    Category = models.CharField(max_length=10)
    DistributionRatio = models.TextField()
    Distribution = models.TextField() 
    DistributionNames = models.TextField()
    PromoteThreshold = models.TextField()

    class Meta:
      db_table = 'BTSubjectInfoV'
      managed = False

class BTGradesThreshold(models.Model):
    Grade = models.ForeignKey('ADAUGDB.BTGradePoints', on_delete=models.CASCADE)
    Subject = models.ForeignKey('BTco_ordinator.BTSubjects', on_delete=models.CASCADE)
    RegEventId = models.ForeignKey('ADAUGDB.BTRegistrationStatus', on_delete=models.CASCADE)
    Threshold_Mark = models.FloatField()
    Section = models.CharField(max_length=2, default='NA')
    Exam_Mode = models.BooleanField() 
    #history = HistoricalRecords()
    class Meta:
        db_table = 'BTGradesThreshold'
        unique_together = (('Grade', 'Subject', 'RegEventId', 'Section',"Exam_Mode"))
        managed = True