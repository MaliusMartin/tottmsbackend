from django.shortcuts import render
import rest_framework.status as status
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import EducationLevel, Region, District, School, Subject, Teacher, TransferApplication, SpecialTransfer, Request, ArrivingTeachers, UserRoles, UserRoleAssignment, Notification,SchoolLevel,SalaryScale,WorkerGrade,SalaryTransfer
from .serializers import EducationLevelSerializer,  RegionSerializer, DistrictSerializer, SchoolSerializer, SubjectSerializer, TeacherSerializer, TransferApplicationSerializer, SpecialTransferSerializer, RequestSerializer, ArrivingTeachersSerializer,UserRolesSerializer, UserRoleAssignmentSerializer, NotificationSerializer,SchoolLevelSerializer, SalaryScaleSerializer,WorkerGradeSerializer,SalaryTransferSerializer


# Create your views here.

@csrf_exempt
def education_level_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            education_levels = EducationLevel.objects.all()
            education_level_serializer = EducationLevelSerializer(education_levels, many=True)
            return JsonResponse(education_level_serializer.data, safe=False)
        else:
            try:
                education_level = EducationLevel.objects.get(pk=id)
                education_level_serializer = EducationLevelSerializer(education_level)
                return JsonResponse(education_level_serializer.data)
            except EducationLevel.DoesNotExist:
                return JsonResponse("Education level not found", status=404)

    elif request.method == "POST":
        education_level_data = JSONParser().parse(request)
        education_level_serializer = EducationLevelSerializer(data=education_level_data)
        if education_level_serializer.is_valid():
            education_level_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(education_level_serializer.errors, status=400)

    elif request.method == "PUT":
        education_level_data = JSONParser().parse(request)
        try:
            education_level = EducationLevel.objects.get(pk=id)
        except EducationLevel.DoesNotExist:
            return JsonResponse("Education level not found", status=404)

        education_level_serializer = EducationLevelSerializer(education_level, data=education_level_data)
        if education_level_serializer.is_valid():
            education_level_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(education_level_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            education_level = EducationLevel.objects.get(pk=id)
            education_level.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except EducationLevel.DoesNotExist:
            return JsonResponse("Education level not found", status=404)
        
        
@csrf_exempt
def school_level_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            school_levels = SchoolLevel.objects.all()
            school_level_serializer = SchoolLevelSerializer(school_levels, many=True)
            return JsonResponse( school_level_serializer.data, safe=False)
        else:
            try:
               school_level = SchoolLevel.objects.get(pk=id)
               school_level_serializer = SchoolLevelSerializer(school_level)
               return JsonResponse(school_level_serializer.data,safe=False)
            except SchoolLevel.DoesNotExist:
                return JsonResponse("School Level not found", status=404)

    elif request.method == "POST":
        school_level_data = JSONParser().parse(request)
        school_level_serializer = SchoolLevelSerializer(data=school_level_data)
        if school_level_serializer.is_valid():
            school_level_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(school_level_serializer.errors, status=400)

    elif request.method == "PUT":
        school_level_data = JSONParser().parse(request)
        try:
           school_level = SchoolLevel.objects.get(pk=id)
        except SchoolLevel.DoesNotExist:
            return JsonResponse("Teacher category not found", status=404)

        school_level_serializer = SchoolLevelSerializer(school_level, data=school_level_data)
        if school_level_serializer.is_valid():
            school_level_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(school_level_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
           school_level = SchoolLevel.objects.get(pk=id)
           school_level.delete()
           return JsonResponse("Deleted Successfully", safe=False)
        except SchoolLevel.DoesNotExist:
            return JsonResponse("School level not found", status=404)

@csrf_exempt
def region_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            regions = Region.objects.all()
            region_serializer = RegionSerializer(regions, many=True)
            return JsonResponse(region_serializer.data, safe=False)
        else:
            try:
                region = Region.objects.get(pk=id)
                region_serializer = RegionSerializer(region)
                return JsonResponse(region_serializer.data)
            except Region.DoesNotExist:
                return JsonResponse("Region not found", status=404)

    elif request.method == "POST":
        region_data = JSONParser().parse(request)
        region_serializer = RegionSerializer(data=region_data)
        if region_serializer.is_valid():
            region_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(region_serializer.errors, status=400)

    elif request.method == "PUT":
        region_data = JSONParser().parse(request)
        try:
            region = Region.objects.get(pk=id)
        except Region.DoesNotExist:
            return JsonResponse("Region not found", status=404)

        region_serializer = RegionSerializer(region, data=region_data)
        if region_serializer.is_valid():
            region_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(region_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            region = Region.objects.get(pk=id)
            region.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Region.DoesNotExist:
            return JsonResponse("Region not found", status=404)
        
        
@csrf_exempt
def district_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            districts = District.objects.all()
            district_serializer = DistrictSerializer(districts, many=True)
            return JsonResponse(district_serializer.data, safe=False)
        else:
            try:
                district = District.objects.get(pk=id)
                district_serializer = DistrictSerializer(district)
                return JsonResponse(district_serializer.data)
            except District.DoesNotExist:
                return JsonResponse("District not found", status=404)

    elif request.method == "POST":
        district_data = JSONParser().parse(request)
        district_serializer = DistrictSerializer(data=district_data)
        if district_serializer.is_valid():
            district_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(district_serializer.errors, status=400)

    elif request.method == "PUT":
        district_data = JSONParser().parse(request)
        try:
            district = District.objects.get(pk=id)
        except District.DoesNotExist:
            return JsonResponse("District not found", status=404)

        district_serializer = DistrictSerializer(district, data=district_data)
        if district_serializer.is_valid():
            district_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(district_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            district = District.objects.get(pk=id)
            district.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except District.DoesNotExist:
            return JsonResponse("District not found", status=404)
        
        
@csrf_exempt
def school_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            schools = School.objects.all()
            school_serializer = SchoolSerializer(schools, many=True)
            return JsonResponse(school_serializer.data, safe=False)
        else:
            try:
                school = School.objects.get(pk=id)
                school_serializer = SchoolSerializer(school)
                return JsonResponse(school_serializer.data)
            except School.DoesNotExist:
                return JsonResponse("School not found", status=404)

    elif request.method == "POST":
        school_data = JSONParser().parse(request)
        school_serializer = SchoolSerializer(data=school_data)
        if school_serializer.is_valid():
            school_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(school_serializer.errors, status=400)

    elif request.method == "PUT":
        school_data = JSONParser().parse(request)
        try:
            school = School.objects.get(pk=id)
        except School.DoesNotExist:
            return JsonResponse("School not found", status=404)

        school_serializer = SchoolSerializer(school, data=school_data)
        if school_serializer.is_valid():
            school_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(school_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            school = School.objects.get(pk=id)
            school.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except School.DoesNotExist:
            return JsonResponse("School not found", status=404)
        
        
@csrf_exempt
def subject_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            subjects = Subject.objects.all()
            subject_serializer = SubjectSerializer(subjects, many=True)
            return JsonResponse(subject_serializer.data, safe=False)
        else:
            try:
                subject = Subject.objects.get(pk=id)
                subject_serializer = SubjectSerializer(subject)
                return JsonResponse(subject_serializer.data)
            except Subject.DoesNotExist:
                return JsonResponse("Subject not found", status=404)

    elif request.method == "POST":
        subject_data = JSONParser().parse(request)
        subject_serializer = SubjectSerializer(data=subject_data)
        if subject_serializer.is_valid():
            subject_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(subject_serializer.errors, status=400)

    elif request.method == "PUT":
        subject_data = JSONParser().parse(request)
        try:
            subject = Subject.objects.get(pk=id)
        except Subject.DoesNotExist:
            return JsonResponse("Subject not found", status=404)

        subject_serializer = SubjectSerializer(subject, data=subject_data)
        if subject_serializer.is_valid():
            subject_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(subject_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            subject = Subject.objects.get(pk=id)
            subject.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Subject.DoesNotExist:
            return JsonResponse("Subject not found", status=404)
        

@csrf_exempt
def teacher_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            teachers = Teacher.objects.all()
            teacher_serializer = TeacherSerializer(teachers, many=True)
            return JsonResponse(teacher_serializer.data, safe=False)
        else:
            try:
                teacher = Teacher.objects.get(pk=id)
                teacher_serializer = TeacherSerializer(teacher)
                return JsonResponse(teacher_serializer.data)
            except Teacher.DoesNotExist:
                return JsonResponse("Teacher not found", status=404)

    elif request.method == "POST":
        teacher_data = JSONParser().parse(request)
        teacher_serializer = TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(teacher_serializer.errors, status=400)

    elif request.method == "PUT":
        teacher_data = JSONParser().parse(request)
        try:
            teacher = Teacher.objects.get(pk=id)
        except Teacher.DoesNotExist:
            return JsonResponse("Teacher not found", status=404)

        teacher_serializer = TeacherSerializer(teacher, data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(teacher_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            teacher = Teacher.objects.get(pk=id)
            teacher.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Teacher.DoesNotExist:
            return JsonResponse("Teacher not found", status=404)

@csrf_exempt
def transfer_application_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            transfer_applications = TransferApplication.objects.all()
            transfer_application_serializer = TransferApplicationSerializer(transfer_applications, many=True)
            return JsonResponse(transfer_application_serializer.data, safe=False)
        else:
            try:
                transfer_application = TransferApplication.objects.get(pk=id)
                transfer_application_serializer = TransferApplicationSerializer(transfer_application)
                return JsonResponse(transfer_application_serializer.data)
            except TransferApplication.DoesNotExist:
                return JsonResponse("Transfer Application not found", status=404)

    elif request.method == "POST":
        transfer_application_data = JSONParser().parse(request)
        transfer_application_serializer = TransferApplicationSerializer(data=transfer_application_data)
        if transfer_application_serializer.is_valid():
            transfer_application_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(transfer_application_serializer.errors, status=400)

    elif request.method == "PUT":
        transfer_application_data = JSONParser().parse(request)
        try:
            transfer_application = TransferApplication.objects.get(pk=id)
        except TransferApplication.DoesNotExist:
            return JsonResponse("Transfer Application not found", status=404)

        transfer_application_serializer = TransferApplicationSerializer(transfer_application, data=transfer_application_data)
        if transfer_application_serializer.is_valid():
            transfer_application_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(transfer_application_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            transfer_application = TransferApplication.objects.get(pk=id)
            transfer_application.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except TransferApplication.DoesNotExist:
            return JsonResponse("Transfer Application not found", status=404)
        
        
@csrf_exempt
def special_transfer_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            special_transfers = SpecialTransfer.objects.all()
            special_transfer_serializer = SpecialTransferSerializer(special_transfers, many=True)
            return JsonResponse(special_transfer_serializer.data, safe=False)
        else:
            try:
                special_transfer = SpecialTransfer.objects.get(pk=id)
                special_transfer_serializer = SpecialTransferSerializer(special_transfer)
                return JsonResponse(special_transfer_serializer.data)
            except SpecialTransfer.DoesNotExist:
                return JsonResponse("Special Transfer not found", status=404)

    elif request.method == "POST":
        special_transfer_data = JSONParser().parse(request)
        special_transfer_serializer = SpecialTransferSerializer(data=special_transfer_data)
        if special_transfer_serializer.is_valid():
            special_transfer_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(special_transfer_serializer.errors, status=400)

    elif request.method == "PUT":
        special_transfer_data = JSONParser().parse(request)
        try:
            special_transfer = SpecialTransfer.objects.get(pk=id)
        except SpecialTransfer.DoesNotExist:
            return JsonResponse("Special Transfer not found", status=404)

        special_transfer_serializer = SpecialTransferSerializer(special_transfer, data=special_transfer_data)
        if special_transfer_serializer.is_valid():
            special_transfer_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(special_transfer_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            special_transfer = SpecialTransfer.objects.get(pk=id)
            special_transfer.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except SpecialTransfer.DoesNotExist:
            return JsonResponse("Special Transfer not found", status=404)
        
        
@csrf_exempt
def request_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            requests = Request.objects.all()
            request_serializer = RequestSerializer(requests, many=True)
            return JsonResponse(request_serializer.data, safe=False)
        else:
            try:
                request_obj = Request.objects.get(pk=id)
                request_serializer = RequestSerializer(request_obj)
                return JsonResponse(request_serializer.data)
            except Request.DoesNotExist:
                return JsonResponse("Request not found", status=404)

    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        request_serializer = RequestSerializer(data=request_data)
        if request_serializer.is_valid():
            request_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(request_serializer.errors, status=400)

    elif request.method == "PUT":
        request_data = JSONParser().parse(request)
        try:
            request_obj = Request.objects.get(pk=id)
        except Request.DoesNotExist:
            return JsonResponse("Request not found", status=404)

        request_serializer = RequestSerializer(request_obj, data=request_data)
        if request_serializer.is_valid():
            request_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(request_serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            request_obj = Request.objects.get(pk=id)
            request_obj.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Request.DoesNotExist:
            return JsonResponse("Request not found", status=404)
        
@csrf_exempt
def arriving_teachers_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            arriving_teachers = ArrivingTeachers.objects.all()
            serializer = ArrivingTeachersSerializer(arriving_teachers, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                arriving_teacher = ArrivingTeachers.objects.get(pk=id)
                serializer = ArrivingTeachersSerializer(arriving_teacher)
                return JsonResponse(serializer.data)
            except ArrivingTeachers.DoesNotExist:
                return JsonResponse("Arriving Teacher not found", status=404)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArrivingTeachersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            arriving_teacher = ArrivingTeachers.objects.get(pk=id)
        except ArrivingTeachers.DoesNotExist:
            return JsonResponse("Arriving Teacher not found", status=404)

        serializer = ArrivingTeachersSerializer(arriving_teacher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            arriving_teacher = ArrivingTeachers.objects.get(pk=id)
            arriving_teacher.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except ArrivingTeachers.DoesNotExist:
            return JsonResponse("Arriving Teacher not found", status=404)
        
        
@csrf_exempt
def user_roles_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            user_roles = UserRoles.objects.all()
            serializer = UserRolesSerializer(user_roles, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                user_role = UserRoles.objects.get(pk=id)
                serializer = UserRolesSerializer(user_role)
                return JsonResponse(serializer.data)
            except UserRoles.DoesNotExist:
                return JsonResponse("User Role not found", status=404)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserRolesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            user_role = UserRoles.objects.get(pk=id)
        except UserRoles.DoesNotExist:
            return JsonResponse("User Role not found", status=404)

        serializer = UserRolesSerializer(user_role, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            user_role = UserRoles.objects.get(pk=id)
            user_role.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except UserRoles.DoesNotExist:
            return JsonResponse("User Role not found", status=404)
        

@csrf_exempt
def user_role_assignment_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            assignments = UserRoleAssignment.objects.all()
            serializer = UserRoleAssignmentSerializer(assignments, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                assignment = UserRoleAssignment.objects.get(pk=id)
                serializer = UserRoleAssignmentSerializer(assignment)
                return JsonResponse(serializer.data)
            except UserRoleAssignment.DoesNotExist:
                return JsonResponse("User Role Assignment not found", status=404)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = UserRoleAssignmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            assignment = UserRoleAssignment.objects.get(pk=id)
        except UserRoleAssignment.DoesNotExist:
            return JsonResponse("User Role Assignment not found", status=404)

        serializer = UserRoleAssignmentSerializer(assignment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            assignment = UserRoleAssignment.objects.get(pk=id)
            assignment.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except UserRoleAssignment.DoesNotExist:
            return JsonResponse("User Role Assignment not found", status=404)
        
        
@csrf_exempt
def notification_api(request, id=0):
    if request.method == "GET":
        if id == 0:
            notifications = Notification.objects.all()
            serializer = NotificationSerializer(notifications, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                notification = Notification.objects.get(pk=id)
                serializer = NotificationSerializer(notification)
                return JsonResponse(serializer.data)
            except Notification.DoesNotExist:
                return JsonResponse("Notification not found", status=404)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = NotificationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        try:
            notification = Notification.objects.get(pk=id)
        except Notification.DoesNotExist:
            return JsonResponse("Notification not found", status=404)

        serializer = NotificationSerializer(notification, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        try:
            notification = Notification.objects.get(pk=id)
            notification.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Notification.DoesNotExist:
            return JsonResponse("Notification not found", status=404)
        
        
# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes([permissions.AllowAny])
@csrf_exempt
def salary_scale_api(request, id=0):
    if request.method == 'GET':
        if id == 0:
            salary_scales = SalaryScale.objects.all()
            serializer = SalaryScaleSerializer(salary_scales, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            try:
                salary_scale = SalaryScale.objects.get(pk=id)
                serializer = SalaryScaleSerializer(salary_scale)
                return JsonResponse(serializer.data, safe=False)
            except SalaryScale.DoesNotExist:
                return JsonResponse('SalaryScale not found',safe=False, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = SalaryScaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Successfully', status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            salary_scale = SalaryScale.objects.get(pk=id)
        except SalaryScale.DoesNotExist:
            return JsonResponse('SalaryScale not found', status=status.HTTP_404_NOT_FOUND)

        serializer = SalaryScaleSerializer(salary_scale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated Successfully', status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            salary_scale = SalaryScale.objects.get(pk=id)
            salary_scale.delete()
            return JsonResponse('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
        except SalaryScale.DoesNotExist:
            return JsonResponse('SalaryScale not found', status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([permissions.AllowAny])
@csrf_exempt
def worker_grade_api(request, id=0):
    if request.method == 'GET':
        if id == 0:
            worker_grades = WorkerGrade.objects.all()
            serializer = WorkerGradeSerializer(worker_grades, many=True)
            return JsonResponse(serializer.data, safe=False)

        else:
            try:
                worker_grade = WorkerGrade.objects.get(pk=id)
                serializer = WorkerGradeSerializer(worker_grade)
                return JsonResponse(serializer.data,safe=False)
            except WorkerGrade.DoesNotExist:
                return JsonResponse('WorkerGrade not found',safe=False, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = WorkerGradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Successfully', status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            worker_grade = WorkerGrade.objects.get(pk=id)
        except WorkerGrade.DoesNotExist:
            return JsonResponse('WorkerGrade not found', status=status.HTTP_404_NOT_FOUND)

        serializer = WorkerGradeSerializer(worker_grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated Successfully', status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            worker_grade = WorkerGrade.objects.get(pk=id)
            worker_grade.delete()
            return JsonResponse('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
        except WorkerGrade.DoesNotExist:
            return JsonResponse('WorkerGrade not found', status=status.HTTP_404_NOT_FOUND)
        

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# @permission_classes([permissions.AllowAny])
@csrf_exempt
def salary_transfer_api(request, id=0):
    if request.method == 'GET':
        if id == 0:
            salary_transfers = SalaryTransfer.objects.all()
            serializer = SalaryTransferSerializer(salary_transfers, many=True)
            return JsonResponse(serializer.data,safe=False)

        else:
            try:
                salary_transfer = SalaryTransfer.objects.get(pk=id)
                serializer = SalaryTransferSerializer(salary_transfer)
                return JsonResponse(serializer.data,safe=False)
            except SalaryTransfer.DoesNotExist:
                return JsonResponse('SalaryTransfer not found',safe=False, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = SalaryTransferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Added Successfully', status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            salary_transfer = SalaryTransfer.objects.get(pk=id)
        except SalaryTransfer.DoesNotExist:
            return JsonResponse('SalaryTransfer not found', status=status.HTTP_404_NOT_FOUND)

        serializer = SalaryTransferSerializer(salary_transfer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse('Updated Successfully', status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            salary_transfer = SalaryTransfer.objects.get(pk=id)
            salary_transfer.delete()
            return JsonResponse('Deleted Successfully', status=status.HTTP_204_NO_CONTENT)
        except SalaryTransfer.DoesNotExist:
            return JsonResponse('SalaryTransfer not found', status=status.HTTP_404_NOT_FOUND)
        
        
@csrf_exempt
def get_districts_for_region(request, id):
    region = Region.objects.get(pk=id)
    districts = District.objects.filter(region=region)

    district_data = []
    for district in districts:
        district_data.append({
            'id': district.id,
            'name': district.name,
        })

    return JsonResponse(district_data, safe=False)
