from django.db import models
import math
from BTco_ordinator.models import BTSubjects

# Create your models here.

class BTStudentGrades (models.Model):

    RegId = models.ForeignKey('BTco_ordinator.BTStudentRegistrations', db_column='RegId', on_delete=models.CASCADE)
    RegEventId = models.IntegerField()
    Regulation = models.FloatField()
    Grade = models.CharField(max_length=2)
    AttGrade = models.CharField(max_length=2)
    #history = HistoricalRecords()
    class Meta:
      db_table = 'BTStudentGrades'
      constraints = [
      models. UniqueConstraint (fields=['RegId'], name='unique_BTStudentGrades_registration')
      ]
      managed = True



class BTMarks (models.Model):
    Registration = models.ForeignKey('BTco_ordinator.BTStudentRegistrations', on_delete=models.CASCADE)
    Marks = models.TextField()
    TotalMarks = models.IntegerField()
    #history = HistoricalRecords()
    class Meta:
      db_table = 'BTMarks'

      constraints = [ 
          models.UniqueConstraint(fields=['Registration'], name='unique_BTmarks_registration') 
      ]
      managed = True

    def get_total_marks(self):
        marks_dis = self.Marks.split(',')
        marks_dis = [mark.split('+') for mark in marks_dis]
        subject = BTSubjects.objects.filter(id=self.Registration.sub_id.id).first()
        ratio = subject.DistributionRatio.split(':')
        total_parts = 0
        for part in ratio:
          total_parts += int(part)
        total = 0
        for index in range(len(marks_dis)):
          marks_row = marks_dis[index]
          sub_total = 0
          for mark in marks_row:
            sub_total += float(mark)
          total = sub_total*int (ratio[index])+ total #added total here,otherwise previous result will be lost
        return math.ceil(total/total_parts)


#HONORS

# class HNStudentGrades (models.Model):
#     HNRegId = models.ForeignKey('BTco_ordinator.HNStudentRegistrations', db_column='HNRegId', on_delete=models.CASCADE)
#     RegEventId = models.IntegerField()
#     Regulation = models.FloatField()
#     Grade = models.CharField(max_length=2)
#     AttGrade = models.CharField(max_length=2)
#     #history = HistoricalRecords()
#     class Meta:
#       db_table = 'HNStudentGrades'
#       constraints = [
#       models. UniqueConstraint (fields=['HNRegId'], name='unique_HNStudentGrades_registration')
#       ]
#       managed = True



# class HNMarks (models.Model):
#     HNRegistration = models.ForeignKey('BTco_ordinator.HNStudentRegistrations', on_delete=models.CASCADE)
#     Marks = models.TextField()
#     TotalMarks = models.IntegerField()
#     #history = HistoricalRecords()
#     class Meta:
#       db_table = 'HNMarks'

#       constraints = [ 
#           models.UniqueConstraint(fields=['HNRegistration'], name='unique_HNmarks_registration') 
#       ]
#       managed = True

#     def get_total_marks(self):
#         marks_dis = self.Marks.split(',')
#         marks_dis = [mark.split('+') for mark in marks_dis]
#         subject = BTSubjects.objects.filter(id=self.Registration.sub_id.id).first()
#         ratio = subject.DistributionRatio.split(':')
#         total_parts = 0
#         for part in ratio:
#           total_parts += int(part)
#           total = 0
#         for index in range(len(marks_dis)):
#           marks_row = marks_dis[index]
#           sub_total = 0
#         for mark in marks_row:
#           sub_total += float(mark)
#           total = sub_total*int (ratio[index])
#         return math.ceil(total/total_parts)
