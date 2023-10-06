from django.urls import path, re_path
from . import views

urlpatterns = [
    # Define URL patterns for each model view
    
    re_path(r'regions/(?P<region_id>\d+)/districts/(?P<district_id>\d+)/schools/', views.filter_schools, name='filter_schools'),
    
    # ...
    path('education-levels/', views.education_level_api, name='education-levels'),
    path('education-levels/<int:id>/', views.education_level_api, name='education-level-detail'),
    
    path('school-levels/', views.school_level_api, name='school-levels'),
    path('school-levels/<int:id>/', views.school_level_api, name='school-level-detail'),
    
    path('regions/', views.region_api, name='regions'),
    path('regions/<int:id>/', views.region_api, name='region-detail'),
    
    path('districts/', views.district_api, name='districts'),
    path('districts/<int:id>/', views.district_api, name='district-detail'),
    
    
    path('schools/', views.school_api, name='schools'),
    path('schools/<int:id>/', views.school_api, name='school-detail'),
    
    path('subjects/', views.subject_api, name='subjects'),
    path('subjects/<int:id>/', views.subject_api, name='subject-detail'),
    
    path('teachers/', views.teacher_api, name='teachers'),
    path('teachers/<int:id>/', views.teacher_api, name='teacher-detail'),
    
    path('transfer-applications/', views.transfer_application_api, name='transfer-applications'),
    path('transfer-applications/<int:id>/', views.transfer_application_api, name='transfer-application-detail'),
    
    path('special-transfers/', views.special_transfer_api, name='special-transfers'),
    path('special-transfers/<int:id>/', views.special_transfer_api, name='special-transfer-detail'),
    
    path('requests/', views.request_api, name='requests'),
    path('requests/<int:id>/', views.request_api, name='request-detail'),
    
    path('arriving-teachers/', views.arriving_teachers_api, name='arriving-teachers'),
    path('arriving-teachers/<int:id>/', views.arriving_teachers_api, name='arriving-teacher-detail'),
    
    path('user-roles/', views.user_roles_api, name='user-roles'),
    path('user-roles/<int:id>/', views.user_roles_api, name='user-role-detail'),
    
    path('user-role-assignments/', views.user_role_assignment_api, name='user-role-assignments'),
    path('user-role-assignments/<int:id>/', views.user_role_assignment_api, name='user-role-assignment-detail'),
    
    path('notifications/', views.notification_api, name='notifications'),
    path('notifications/<int:id>/', views.notification_api, name='notification-detail'),
    
    path('scale/', views.salary_scale_api, name='salary-scale'),
    path('scale/<int:id>/', views.salary_scale_api, name='salary-scale'),
    
    path('grade/', views.worker_grade_api, name='grade'),
    path('grade/<int:id>/', views.worker_grade_api, name='grade'),
    
    path('regions/<int:id>/districts/', views.get_districts_for_region),
    
    path('forms/<int:id>', views.get_form_data, name='forms'),
    
    
   
    
    # ...
   
    
    # more URL patterns for other views in tottms app
]
