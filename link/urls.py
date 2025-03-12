from django.contrib import admin
from django.urls import path,include   
from . import views

urlpatterns = [
    
    path('',views.home),
    path('logins',views.login),
    path('shome',views.shome),
    path('adm',views.adm),
    path('chome',views.chome),
    
    path('adm_companies',views.adm_companies),
    path('accept_com/<id>',views.accept_com),
    path('reject_com/<id>',views.reject_com),
    
    path('accept_stu/<id>',views.accept_stu),
    path('reject_stu/<id>',views.reject_stu),
    
    path('adm_vaccancy/<id>',views.adm_vaccancy),
    path('adm_request/<id>',views.adm_request),
    
    
    path('adm_student',views.adm_student),
    path('adm_department',views.adm_department),
    path('adm_complaint',views.adm_complaint),
    path('adm_reply/<id>',views.adm_reply),
    
    
    
    path('company_reg',views.company_reg),
    path('company_profile',views.company_profile),
    path('add_vaccancy',views.add_vaccancy),
    path('job_request/<id>',views.job_request),
    path('com_complaint',views.com_complaint),
    
    
    path('student_reg',views.student_reg),
    path('stu_profile',views.stu_profile),
    path('stu_companies',views.stu_companies),
    path('stu_complaint',views.stu_complaint),
    path('std_vaccancy/<id>',views.std_vaccancy),
    path('std_request/<id>',views.std_request),
    
    
    path('accept_req/<id>',views.accept_req),
    path('reject_req/<id>',views.reject_req),
    
    
    
    
    
    
    
    
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
]