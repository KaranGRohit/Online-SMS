from django.urls import path
from . import views

from django.conf.urls import url

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    url(r'^getstudentinfo/addstudentinfo/$', views.addstudentinfo),
    url(r'^getstudentinfo/$', views.getstudentinfo),
    url(r'^addsuccess/$', views.addsuccess),
    path('students/', views.StudentListView.as_view(), name='students'),

]
