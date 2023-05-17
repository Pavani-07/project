from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BTFaculty_user(models.Model):

    User= models.ForeignKey(User, on_delete=models.CASCADE)

    Faculty = models.ForeignKey('BTExamStaffDB.BTFacultyInfo', on_delete=models.CASCADE)

    AssignDate = models.DateTimeField(auto_now_add=True)

    RevokeDate = models.DateTimeField(null=True)

    #history = HistoricalRecords()

    class Meta:

        db_table = 'BTFaculty_user'

        unique_together=(('User', 'Faculty', 'AssignDate', 'RevokeDate'))

        managed = True


class BTCoordinator(models.Model):

    User= models.ForeignKey(User, on_delete=models.CASCADE)

    Faculty = models.ForeignKey('BTExamStaffDB.BTFacultyInfo', on_delete=models.CASCADE)

    Dept = models.IntegerField()

    BYear = models.IntegerField()

    AssignDate = models.DateTimeField(auto_now_add=True)

    RevokeDate = models.DateTimeField(null=True)

    #history = HistoricalRecords()

    class Meta:

        db_table = 'BTFaculty_Coordinator'

        unique_together=(('User', 'Faculty', 'AssignDate', 'RevokeDate'))

        managed = True