from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BTCourses (models.Model):
    SubCode = models.CharField(max_length=10)
    SubName = models.CharField(max_length=255)
    Credits = models.IntegerField()
    OfferedBy = models.IntegerField()
    CourseStructure = models.ForeignKey("ADAUGDB.BTCourseStructure", on_delete=models.CASCADE)
    lectures = models.IntegerField()
    tutorials = models.IntegerField()
    practicals = models.IntegerField()
    DistributionRatio = models.TextField()
    MarkDistribution = models.ForeignKey("ADAUGDB.BTMarksDistribution", on_delete=models.CASCADE)
    # history = HistoricalRecords()
    class Meta:
        db_table = 'BTCourses'
        constraints = [
          models.UniqueConstraint(fields = ['SubCode', 'SubName', 'CourseStructure', 'DistributionRatio', 'MarkDistribution'], name="BTCourses_unique_course")
        ]
        managed = True


class BTMarksDistribution (models.Model):
    Regulation = models.FloatField()
    Distribution = models.TextField()
    DistributionNames = models.TextField()
    PromoteThreshold = models.TextField()
    # history = HistoricalRecords()
    class Meta:
      db_table = 'BTMarksDistribution'
      unique_together = (('Regulation', 'Distribution', 'DistributionNames', 'PromoteThreshold'))
      managed = True

    def str(self):
      return str(self.Distribution)+', '+str(self.PromoteThreshold)

    def distributions (self):
      distributions_names = self.DistributionNames.split(",") 
      distributions_marks = self.Distribution.split(',')
      CHOICES = [] 
      outer_index = 0
      for names, marks in zip(distributions_names, distributions_marks):
        names = names.split('+')
        marks = marks.split('+')
        inner_index = 0
        for n,m in zip(names, marks):
          CHOICES += [(str(outer_index)+', '+str(inner_index), str(n)+', '+str(m))]
          inner_index += 1
        outer_index += 1
      return CHOICES

    def get_zeroes_string(self):
      distribution_marks = self.Distribution.split(',')
      marks = [row.split("+") for row in distribution_marks]
      zero_marks = [['0' for mark in range(len(row))] for row in marks]
      zero_marks = ['+'.join(mark) for mark in zero_marks] 
      zero_marks = ','.join(zero_marks)
      return zero_marks
    
    def get_marks_limit(self, outer, inner):
      return int(self.Distribution.split(',') [outer].split("+")[inner])

    def get_excel_column_index(self, outer, inner):
      distribution_marks = self.Distribution.split(',') 
      marks = [row.split('+') for row in distribution_marks]
      index = 3
      #index starts from 1 availing for the roll number (index=0) and name(index-1) rows in excel sheet.
      for num in range(outer):    
        index += len(marks [num])
      index += inner
      return index
    

class BTHOD(models.Model):
    Faculty = models.ForeignKey('BTExamStaffDB.BTFacultyInfo', on_delete=models.CASCADE)
    Dept = models.IntegerField()
    AssignedDate = models.DateTimeField (auto_now_add=True)
    RevokeDate = models.DateTimeField(null=True)
    User =models.ForeignKey(User, on_delete=models. CASCADE)
    #history = HistoricalRecords()
    class Meta:
        db_table = 'BTHOD'
        unique_together = (('Faculty', 'Dept', 'AssignedDate'))
        managed = True


class BTCourseStructure(models.Model):
    BYear = models.IntegerField()
    BSem = models.IntegerField()
    Dept = models.IntegerField() 
    Regulation = models.FloatField() 
    Category = models.CharField(max_length=10) 
    Type = models.CharField(max_length=10) 
    Creditable = models.IntegerField()
    Credits = models.IntegerField()
    count = models.IntegerField()
    Rigid = models.BooleanField()
    #history = Historical Records()
    class Meta:

        db_table = 'BTCourseStructure'
        constraints = [
          models. UniqueConstraint(fields=['Category', 'Type', 'Creditable', 'Credits', 'Regulation', 'BYear', 'BSem', 'Dept'], name='Unique BTCourseStructureId')
        ]
        managed = True


class BTRegistrationstatus (models.Model):
    AYear= models.IntegerField() 
    ASem= models.IntegerField()
    BYear= models.IntegerField()
    BSem = models.IntegerField()
    Regulation = models.FloatField()
    Dept = models.IntegerField() 
    Mode = models.CharField(max_length=1) # R for Regular B for Backlog 
    Status = models.IntegerField() 
    RollListstatus = models.IntegerField()
    RollListFeeStatus = models.IntegerField() 
    OERollListStatus = models.IntegerField()
    OERegistrationStatus = models.IntegerField()
    RegistrationStatus = models.IntegerField() 
    MarksStatus = models.IntegerField()
    Gradestatus = models.IntegerField()

    #history = Historical Records()

    class Meta:
        db_table = 'BTRegistration_Status'
        constraints = [
          models.UniqueConstraint(fields=['AYear', 'ASem', 'BYear', 'BSem', 'Regulation', 'Dept', 'Mode'], name='unique BTRegistrationstatus')
        ]
        managed = True

        # def str(self):
        #   name = str(DEPARTMENTS[self.Dept-1]) + ':' + str(YEARS[self.BYear]) + ':' + str(SEMS[self.BSem])+ ':'+  str(self.AYear) + ':' + str(self.ASem) + ':' + str(self.Regulation) + ':' + str(self.Mode)
        #   return name

        # def open_str(self):
        #   name = str(YEARS[self.BYear]) + ':' + str(SEMS[self.BSem]) +':'+ str(self.AYear) + ':' + str(self.ASem) + ':' + str(self.Regulation) + ':' + str(self.Mode)
        #   return name
        
class BTGradePoints(models.Model):
    Regulation = models.FloatField()
    Grade = models.CharField(max_length=2)
    Points = models.IntegerField()
    #history = HistoricalRecords()
    
    class Meta:
        db_table = 'BTGradePoints'
        unique_together = (('Regulation', 'Grade', 'Points'))
        managed = True

# #HONORS 
# class HNCourseStructure(models.Model):
#     BYear = models.IntegerField()
#     BSem = models.IntegerField()
#     Dept = models.IntegerField() 
#     Regulation = models.FloatField()  
#     Creditable = models.IntegerField()
#     Credits = models.IntegerField()
#     count = models.IntegerField()
#     Rigid = models.BooleanField()
#     #history = Historical Records()
#     class Meta:

#         db_table = 'HNCourseStructure'
#         constraints = [
#           models. UniqueConstraint(fields=[ 'Creditable', 'Credits', 'Regulation', 'BYear', 'BSem', 'Dept'], name='Unique HNCourseStructureId')
#         ]
#         managed = True


# class HNCourses (models.Model):
#     SubCode = models.CharField(max_length=10)
#     SubName = models.CharField(max_length=255)
#     Credits = models.IntegerField()
#     OfferedBy = models.IntegerField()
#     CourseStructure = models.ForeignKey("ADAUGDB.HNCourseStructure", on_delete=models.CASCADE)
#     lectures = models.IntegerField()
#     tutorials = models.IntegerField()
#     practicals = models.IntegerField()
#     DistributionRatio = models.TextField()
#     MarkDistribution = models.ForeignKey("ADAUGDB.BTMarksDistribution", on_delete=models.CASCADE)
#     # history = HistoricalRecords()
#     class Meta:
#         db_table = 'HNCourses'
#         constraints = [
#           models.UniqueConstraint(fields = ['SubCode', 'SubName', 'CourseStructure', 'DistributionRatio', 'MarkDistribution'], name="HNCourses_unique_course")
#         ]
#         managed = True

# class HNRegistrationstatus (models.Model):
#     AYear= models.IntegerField() 
#     ASem= models.IntegerField()
#     BYear= models.IntegerField()
#     BSem = models.IntegerField()
#     Regulation = models.FloatField()
#     Dept = models.IntegerField() 
#     Mode = models.CharField(max_length=1) # R for Regular B for Backlog 
#     Status = models.IntegerField() 
#     RollListstatus = models.IntegerField()
#     RollListFeeStatus = models.IntegerField() 
#     # OERollListStatus = models.IntegerField()
#     # OERegistrationStatus = models.IntegerField()
#     RegistrationStatus = models.IntegerField() 
#     MarksStatus = models.IntegerField()
#     Gradestatus = models.IntegerField()
#     #history = Historical Records()

#     class Meta:
#         db_table = 'HNRegistration_Status'
#         constraints = [
#           models.UniqueConstraint(fields=['AYear', 'ASem', 'BYear', 'BSem', 'Regulation', 'Dept', 'Mode'], name='unique HNRegistrationstatus')
#         ]
#         managed = True

#         # def str(self):
#         #   name = str(DEPARTMENTS[self.Dept-1]) + ':' + str(YEARS[self.BYear]) + ':' + str(SEMS[self.BSem])+ ':'+  str(self.AYear) + ':' + str(self.ASem) + ':' + str(self.Regulation) + ':' + str(self.Mode)
#         #   return name

#         # def open_str(self):
#         #   name = str(YEARS[self.BYear]) + ':' + str(SEMS[self.BSem]) +':'+ str(self.AYear) + ':' + str(self.ASem) + ':' + str(self.Regulation) + ':' + str(self.Mode)
#         #   return name