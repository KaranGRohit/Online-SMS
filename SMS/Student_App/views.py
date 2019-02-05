from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
#import pymysql
from Student_App.models import Student
from django.template.context_processors import csrf
from django.views import generic

class StudentListView(generic.ListView):
	model = Student


def getstudentinfo(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('addstudentinfo.html', c)

def addstudentinfo(request):
    sfname = request.POST.get('sfname', '')
    slname = request.POST.get('slname', '')
    saddr = request.POST.get('saddr', '')
    semail = request.POST.get('semail', '')
    sclass = request.POST.get('sclass', '')
    s = Student(SFName=sfname, SLname=slname, SAddress=saddr, SEmail=semail, SClass=sclass)
    s.save()

    res = 'Printing all Student entries in the DB : <br>'

    return HttpResponseRedirect('student/addsuccess/')


def addsuccess(request):
	return render_to_response('addrecord.html')
