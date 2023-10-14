from rest_framework import serializers
from .models import EducationLevel,  Region, District, School, Subject, Teacher, TransferApplication, SpecialTransfer, Request, ArrivingTeachers, UserRoles, UserRoleAssignment, Notification,SchoolLevel,SalaryScale,WorkerGrade,SalaryTransfer,Gender,Position,TransferReasons

class EducationLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationLevel
        fields = '__all__'

class SchoolLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolLevel
        fields = '__all__'
        
class SalaryScaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryScale
        fields = '__all__'
        
class WorkerGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerGrade
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'  # Include all fields in the serialization

class TransferApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferApplication
        fields = '__all__'  # Include all fields in the serialization
        
class SpecialTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialTransfer
        fields = '__all__'  # Include all fields in the serialization

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'  # Include all fields in the serialization

class ArrivingTeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArrivingTeachers
        fields = '__all__'  # Include all fields in the serialization

class UserRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoles
        fields = '__all__'  # Include all fields in the serialization

class UserRoleAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRoleAssignment
        fields = '__all__'  # Include all fields in the serialization

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'  # Include all fields in the serialization
        
class SalaryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryTransfer
        fields = '__all__'  # Include all fields in the serialization
        
class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields  = '__all__'
        
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'
        
class TransferReasonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferReasons
        fields = '__all__'