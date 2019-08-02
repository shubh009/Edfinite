"""
Definition of urls for DemoProjectPythn.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm

from . import  settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from django.views.generic.list import ListView
from app.models import Emp
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^about', 'app.views.about', name='about'),
      url(r'^CourseList', 'app.views.CourseList', name='CourseList'),
       url(r'^CourseDetails', 'app.views.CourseDetails', name='CourseDetails'),
       url(r'^JobDescription', 'app.views.JobDescription', name='JobDescription'),
        url(r'^BookAppointment', 'app.views.BookAppointment', name='BookAppointment'),
       # url(r'^EmpList', 'app.views.EmpList', name='EmpList'),
       #url(r'^AddEmp', 'app.views.AddEmp', name='AddEmp'),
        url(r'^EmpForm', 'app.views.EmpForm', name='EmpForm'),
       
       
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)