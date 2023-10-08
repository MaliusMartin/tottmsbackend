from django.contrib import admin
from .models import Forms, SchoolLevel, Region, District, School, Subject, SalaryScale, WorkerGrade,Teacher,Gender,Position

# Register your models here.

class FormsAdmin(admin.ModelAdmin):
    list_display = ('id','form_name','form')
    search_fields = ('id','form_name','form')
    list_filter = ('id','form_name','form')
    
class SchoollevelsAdmin(admin.ModelAdmin):
    list_display = ('id','levelName','subvote')
    search_fields = ('id','levelName','subvote')
    list_filter = ('id','levelName','subvote')
    
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')
    list_filter = ('id','name')
    
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','name','votecode','region')
    search_fields = ('id','name','votecode','region')
    list_filter = ('id','name','votecode','region')
    
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('id','name','district','region','School_level')
    search_fields = ('id','name','district','region','School_level')
    list_filter = ('id','name','district','region','School_level')
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','name','subjectcode')
    search_fields = ('id','name','subjectcode')
    list_filter = ('id','name','subjectcode')
    
class SalaryScaleAdmin(admin.ModelAdmin):
    list_display = ('id','scale','amount')
    search_fields = ('id','scale','amount')
    list_filter = ('id','scale','amount')
    
class WorkerGradeAdmin(admin.ModelAdmin):
    list_display = ('id','grade')
    search_fields = ('id','grade')
    list_filter = ('id','grade')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','fname','mname','sname','check_number','grade','gender','position','start_date','date_of_birth','expected_retirement_date','region','district','school_level','school','education_level','subjects_taught','phone','email','password','created_at','updated_at')
    search_fields = ('id','fname','mname','sname','check_number','grade','gender','position','start_date','date_of_birth','expected_retirement_date','region','district','school_level','school','education_level','subjects_taught','phone','email','password','created_at','updated_at')
    list_filter =('id','fname','mname','sname','check_number','grade','gender','position','start_date','date_of_birth','expected_retirement_date','region','district','school_level','school','education_level','subjects_taught','phone','email','password','created_at','updated_at')

    
class  GenderAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')
    list_filter = ('id','name')
    
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('id','name')
    list_filter = ('id','name')
    
    
admin.site.register(Forms,FormsAdmin)
admin.site.register(SchoolLevel,SchoollevelsAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(District,DistrictAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(SalaryScale,SalaryScaleAdmin)
admin.site.register(WorkerGrade,WorkerGradeAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Gender,GenderAdmin)
admin.site.register(Position,PositionAdmin)
admin.site.site_header = "TOTTMS ADMIN"