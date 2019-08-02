"""
Definition of models.
"""

from django.db import models

# Create your models here.
#class Event(models.Model):
#     name=models.CharField('Event Name', max_length=120)
#     event_date = models.DateTimeField('Event Date')
#     venue = models.CharField(max_length=120)
#     manager = models.CharField(max_length = 60)
#     description = models.TextField(blank=True)

#testing database tables
class Emp(models.Model):
    empid=models.IntegerField(max_length=10)
    empname=models.CharField(max_length=120)
    empemail=models.CharField(max_length=200)
    empcontact=models.IntegerField(max_length=12)

class Empdata(models.Model):
    empname=models.CharField(max_length=120, primary_key=True)
    empemail=models.CharField(max_length=200)
    empcontact=models.IntegerField(max_length=12)

#Edufinte database tables.

class CourseMaster(models.Model):
    CourseId=models.IntegerField(max_length=10, primary_key=True)
    CourseTitle=models.CharField(max_length=100)
    CoursePrice=models.IntegerField()
    CourseSummary=models.CharField(max_length=1000)
    ImagePath=models.CharField(max_length=150)
    IsActive=models.BooleanField()
    def __unicode__(self):      
        return self.CourseTitle
    class Meta:
        ordering = ('CourseTitle',)
        verbose_name = 'Course Master'
        verbose_name_plural = 'Course Masters'


class CourseStats(models.Model):
         CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE  )
         Duration=models.IntegerField()
         CourseLevel=models.CharField(max_length=50)
         Eligibility=models.CharField(max_length=50)
         TutionFee=models.IntegerField()
         AvgSalary=models.IntegerField()
         AdmisionExam=models.CharField(max_length=50)
         Isactiv=models.BooleanField()
         def __unicode__(self):      
            return self.CourseLevel

class CourseContent(models.Model):
    CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE  )
    Paraid=models.IntegerField()
    Paraheading=models.CharField(max_length=100)
    Paracontent=models.CharField(max_length=5000)
    isctive =models.BooleanField()
    def __unicode__(self):      
            return self.Paraheading

class JobsAndSalary(models.Model):
    courseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    Jobid=models.IntegerField(max_length=10, primary_key=True)
    ProfileName=models.CharField(max_length=150)
    AvgSalary=models.IntegerField()
    ImaagePath=models.CharField(max_length=100)
    ParaSummary=models.CharField(max_length=250)
    isactive=models.BooleanField()
    def __unicode__(self):      
            return self.ProfileName

class jobContent(models.Model):
    Contentoid=models.IntegerField()
    JobId=models.ForeignKey(JobsAndSalary, on_delete=models.CASCADE)
    CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    ParaName=models.CharField(max_length=500)
    ParaContent=models.CharField(max_length=5000)
    Isactive =models.BooleanField()
    def __unicode__(self):      
            return self.ParaName

class LearningPath(models.Model):
    PathId =models.IntegerField()
    JobId=models.ForeignKey(JobsAndSalary, on_delete=models.CASCADE)
    CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    PathTittle=models.CharField(max_length=200)
    PathDescription=models.CharField(max_length=2000)
    def __unicode__(self):
        return self.PathTittle

class InstructorMaster(models.Model):
    InstructorId=models.IntegerField(max_length=10, primary_key=True)
    Name=models.CharField(max_length=100)
    EmailId=models.CharField(max_length=256)
    ContactNo=models.IntegerField()
    Education=models.CharField(max_length=100)
    Exp=models.IntegerField()
    JobId=models.ForeignKey(JobsAndSalary, on_delete=models.CASCADE)
    CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    ImagePath=models.CharField(max_length=256)
    isactive=models.BooleanField()
    def __unicode__(self):
        return self.Name

class LearningHour(models.Model):
    HourId=models.IntegerField(max_length=10, primary_key=True)
    LearningTimeSlot=models.CharField(max_length=50)
    Isactive=models.BooleanField()
    def __unicode__(self):
        return self.LearningTimeSlot

class InstLearningHour(models.Model):
    InstructorId=models.ForeignKey(InstructorMaster, on_delete=models.CASCADE)
    HourId=models.ForeignKey(LearningHour, on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    isactive=models.BooleanField()
    def __unicode__(self):
        return self.Name

#class InstructorHour(models.Model):
#      InstructorId=models.ForeignKey(InstructorMaster, on_delete=models.CASCADE)
#      HourId=models.ForeignKey(LearningHour, on_delete=models.CASCADE)
#      Name=models.CharField(max_length=100)
#      isactive=models.BooleanField()
#      def __unicode__(self):
#        return self.Name

class StudentMaster(models.Model):
    StudentId=models.IntegerField()
    Name=models.CharField(max_length=100)
    EmailId=models.CharField(max_length=256)
    ContactNo=models.IntegerField()
    Education=models.CharField(max_length=100)
    DOB=models.CharField(max_length=20)
    SignupDate=models.CharField(max_length=15)
    Isactive=models.BooleanField()
    def __unicode__(self):
        return self.Name

class StudentSubscription(models.Model):
    StudentId=models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    InstrucorId=models.ForeignKey(InstructorMaster, on_delete=models.CASCADE)
    HourId=models.ForeignKey(LearningHour, on_delete=models.CASCADE)
    SubscriptionStartate=models.CharField(max_length=20)
    SubscriptionEndDate=models.CharField(max_length=20)
    Isactive=models.BooleanField()
    def __unicode__(self):
        return self.StudentId

class StudentOrderMaster(models.Model):
    StudentId=models.ForeignKey(StudentMaster, on_delete=models.CASCADE)
    OrderId=models.IntegerField()
    CourseId=models.ForeignKey(CourseMaster, on_delete=models.CASCADE)
    OrderDate=models.CharField(max_length=20)
    IsOrderConfirm=models.BooleanField()
    def __unicode__(self):
        return self.StudentId
    


class std(models.Model):
    stdid=models.IntegerField()
    stdname=models.CharField(max_length=200)

class Stddd(models.Model):
    stdid=models.IntegerField()
    stdname=models.CharField(max_length=200)

