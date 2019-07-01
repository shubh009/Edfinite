"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

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

def CourseList(request):
    """Renders the Course List page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CourseList.html',
        context_instance = RequestContext(request,
        {
            'title':'Course List',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def CourseDetails(request):
    """Renders the Course Details page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/CourseDetails.html',
        context_instance = RequestContext(request,
        {
            'title':'Course Details',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )

def JobDescription(request):
    """Renders the Job Description page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/JobDescription.html',
        context_instance = RequestContext(request,
        {
            'title':'Job Description',
            'message':'Your application description page.',
            'year':datetime.now().year,
        })
    )
