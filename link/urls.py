from django.contrib import admin
from django.urls import path,include   
from . import views

urlpatterns = [
    
    path('',views.home),
    path('login/',views.login_view),
    path('shome',views.shome),
    path('fhome',views.fhome),
    path('phome',views.phome),
    path('adm',views.adm),
    path('chome',views.chome),
    
    path('adm_companies',views.adm_companies),
    path('accept_com/<id>',views.accept_com),
    path('reject_com/<id>',views.reject_com),
    
    path('accept_stu/<id>',views.accept_stu),
    path('reject_stu/<id>',views.reject_stu),
    
    path('accept_freelancers/<id>',views.accept_freelancers),
    path('reject_freelancers/<id>',views.reject_freelancers),

    path('accept-parttime/<id>',views.accept_parttime),
    path('reject-parttime/<id>',views.reject_parttime),


    path('adm_vaccancy/<id>',views.adm_vaccancy),
    path('adm_request/<id>',views.adm_request),
    
    
    path('adm_student',views.adm_student),
    path('adm-freelancers',views.adm_freelancers),
    path('adm-partime',views.adm_partime),
    
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
    path('stu_freelance_jobs',views.stu_freelance_jobs),
    path('stu_parttime_jobs',views.stu_parttime_jobs),
    path('stu_complaint',views.stu_complaint),
    path('std_vaccancy/<id>',views.std_vaccancy),
    path('std_request/<id>',views.std_request),

    path('freelance-reg',views.freelance_reg),
    path('freelance-profile',views.freelance_profile),
    path('freelance-job-post',views.freelance_job_post),
    path('posted-jobs-freelance',views.posted_jobs_freelance),
    path('std_freelance_request/<id>',views.std_freelance_request),
    path('view-freelance-requests/<id>',views.view_freelance_request),

    
    

    
    
    path('accept_req/<id>',views.accept_req),
    path('reject_req/<id>',views.reject_req),

    path('accept-freelance-req/<id>',views.accept_freelance_req),
    path('reject_freelance_req/<id>',views.reject_freelance_req),

    path('accept-parttime-req/<id>',views.accept_parttime_req),
    path('reject_parttime_req/<id>',views.reject_parttime_req),


    path('parttime-reg',views.parttime_reg),
    path('parttime-profile',views.parttime_profile),
    path('parttime-job-post',views.parttime_job_post),
    path('posted-jobs-parttime',views.posted_jobs_parttime),
    path('std_parttime_request/<id>',views.std_parttime_request),
    path('view-parttime-requests/<id>',views.view_parttime_request),


    
    
    
    
    
    
    
    
    
    
  
    
    
    
    
    
    
    
    
    
    
    
]