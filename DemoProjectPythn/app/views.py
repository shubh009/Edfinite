"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Emp
from .models import Empdata
from .models import *

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        context_instance = RequestContext(request,
        {
            'title':'About Mission and Vission',
            'message':'Few words about your websites and goals. ',
            'year':datetime.now().year,
        })
    )

def EmpList(request):
    """Renders the Book Appointment page."""
    assert isinstance(request, HttpRequest)
    All_Emp=Empdata.objects.all()
    return render(
        request,
        'app/EmpList.html',
        context_instance = RequestContext(request,
        {
            'Emplist':All_Emp,
            'title':'Book Appointment With your mentor',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def CourseList(request):
    """Renders the Course List page."""
    assert isinstance(request, HttpRequest)
    All_course=CourseMaster.objects.all()
    return render(
        request,
        'app/CourseList.html',
        context_instance = RequestContext(request,
        {
            'CourseList':All_course,
            'title':'Course List',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def CourseDetails(request):
    """Renders the Course Details page."""
    assert isinstance(request, HttpRequest)
    x = request.GET.get('cid')
    cdd=CourseStats.objects.get(CourseId=x)
    Course=CourseMaster.objects.get(CourseId=x)
    CourseCnt=CourseContent.objects.get(CourseId=x)
    All_course=CourseMaster.objects.all()
    All_joblist=JobsAndSalary.objects.filter(courseId=x)
    #print("Course Id is"+ cdd.CourseLevel)
    #print("Course Id is"+ Course.CourseTitle)
    #print("Course Id is:" + CourseCnt.Paraheading)
    return render(
        request,
        'app/CourseDetails.html',
        context_instance = RequestContext(request,
        {
            'CourseId':x,
            'CourseDetail':cdd,
            'CourseMaster': Course,
            'CourseContent': CourseCnt,
             'CourseList':All_course,
             'JobList':All_joblist,
            'title':'Course Details',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def JobDescription(request):
    """Renders the Job Description page."""
    assert isinstance(request, HttpRequest)
    Query_jid = request.GET.get('jid')
    print("Job  Id is"+ Query_jid)
    cdd=JobsAndSalary.objects.get(Jobid=Query_jid)
    JobDesc=jobContent.objects.get(JobId=Query_jid)
    JobLearningPath=LearningPath.objects.filter(JobId=Query_jid)
    JobIntrustor=InstructorMaster.objects.filter(JobId=Query_jid)
    return render(
        request,
        'app/JobDescription.html',
        context_instance = RequestContext(request,
        {
            'JobInfo': cdd,
            'Job_Desc':JobDesc,
            'Job_LearningPath':JobLearningPath,
            'Job_Instrustor':JobIntrustor,
            'title':'Job Description',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )



def BookAppointment(request):
    """Renders the Book Appointment page."""
    assert isinstance(request, HttpRequest)
    Query_Instid=request.GET.get('Instid')
    InstInfo=InstructorMaster.objects.get(InstructorId=Query_Instid)
    print("InstructorId is"+ InstInfo.Name)
    return render(
        request,
        'app/BookAppointment.html',
        context_instance = RequestContext(request,
        {
            'Inst_info': InstInfo,
            'title':'Book Appointment With your mentor',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def AddEmp(request):
    assert isinstance(request, HttpRequest)
    return render(
        request, 'app/AddEmp.html', context_instance = RequestContext(request,
        {
            'title':'Book Appointment With your mentor',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
   )

def EmpList(request):
    """Renders the Book Appointment page."""
    assert isinstance(request, HttpRequest)
    All_Emp=Empdata.objects.all()
    return render(
        request,
        'app/EmpList.html',
        context_instance = RequestContext(request,
        {
            'Emplist':All_Emp,
            'title':'Book Appointment With your mentor',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def EmpForm(request):
    """Renders the Book Appointment page."""
    assert isinstance(request, HttpRequest)
    print("Form Submission")
    str="shubhanshu"
    Emp_Name=request.POST.get("EmpName");
    Emp_Email=request.POST.get("EmpEmail");
    Emp_Contact=request.POST.get("EmpContact");
    Emp_info=Empdata(empname=Emp_Name, empemail=Emp_Email, empcontact=Emp_Contact);
    print(Emp_Name, Emp_Email, Emp_Contact, str)
    Emp_info.save();
    return render(
        request,
        'app/AddEmp.html',
        context_instance = RequestContext(request,
        {
            'title':'Add New Employee into database',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )




