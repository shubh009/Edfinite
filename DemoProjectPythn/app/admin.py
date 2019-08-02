from app.models import Empdata
from django.contrib import admin
from app.models import Emp,CourseMaster, CourseStats, CourseContent, InstructorMaster, jobContent, JobsAndSalary, LearningHour, LearningPath, StudentMaster, StudentOrderMaster, StudentSubscription, InstLearningHour
from django.contrib.admin.options import  InlineModelAdmin, BaseModelAdmin

admin.site.register(Empdata)
admin.site.register(Emp)
#admin.site.register(CourseMaster)
admin.site.register(CourseStats)
admin.site.register(CourseContent)
admin.site.register(InstructorMaster)
admin.site.register(JobsAndSalary)
admin.site.register(jobContent)
admin.site.register(LearningHour)
admin.site.register(LearningPath)
admin.site.register(StudentMaster)
admin.site.register(StudentOrderMaster)
admin.site.register(StudentSubscription)
admin.site.register(InstLearningHour)

class CourseStatsAdmin(admin.TabularInline):
    model = CourseStats

class CourseContentAdmin(admin.TabularInline):
    model=CourseContent

class CourseMasterAdmin(admin.ModelAdmin):
    inlines = [CourseStatsAdmin, CourseContentAdmin]

admin.site.register(CourseMaster, CourseMasterAdmin)