#from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
#import pymysql
from Teacher_App.models import Result
from django.template.context_processors import csrf
from django.views import generic

class IndexView(TemplateView):
    template_name = 'teacher/index.html'


def Result(request):
    rid = request.POST.get('rid','')
    grade = request.POST.get('grade','')
    sub1 = request.POST.get('sub1','')
    sub2 = request.POST.get('sub2','')
    sub3 = request.POST.get('sub3','')
    marks1 = request.POST.get('marks1','')
    marks2 = request.POST.get('marks2','')
    marks3 = request.POST.get('marks3','')
    r = Result(Rid=rid, grade=grade, sub1=sub1, sub2=sub2, sub3=sub3, marks1=marks1, marks2=marks2, marks3=marks3)
    r.save()
    return HttpResponseRedirect('')
    return HttpResponseRedirect('teacher/addresult/')